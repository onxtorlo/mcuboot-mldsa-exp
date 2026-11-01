#!/usr/bin/env python3
"""ChkUp steps 2-3 for MCUboot: verification procedure recognition + vulnerability discovery.

Input: an analysis build made with boot_conf/callgraph.conf (call graph .ci files and
-fdump-tree-optimized-lineno GIMPLE dumps next to every object file).

Step 2 (ChkUp 4.2), adapted to source builds:
  * key functions are matched by symbol name against CORPUS (ChkUp needs feature similarity
    + DFG isomorphism because it works on stripped binaries; a source build keeps names);
  * a key call counts as a verification procedure only if its result, or the buffer it
    writes (pass-by-reference), reaches a conditional expression (ChkUp's reaching-
    definition rule). The check runs on GIMPLE SSA and follows values across function
    boundaries through return values and output parameters.
Step 3 (ChkUp 4.3): per property (authenticity, integrity, freshness, compatibility) the
  verdict is missing / improper / ok; plus two proposed properties:
  P5 unsigned-field use (TLVs read from the unprotected area, cf. CVE-2024-32883),
  P6 anti-rollback value protection (where the compared version / counter comes from).

usage: scripts/chkup_analyze.py <build_dir> --out <dir> [--entry main]
output: procedures.tsv (every key call on the path and where its value goes),
        tlv_reads.tsv (P5), verdict.json, verdict.md
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import callgraph_paths as cg  # noqa: E402  (step 1)

# ---------------------------------------------------------------- corpus (ChkUp Table 5)
# name: (property, proper?, how the verdict leaves the call: "ret" or ("out", arg index))
# Library functions only, as in ChkUp; MCUboot's own freshness/compatibility functions are
# the "proprietary" part of the corpus (ChkUp builds that part by reverse engineering).
CORPUS = {
    # integrity: digest computation (the digest is written to an output buffer)
    "tc_sha256_final": ("integrity", True, ("out", 0)),
    "mbedtls_sha256_finish": ("integrity", True, ("out", 1)),
    "mbedtls_sha512_finish": ("integrity", True, ("out", 1)),
    "psa_hash_finish": ("integrity", True, ("out", 1)),
    "psa_hash_compute": ("integrity", True, ("out", 3)),
    "mbedtls_md5_finish": ("integrity", False, ("out", 1)),
    "mbedtls_sha1_finish": ("integrity", False, ("out", 1)),
    "crc32_ieee": ("integrity", False, "ret"),
    "crc32_ieee_update": ("integrity", False, "ret"),
    "crc16_ccitt": ("integrity", False, "ret"),
    # authenticity: asymmetric signature verification = proper; MAC only = improper
    "mcuboot_mldsa_verify": ("authenticity", True, "ret"),
    "mbedtls_rsa_public": ("authenticity", True, "ret"),
    "mbedtls_rsa_rsassa_pss_verify": ("authenticity", True, "ret"),
    "mbedtls_pk_verify": ("authenticity", True, "ret"),
    "psa_verify_hash": ("authenticity", True, "ret"),
    "psa_verify_message": ("authenticity", True, "ret"),
    "uECC_verify": ("authenticity", True, "ret"),
    "ED25519_verify": ("authenticity", True, "ret"),
    "tc_hmac_final": ("authenticity", False, ("out", 0)),
    "tc_cmac_final": ("authenticity", False, ("out", 0)),
    "mbedtls_md_hmac_finish": ("authenticity", False, ("out", 1)),
    "mbedtls_cipher_cmac_finish": ("authenticity", False, ("out", 1)),
    "psa_mac_verify_finish": ("authenticity", False, "ret"),
    # freshness (MCUboot-specific): version / security counter comparison
    "boot_compare_version": ("freshness", True, "ret"),
    "bootutil_get_img_security_cnt": ("freshness", True, ("out", 3)),
    "boot_nv_security_counter_get": ("freshness", True, "ret"),
    # compatibility (MCUboot-specific): inter-image dependency TLV
    "boot_verify_slot_dependencies": ("compatibility", True, "ret"),
}
PROPERTIES = ["authenticity", "integrity", "freshness", "compatibility"]

# ---------------------------------------------------------------- GIMPLE parsing
FUNC_HDR = re.compile(r"^;; Function (\S+) \((\S+), funcdef_no")
LOC = re.compile(r"\[[^\[\]]*?:(\d+):\d+(?: discrim \d+)?\] ?")
SSA = re.compile(r"(?<![\w.])((?:[A-Za-z_][\w.]*?)?_\d+)(\(D\))?(?![\w.])")
SSA_DECL = re.compile(r"^_|_\d+$")  # GIMPLE temporaries are declared too; they are not memory
ADDR = re.compile(r"&(\w+)\b")
DEREF = re.compile(r"(?:\*|MEM\[\([^)]*\)|MEM <[^>]*> \[\([^)]*\))((?:[A-Za-z_][\w.]*?)?_\d+)")
ARROW = re.compile(r"((?:[A-Za-z_][\w.]*?)?_\d+)(?:\(D\))?->")
CALL = re.compile(r"^(?:(.+?) = )?([A-Za-z_][\w.]*) \((.*)\);$")
DECL = re.compile(r"^  (?!#)[^=;()]*?[\s*](\w+)(?:\[\d+\])*;$")


CLONE = re.compile(r"\.(isra|part|constprop|cold|lto_priv)(\.\d+)?")


def canon(name):
    """Clone names: definitions print foo.isra.0, call sites print foo.isra."""
    return CLONE.sub("", name)


def split_args(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "([<":
            depth += 1
        elif ch in ")]>":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


class Func:
    def __init__(self, name, path):
        self.name, self.path = name, path
        self.params, self.locals, self.stmts = [], set(), []  # stmts: (line, kind, data)
        self.consts = {}  # parameters fixed by IPA constant propagation (# DEBUG p => 1)


def parse_gimple(path):
    funcs, f, in_body, seen_bb, sig_next = [], None, False, False, False
    for raw in open(path, encoding="utf-8", errors="replace"):
        raw = raw.rstrip("\n")
        m = FUNC_HDR.match(raw)
        if m:
            f = Func(m.group(2), path)
            funcs.append(f)
            in_body, seen_bb, sig_next = False, False, True
            continue
        if f is None:
            continue
        if sig_next and raw and not raw.startswith(";;") and "(" in raw:
            inner = raw[raw.index("(") + 1: raw.rindex(")")]
            if inner.strip() not in ("", "void"):
                f.params = [re.sub(r"[\s*]+", " ", a).split(" ")[-1] for a in split_args(inner)]
            sig_next = False
            continue
        if raw == "{":
            in_body = True
            continue
        if raw == "}":
            in_body = False
            continue
        if not in_body:
            continue
        if raw.lstrip().startswith("<bb "):
            seen_bb = True
            continue
        mline = LOC.search(raw)
        line = int(mline.group(1)) if mline else 0
        s = LOC.sub("", raw).strip()
        if not seen_bb:
            d = DECL.match("  " + s) if s.endswith(";") else None
            if d and not SSA_DECL.search(d.group(1)):
                f.locals.add(d.group(1))
            continue
        s = re.sub(r"\s*\[tail call\]$", "", s)
        dc = re.match(r"# DEBUG (\w+) => (-?\d+)$", s)
        if dc and dc.group(1) not in f.consts:  # first binding (clones drop the parameter itself)
            f.consts[dc.group(1)] = dc.group(2)
        if (not s or s.startswith("# DEBUG") or s.startswith("__asm__") or "CLOBBER" in s
                or s.startswith("goto") or s == "else" or s.startswith("<")):
            continue
        if s.startswith("# ") and " = PHI <" in s:
            lhs, rhs = s[2:].split(" = PHI <", 1)
            f.stmts.append((line, "phi", (lhs.strip(), rhs)))
        elif s.startswith("if ("):
            f.stmts.append((line, "cond", s))
        elif s.startswith("switch ("):
            f.stmts.append((line, "cond", s.split(")")[0] + ")"))
        elif s.startswith("return"):
            f.stmts.append((line, "ret", s[6:].rstrip(";").strip()))
        else:
            m = CALL.match(s)
            if m:
                f.stmts.append((line, "call", (m.group(1), m.group(2), split_args(m.group(3)))))
            elif " = " in s:
                lhs, rhs = s.rstrip(";").split(" = ", 1)
                f.stmts.append((line, "assign", (lhs.strip(), rhs)))
    return funcs


def load_gimple(build_dir):
    funcs = {}
    for root, _, files in os.walk(build_dir):
        for fn in files:
            if fn.endswith(".optimized") and "/bootloader/mcuboot/" in os.path.join(root, fn):
                for f in parse_gimple(os.path.join(root, fn)):
                    funcs[(f.path, f.name)] = f
    # static functions from headers (e.g. bootutil_sha_finish) get one copy per TU;
    # a copy is only called from its own TU
    count = defaultdict(int)
    for f in funcs.values():
        count[canon(f.name)] += 1
    for f in funcs.values():
        f.multi = count[canon(f.name)] > 1
    return funcs


# ---------------------------------------------------------------- value-to-condition tracing
def ssa_names(text):
    return {m.group(1) for m in SSA.finditer(text)}


def roots_read(text, f):
    r = {"&" + a for a in ADDR.findall(text) if a in f.locals}
    r |= {"*" + p for p in DEREF.findall(text)} | {"*" + p for p in ARROW.findall(text)}
    r |= {v for v in f.locals if re.search(rf"(?<![\w.&]){re.escape(v)}(?![\w.(])", text)}
    return {x if not x.startswith("&") else x[1:] for x in r}


def store_root(lhs, f):
    """Memory location written by 'lhs = ...' (None if lhs is an SSA name)."""
    if SSA.fullmatch(lhs):
        return None
    m = DEREF.search(lhs) or ARROW.search(lhs)
    if m:
        return "*" + m.group(1)
    a = ADDR.search(lhs)
    if a:
        return a.group(1)
    w = re.match(r"(\w+)", lhs)
    return w.group(1) if w and w.group(1) in f.locals else None


def arg_root(arg, f):
    """Seed for an output argument: '&buf' -> buf, 'p_3(D)' -> *p_3."""
    a = ADDR.match(arg.strip())
    if a:
        return a.group(1)
    s = SSA.search(arg)
    return "*" + s.group(1) if s else None


def param_index(f, ssa):
    base = re.sub(r"_\d+$", "", ssa)
    return f.params.index(base) if base in f.params else None


def trace(f, seed_ssa, seed_roots, writer=None):
    """Flow-insensitive fixpoint over one function. Returns conds, ret, out params.
    writer: (line, callee) of the call that fills a seeded buffer; its own return value says
    nothing about the buffer contents, so it is not tainted by it."""
    T, R = set(seed_ssa), set(seed_roots)
    conds, ret_data, outp = [], False, set()
    changed = True
    while changed:
        changed = False
        for line, kind, d in f.stmts:
            if kind == "phi":
                lhs, rhs = d
                if lhs not in T and ssa_names(rhs) & T:
                    T.add(lhs)
                    changed = True
            elif kind == "assign":
                lhs, rhs = d
                if ssa_names(rhs) & T or roots_read(rhs, f) & R:
                    r = store_root(lhs, f)
                    tgt = (r, R) if r else (lhs, T)
                    if tgt[0] and tgt[0] not in tgt[1]:
                        tgt[1].add(tgt[0])
                        changed = True
            elif kind == "call":
                lhs, callee, args = d
                if writer and (line, canon(callee)) == writer:
                    continue
                hit = any(ssa_names(a) & T or roots_read(a, f) & R for a in args)
                if hit and lhs:
                    r = store_root(lhs, f)
                    tgt = (r, R) if r else (lhs, T)
                    if tgt[0] and tgt[0] not in tgt[1]:
                        tgt[1].add(tgt[0])
                        changed = True
    for line, kind, d in f.stmts:
        if kind == "cond" and (ssa_names(d) & T or roots_read(d, f) & R):
            conds.append((line, d))
        elif kind == "ret" and d and (ssa_names(d) & T or roots_read(d, f) & R):
            ret_data = True
    for r in R:
        if r.startswith("*"):
            i = param_index(f, r[1:])
            if i is not None:
                outp.add(i)
    return conds, ret_data, outp


def callers_index(funcs):
    idx = defaultdict(list)
    for f in funcs.values():
        for line, kind, d in f.stmts:
            if kind == "call":
                idx[canon(d[1])].append((f, line, d[0], d[2]))
    return idx


def follow(funcs, callers, start_f, seed_ssa, seed_roots, stop, max_depth=10, allowed=None, writer=None):
    """Trace from a key call site upward. A function whose own condition depends on the value
    hands a control-dependent verdict to its callers through its return value."""
    hops, first_cond, seen = [], None, set()
    work = [(start_f, frozenset(seed_ssa), frozenset(seed_roots), 0, "data", writer)]
    while work:
        f, ss, rr, depth, how, wr = work.pop(0)
        key = (f.name, ss, rr)
        if key in seen or depth > max_depth:
            continue
        seen.add(key)
        conds, ret_data, outp = trace(f, ss, rr, wr)
        hops.append({"func": canon(f.name), "depth": depth, "via": how,
                     "conds": [f"{line}: {c}" for line, c in conds[:4]], "ret": ret_data,
                     "out_params": sorted(outp)})
        if conds and first_cond is None:
            first_cond = (canon(f.name), conds[0][0], conds[0][1])
        if canon(f.name) in stop:
            continue
        ret_any = ret_data or bool(conds)
        for cf, line, lhs, args in callers.get(canon(f.name), []):
            if allowed is not None and canon(cf.name) not in allowed:
                continue
            if f.multi and cf.path != f.path:
                continue
            s2, r2 = set(), set()
            wr2 = (line, canon(f.name)) if outp and not (ret_any and lhs) else None
            if ret_any and lhs:
                (s2 if SSA.fullmatch(lhs) else r2).add(lhs if SSA.fullmatch(lhs) else store_root(lhs, cf))
            for i in outp:
                if i < len(args) and arg_root(args[i], cf):
                    r2.add(arg_root(args[i], cf))
            r2.discard(None)
            if s2 or r2:
                work.append((cf, frozenset(s2), frozenset(r2), depth + 1,
                             "ret" if ret_data else ("ctrl" if conds else "out"), wr2))
    return first_cond, hops


# ---------------------------------------------------------------- main analysis
def tlv_constants(mcuboot):
    consts = {}
    for line in open(os.path.join(mcuboot, "boot/bootutil/include/bootutil/image.h")):
        m = re.match(r"#define (IMAGE_TLV_\w+)\s+(0x[0-9a-fA-F]+)", line)
        if m:
            consts[int(m.group(2), 16)] = m.group(1)
    return consts


def kconfig(build_dir, names):
    vals = {}
    for line in open(os.path.join(build_dir, "zephyr/.config")):
        for n in names:
            if line.startswith(f"CONFIG_{n}="):
                vals[n] = line.split("=", 1)[1].strip()
    return {n: vals.get(n, "n") for n in names}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir")
    ap.add_argument("--out", required=True)
    ap.add_argument("--entry", default="main")
    ap.add_argument("--mcuboot", default=os.path.expanduser("~/secureboot/bootloader/mcuboot"))
    a = ap.parse_args()

    # step 1: functions on the update/boot path
    defs, edges, _ = cg.load(a.build_dir)
    _, chains = cg.walk(a.entry, defs, edges)
    on_path = {name for name, cat, _, _ in chains if cat == "mcuboot"}
    chain_of = {name: chain for name, _, _, chain in chains}

    funcs = load_gimple(a.build_dir)
    callers = callers_index(funcs)
    stop = {a.entry}

    # step 2: key calls on the path, traced to conditions
    procs = []
    for f in funcs.values():
        fname = canon(f.name)
        if fname not in on_path:
            continue
        for line, kind, d in f.stmts:
            if kind != "call" or d[1] not in CORPUS:
                continue
            lhs, callee, args = d
            prop, proper, how = CORPUS[callee]
            seed_s, seed_r = set(), set()
            if how == "ret" and lhs:
                (seed_s.add(lhs) if SSA.fullmatch(lhs) else seed_r.add(store_root(lhs, f)))
            elif how != "ret" and how[1] < len(args) and arg_root(args[how[1]], f):
                seed_r.add(arg_root(args[how[1]], f))
            seed_r.discard(None)
            first, hops = follow(funcs, callers, f, seed_s, seed_r, stop, allowed=on_path,
                                 writer=(line, callee) if how != "ret" else None)
            top = max(hops, key=lambda h: h["depth"])["func"] if hops else fname
            procs.append({"property": prop, "key_function": callee, "proper": proper,
                          "caller": fname, "line": line, "chain": chain_of.get(fname, ""),
                          "reaches_condition": first is not None,
                          "first_condition": f"{first[0]}:{first[1]}: {first[2]}" if first else "",
                          "decision_reaches": top, "hops": hops})

    # P5: TLV reads (type, protected-only flag) and the allow-list check
    tlv_names = tlv_constants(a.mcuboot)
    tlv_reads = []
    for f in funcs.values():
        fname = canon(f.name)
        if fname not in on_path:
            continue
        for line, kind, d in f.stmts:
            if kind == "call" and d[1] == "bootutil_tlv_iter_begin" and len(d[2]) >= 5:
                t, p = d[2][3], d[2][4]
                t_name = tlv_names.get(int(t), t) if t.isdigit() else t
                tlv_reads.append({"func": fname, "line": line, "type": t_name,
                                  "protected_only": p == "1" if p in ("0", "1") else p})
    is_prot = []
    for f in funcs.values():
        fname = canon(f.name)
        if fname not in on_path:
            continue
        for line, kind, d in f.stmts:
            if kind == "call" and d[1] == "bootutil_tlv_iter_is_prot" and d[0]:
                first, _ = follow(funcs, callers, f, {d[0]}, set(), stop, max_depth=0)
                is_prot.append({"func": fname, "line": line, "checked": first is not None})

    # step 3: verdicts
    kc = kconfig(a.build_dir, ["BOOT_VALIDATE_SLOT0", "MCUBOOT_DOWNGRADE_PREVENTION",
                               "MCUBOOT_DOWNGRADE_PREVENTION_SECURITY_COUNTER",
                               "MCUBOOT_HW_DOWNGRADE_PREVENTION", "MCUBOOT_USE_TLV_ALLOW_LIST",
                               "BOOT_SWAP_USING_SCRATCH", "BOOT_UPGRADE_ONLY"])
    verdict = {}
    for prop in PROPERTIES:
        ps = [p for p in procs if p["property"] == prop]
        checked = [p for p in ps if p["reaches_condition"]]
        if not checked:
            v = "missing" if not ps else "missing (computed but never checked)"
        elif any(not p["proper"] for p in checked) and not any(p["proper"] for p in checked):
            v = "improper"
        else:
            v = "ok"
        verdict[prop] = {"verdict": v, "procedures": sorted({f"{p['caller']} -> {p['key_function']}"
                                                             for p in checked})}
    # Which slots go through image validation (boot_validate_slot(state, slot, bs)):
    # slot 1 = upgrade candidate, slot 0 = running image re-checked on every boot
    # (IPA-SRA clones drop parameters, so take the integer literal argument, not a position)
    # (.constprop clones carry the slot as a "# DEBUG slot => N" binding instead of an argument)
    vs_const = next((f.consts["slot"] for f in funcs.values() if canon(f.name) == "boot_validate_slot"
                     and ".constprop" in f.name and "slot" in f.consts), "?")
    validated = sorted({next((x for x in d[2] if x.isdigit()), vs_const)
                        for f in funcs.values() if canon(f.name) in on_path
                        for line, kind, d in f.stmts
                        if kind == "call" and canon(d[1]) == "boot_validate_slot"})
    for prop in ("authenticity", "integrity"):
        verdict[prop]["validated_slots"] = validated
        if verdict[prop]["verdict"] == "ok" and "0" not in validated:
            verdict[prop]["verdict"] = "partial (upgrade only; primary slot not re-validated at boot)"
    # P5: every type-specific read must be protected-only; ANY reads need the is_prot check
    bad = [t for t in tlv_reads if t["type"] != "IMAGE_TLV_ANY" and t["protected_only"] is not True
           and t["type"] not in ("IMAGE_TLV_SIG_PURE",) and not t["type"].startswith("IMAGE_TLV_ENC")]
    any_reads = [t for t in tlv_reads if t["type"] == "IMAGE_TLV_ANY" and t["protected_only"] is not True]
    any_guarded = {i["func"] for i in is_prot if i["checked"]}
    unguarded = [t for t in any_reads if t["func"] not in any_guarded]
    verdict["P5_unsigned_field_use"] = {
        "verdict": "ok" if not bad and not unguarded else "improper (unprotected TLVs not restricted)",
        "type_reads_not_protected": bad, "any_reads_without_allow_list": unguarded}
    # P6: freshness value source
    fr = [p for p in procs if p["property"] == "freshness" and p["reaches_condition"]]
    srcs = []
    for p in fr:
        if p["key_function"] == "boot_compare_version":
            srcs.append("image header ih_ver (covered by the image hash -> signed)")
        elif p["key_function"] == "bootutil_get_img_security_cnt":
            prot = [t for t in tlv_reads if t["type"] == "IMAGE_TLV_SEC_CNT"]
            srcs.append("SEC_CNT TLV, protected area only" if prot and all(t["protected_only"] is True for t in prot)
                        else "SEC_CNT TLV, NOT restricted to the protected area")
        else:
            srcs.append(p["key_function"])
    verdict["P6_rollback_value_protection"] = {
        "verdict": "n/a (no freshness check)" if not fr else
        ("ok" if all("NOT" not in s for s in srcs) else "vulnerable"), "sources": sorted(set(srcs))}

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "procedures.tsv"), "w") as fo:
        fo.write("property\tkey_function\tproper\tcaller\tline\treaches_condition\tfirst_condition\tdecision_reaches\tchain\n")
        for p in sorted(procs, key=lambda p: (p["property"], p["caller"], p["line"])):
            fo.write("\t".join(str(p[k]) for k in ["property", "key_function", "proper", "caller", "line",
                                                    "reaches_condition", "first_condition",
                                                    "decision_reaches", "chain"]) + "\n")
    with open(os.path.join(a.out, "tlv_reads.tsv"), "w") as fo:
        fo.write("func\tline\ttype\tprotected_only\n")
        for t in tlv_reads:
            fo.write(f"{t['func']}\t{t['line']}\t{t['type']}\t{t['protected_only']}\n")
    json.dump({"kconfig": kc, "verdict": verdict, "procedures": procs, "tlv_reads": tlv_reads,
               "is_prot_checks": is_prot}, open(os.path.join(a.out, "verdict.json"), "w"), indent=1)

    lines = [f"# ChkUp verdict — {os.path.basename(os.path.normpath(a.build_dir))}", "",
             "Kconfig: " + ", ".join(f"{k}={v}" for k, v in kc.items()), "",
             "| property | verdict | verification procedures (caller -> key function) |", "|---|---|---|"]
    for k, v in verdict.items():
        extra = v.get("procedures") or v.get("sources") or \
            [f"{t['func']}:{t['line']} {t['type']}" for t in v.get("type_reads_not_protected", []) +
             v.get("any_reads_without_allow_list", [])]
        lines.append(f"| {k} | {v['verdict']} | {'; '.join(extra) if extra else '-'} |")
    lines += ["", "## Key calls on the path", "",
              "| property | key function | caller:line | reaches condition | first condition | decision reaches |",
              "|---|---|---|---|---|---|"]
    for p in sorted(procs, key=lambda p: (p["property"], p["caller"], p["line"])):
        lines.append(f"| {p['property']} | {p['key_function']}{'' if p['proper'] else ' (improper)'} | "
                     f"{p['caller']}:{p['line']} | {p['reaches_condition']} | `{p['first_condition']}` | "
                     f"{p['decision_reaches']} |")
    lines += ["", "## TLV reads on the path (P5)", "", "| func:line | type | protected only |", "|---|---|---|"]
    lines += [f"| {t['func']}:{t['line']} | {t['type']} | {t['protected_only']} |" for t in tlv_reads]
    lines += ["", "allow-list check (bootutil_tlv_iter_is_prot -> condition): " +
              (", ".join(f"{i['func']}:{i['line']}={i['checked']}" for i in is_prot) or "none on path")]
    open(os.path.join(a.out, "verdict.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines[:6 + len(verdict)]))


if __name__ == "__main__":
    main()
