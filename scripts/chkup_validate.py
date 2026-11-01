#!/usr/bin/env python3
"""ChkUp step 4: validate static alerts on the board with PoC images (ChkUp 4.4, Table 2).

For every alert in verdict.json (scripts/chkup_analyze.py) the PoCs mapped to its
(property, kind) are flashed and the board is reset. ChkUp's rule decides: if the update
still goes through (the attacker's image runs), the alert is a true positive; if MCUboot
rejects it, a false positive. With --negative the same PoCs are also run for properties
without an alert: attack succeeds -> false negative, rejected -> true negative.
A legitimate upgrade runs first; if it fails the test environment is broken and nothing
else is judged.

usage: scripts/chkup_validate.py <conf> <boot build name> <verdict.json> <outdir> [--negative]
  e.g. mldsa65 mldsa65_chkup_dgp results/x/static/mldsa65_chkup_dgp/verdict.json results/x/poc/...
needs: build/boot_<boot build name>, build/hello_v1, build/hello_v2, build/hello_nucleo,
       keys/<KEY>.pem, serial port free, ST-Link attached to WSL
output: <outdir>/validation.csv, validation.md, logs/, images/ (+ info.txt)
"""
import argparse
import csv
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
WS = os.path.dirname(EXP)
BUILD = os.path.join(WS, "build")
IMGTOOL = os.path.join(WS, "bootloader/mcuboot/scripts/imgtool.py")
HDR_SIZE, SLOT_SIZE = "0x200", "0xc0000"
SLOT0, SLOT1 = "0x08020000", "0x08120000"
OCD = ["openocd", "-f", "interface/stlink.cfg", "-f", "target/stm32f4x.cfg"]

# ---------------------------------------------------------------- PoC table (ChkUp Table 2)
# slot0/slot1: image names built in make_images(); success: what runs if the attack works
#   v1 / v2: that application; v2-tampered / v1-tampered: modified payload runs;
#   accepted: slot1 taken and jumped to, application without console (other board)
POCS = {
    "auth_unsigned": ("unsigned image (hash TLV only)", "v1_sc1", "up_v2_unsigned", "v2"),
    "auth_wrongkey": ("signed with another key of the same type", "v1_sc1", "up_v2_wrongkey", "v2"),
    "integ_modified": ("payload modified, nothing else", "v1_sc1", "up_v2_mod", "v2-tampered"),
    "integ_rehash": ("payload modified + SHA256 TLV replaced", "v1_sc1", "up_v2_rehash", "v2-tampered"),
    "slot0_tamper": ("running image (slot0) modified, no upgrade", "v1_tampered", None, "v1-tampered"),
    "fresh_older": ("older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1)", "v2_sc5", "up_v1_sc1", "v1"),
    "fresh_setver": ("older image, header version raised to 3.0.0 (not re-signed)", "v2_sc5", "up_v1_setver", "v1"),
    "comp_otherboard": ("image built for another board, signed with the same key", "v1_sc1", "up_other", "accepted"),
    "p5_inject": ("TLV injected in the unprotected area", "v1_sc1", "up_v2_inject", "v2"),
    "p6_equal_counter": ("older image with the same security counter (5 -> 5)", "v2_sc5", "up_v1_sc5", "v1"),
    "p6_unprot_counter": ("older image cnt1 + SEC_CNT=10 in the unprotected area", "v2_sc5", "up_v1_sc1_inject", "v1"),
}
BASELINE = ("legitimate upgrade v1/cnt1 -> v2/cnt5", "v1_sc1", "up_v2_sc5", "v2")
ALERT_POCS = {
    ("authenticity", "missing"): ["auth_unsigned"],
    ("authenticity", "improper"): ["auth_wrongkey"],
    ("authenticity", "partial"): ["slot0_tamper"],
    ("integrity", "missing"): ["integ_modified"],
    ("integrity", "improper"): ["integ_rehash"],
    ("integrity", "partial"): ["slot0_tamper"],
    ("freshness", "missing"): ["fresh_older"],
    ("freshness", "improper"): ["fresh_setver"],
    ("compatibility", "missing"): ["comp_otherboard"],
    ("P5", "improper"): ["p5_inject"],
    ("P6", "improper"): ["p6_equal_counter", "p6_unprot_counter"],
}
# an alert whose detail names the flaw gets only the PoC for that flaw; the property's
# other PoCs then run as negative checks
DETAIL_POCS = [
    ("P6", "equal security counter", ["p6_equal_counter"]),
    ("P6", "unprotected", ["p6_unprot_counter"]),
]


def alert_pocs(al):
    for prop, key, pocs in DETAIL_POCS:
        if al["property"] == prop and key in al.get("detail", ""):
            return pocs
    return ALERT_POCS.get((al["property"], al["kind"]), [])
# negative checks: properties without an alert get every PoC of that property
PROPERTY_POCS = {
    "authenticity": ["auth_unsigned", "auth_wrongkey", "slot0_tamper"],
    "integrity": ["integ_modified", "integ_rehash"],
    "freshness": ["fresh_older", "fresh_setver"],
    "compatibility": ["comp_otherboard"],
    "P5": ["p5_inject"],
    "P6": ["p6_equal_counter", "p6_unprot_counter"],
}


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def conf_get(conf, key):
    for line in open(os.path.join(EXP, "boot_conf", f"{conf}.conf")):
        if line.startswith(f"# {key}="):
            return line.split("=", 1)[1].strip()
    return ""


def make_images(conf, d):
    key = conf_get(conf, "KEY")
    extra = conf_get(conf, "SIGN").split()
    k = ["-k", os.path.join(EXP, "keys", f"{key}.pem")]
    up = ["--pad", "--confirm"]
    tool = [sys.executable, os.path.join(HERE, "chkup_images.py")]

    def sign(app, out, ver, *args):
        run([sys.executable, IMGTOOL, "sign", *extra, "--header-size", HDR_SIZE, "--align", "1",
             "--slot-size", SLOT_SIZE, "--version", ver, *args,
             os.path.join(BUILD, app, "zephyr/zephyr.bin"), os.path.join(d, out + ".bin")])

    p = lambda n: os.path.join(d, n + ".bin")  # noqa: E731
    sign("hello_v1", "v1_sc1", "1.0.0", *k, "-s", "1")
    sign("hello_v2", "v2_sc5", "2.0.0", *k, "-s", "5")
    sign("hello_v2", "up_v2_sc5", "2.0.0", *k, "-s", "5", *up)
    sign("hello_v1", "up_v1_sc1", "1.0.0", *k, "-s", "1", *up)
    sign("hello_v1", "up_v1_sc5", "1.0.0", *k, "-s", "5", *up)
    sign("hello_v2", "up_v2_unsigned", "2.0.0", "-s", "5", *up)
    with tempfile.TemporaryDirectory() as t:
        other = os.path.join(t, "other.pem")
        run([sys.executable, IMGTOOL, "keygen", "-k", other, "-t", key_type(key)])
        sign("hello_v2", "up_v2_wrongkey", "2.0.0", "-k", other, "-s", "5", *up)
    sign("hello_nucleo", "up_other", "2.0.0", *k, "-s", "5", *up)
    run(tool + ["replace", p("up_v2_sc5"), p("up_v2_mod"), "Hello World", "Hello Wor1d"])
    rehash(p("up_v2_mod"), p("up_v2_rehash"))
    run(tool + ["replace", p("v1_sc1"), p("v1_tampered"), "Hello World", "Hello Wor1d"])
    run(tool + ["setver", p("up_v1_sc1"), p("up_v1_setver"), "3.0.0"])
    run(tool + ["inject", p("up_v2_sc5"), p("up_v2_inject"), "0x50", "0a000000"])
    run(tool + ["inject", p("up_v1_sc1"), p("up_v1_sc1_inject"), "0x50", "0a000000"])
    with open(os.path.join(d, "info.txt"), "w") as fo:
        for f in sorted(os.listdir(d)):
            if f.endswith(".bin"):
                fo.write(f"== {f}\n" + run(tool + ["info", os.path.join(d, f)]).stdout)


def rehash(src, dst):
    """Recompute the SHA256 TLV of an already modified image (the signature stays stale)."""
    import hashlib
    sys.path.insert(0, HERE)
    import chkup_images
    data = bytearray(open(src, "rb").read())
    info = chkup_images.parse(data)
    sha = next(t for t in info["tlvs"] if t["type"] == chkup_images.TLV_SHA256)
    data[sha["off"]:sha["off"] + 32] = hashlib.sha256(data[:info["hashed_end"]]).digest()
    open(dst, "wb").write(data)


def key_type(key):
    m = re.match(r"mldsa(\d+)$", key)
    if m:
        return f"ml-dsa-{m.group(1)}"
    return {"rsa2048": "rsa-2048", "rsa3072": "rsa-3072", "ecdsa_p256": "ecdsa-p256",
            "ed25519": "ed25519"}[key]


# ---------------------------------------------------------------- board
def flash_case(boot, s0, s1, log):
    with open(log, "w") as fo:
        def step(cmd):
            r = subprocess.run(cmd, stdout=fo, stderr=subprocess.STDOUT, cwd=WS)
            if r.returncode:
                raise RuntimeError(f"failed: {' '.join(cmd)}")
        step([os.path.join(HERE, "flash.sh"), "erase"])
        step([os.path.join(HERE, "flash.sh"), "boot", boot])
        step([os.path.join(HERE, "flash.sh"), "slot0", s0])
        if s1:  # core left halted so the capture sees MCUboot process slot1
            step(OCD + ["-c", f"init; reset halt; program {s1} {SLOT1} verify; shutdown"])


def observe(log):
    text = open(log, errors="replace").read()
    m = re.search(r"\[(v\d|other)\] Hello Wor([l1])d", text)
    app = None if not m else m.group(1) + ("-tampered" if m.group(2) == "1" else "")
    marks = [n for n, pat in [("swap", "Starting swap"), ("rejected", "slot is not valid"),
                              ("downgrade-erased", "downgrade prevention"),
                              ("no-bootable", "Unable to find bootable image"), ("jump", "Jumping to")]
             if pat in text]
    if app is None and "jump" in marks and not {"rejected", "downgrade-erased"} & set(marks):
        app = "accepted"
    return app or "none", marks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("conf")
    ap.add_argument("boot")
    ap.add_argument("verdict")
    ap.add_argument("out")
    ap.add_argument("--negative", action="store_true")
    a = ap.parse_args()
    out = a.out if os.path.isabs(a.out) else os.path.join(WS, a.out)
    if os.path.exists(out):
        sys.exit(f"{out} already exists; pick a new directory")
    img, logs = os.path.join(out, "images"), os.path.join(out, "logs")
    os.makedirs(img)
    os.makedirs(logs)
    v = json.load(open(a.verdict))
    make_images(a.conf, img)

    plan = []  # (case id, poc, property, alert kind or None)
    for al in v["alerts"]:
        for poc in alert_pocs(al):  # every alert keeps its own run, even if the PoC repeats
            plan.append((poc, al["property"], al["kind"]))
    if a.negative:
        has_fresh = not v["verdict"]["freshness"]["verdict"].startswith("missing")
        for prop, pocs in PROPERTY_POCS.items():
            if prop == "P6" and not has_fresh:
                continue
            plan += [(poc, prop, None) for poc in pocs if poc not in [p[0] for p in plan]]

    rows = []

    def case(cid, desc, s0, s1, success, prop, kind):
        flog, blog = os.path.join(logs, f"{cid}.flash.log"), os.path.join(logs, f"{cid}.log")
        flash_case(a.boot, os.path.join(img, s0 + ".bin"), s1 and os.path.join(img, s1 + ".bin"), flog)
        subprocess.run([sys.executable, os.path.join(HERE, "capture_boot.py"), "--seconds", "25",
                        "--log", blog], check=True, capture_output=True, cwd=WS)
        got, marks = observe(blog)
        attack = got == success
        if kind is None and prop == "baseline":
            res = "ok" if attack else "ENV-FAIL"
        elif kind:
            res = "TP" if attack else "FP"
        else:
            res = "FN" if attack else "TN"
        row = {"case": cid, "property": prop, "alert": kind or "-", "poc": desc, "attack_succeeds_if": success,
               "observed": got, "attack_succeeded": attack, "result": res, "markers": ";".join(marks)}
        rows.append(row)
        print(f"{cid:18s} {prop:13s} {kind or '-':9s} expect-if-attack {success:12s} got {got:12s} {res}",
              flush=True)
        return res

    if case("baseline", *BASELINE, "baseline", None) != "ok":
        print("baseline upgrade failed: test environment broken, stopping", file=sys.stderr)
    else:
        done = set()
        for poc, prop, kind in plan:
            cid = poc if poc not in done else f"{poc}_{prop}"
            done.add(poc)
            desc, s0, s1, success = POCS[poc]
            case(cid, desc, s0, s1, success, prop, kind)

    with open(os.path.join(out, "validation.csv"), "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    counts = {r: sum(1 for x in rows if x["result"] == r) for r in ("TP", "FP", "TN", "FN")}
    md = [f"# ChkUp step 4 — boot_{a.boot}", "",
          f"alerts: {len(v['alerts'])} -> TP {counts['TP']}, FP {counts['FP']}; "
          f"negative checks -> TN {counts['TN']}, FN {counts['FN']}", "",
          "| case | property | alert | PoC | attack succeeds if | observed | result | MCUboot log |",
          "|---|---|---|---|---|---|---|---|"]
    md += [f"| {r['case']} | {r['property']} | {r['alert']} | {r['poc']} | {r['attack_succeeds_if']} | "
           f"{r['observed']} | {r['result']} | {r['markers']} |" for r in rows]
    open(os.path.join(out, "validation.md"), "w").write("\n".join(md) + "\n")
    json.dump(counts, open(os.path.join(out, "counts.json"), "w"))
    sys.exit(0 if rows and rows[0]["result"] == "ok" else 1)


if __name__ == "__main__":
    main()
