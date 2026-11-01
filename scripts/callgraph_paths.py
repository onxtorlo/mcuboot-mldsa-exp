#!/usr/bin/env python3
"""ChkUp step 1 (execution path recovery) for MCUboot, from GCC -fcallgraph-info output.

Merges every per-TU .ci file of an analysis build (boot_conf/callgraph.conf) into one
function-level call graph, then walks it from the entry (boot_go) and prints the call tree
in call-site order, which approximates the update/boot execution path up to the jump.

Pruning follows ChkUp's path-explosion rules (Appendix A.1): logging, asserts, libc and
kernel utilities are skipped; crypto and flash APIs are kept as leaves (the call MCUboot
makes into the library is what step 2 matches against the corpus, not library internals).

usage: scripts/callgraph_paths.py <build_dir> [--entry boot_go] [--out <dir>]
output (with --out): callgraph.json (merged graph), tree.txt (pruned call tree),
                     chains.tsv (entry -> function call chains for every kept function)
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict

NODE_RE = re.compile(r'^node: \{ title: "([^"]*)" label: "([^"]*)"(.*)\}$')
EDGE_RE = re.compile(r'^edge: \{ sourcename: "([^"]*)" targetname: "([^"]*)" label: "([^"]*)" \}$')
CLONE_RE = re.compile(r'\.(isra|part|constprop|cold|lto_priv)\.\d+')

# Where a function is defined decides how it is treated in the tree.
CATEGORIES = [  # (category, path substring) - first match wins
    ("crypto", "/bootloader/mcuboot/ext/"),  # bundled TinyCrypt etc.
    ("mcuboot", "/bootloader/mcuboot/"),
    ("crypto", "/tf-psa-crypto/"),
    ("crypto", "/modules/crypto/"),
    ("crypto", "/mbedtls/"),
    ("flash", "/drivers/flash/"),
    ("flash", "/subsys/storage/flash_map/"),
]
SKIP_NAME = re.compile(
    r'^(z_log|log_|__assert|assert|printk|z_impl_|k_|z_|sys_|arch_|mem(set|cpy|cmp|move)$|'
    r'str(n?len|n?cmp|n?cpy)$|__aeabi|cbprintf|__stack_chk)'
)


def short(name):
    """'/abs/path/file.c:func.isra.0' -> 'func' (static funcs carry their file as prefix)."""
    base = name.rsplit(":", 1)[-1] if ":" in name else name
    return CLONE_RE.sub("", base)


def canon(title):
    """Merge GCC clones (.isra/.part/...) into the source-level function."""
    return CLONE_RE.sub("", title)


def load(build_dir):
    defs = {}   # canon title -> definition location "file:line"
    edges = defaultdict(list)  # canon src -> [(canon dst, callsite)]
    n_files = 0
    for root, _, files in os.walk(build_dir):
        for fn in files:
            if not fn.endswith(".ci"):
                continue
            n_files += 1
            with open(os.path.join(root, fn), encoding="utf-8", errors="replace") as f:
                for line in f:
                    line = line.rstrip("\n")
                    m = NODE_RE.match(line)
                    if m:
                        title, label, rest = m.groups()
                        if "shape" not in rest:  # defined in this TU (ellipse = external decl)
                            loc = label.split("\\n", 1)[-1].rsplit(":", 1)[0]
                            defs[canon(title)] = loc
                        continue
                    m = EDGE_RE.match(line)
                    if m:
                        src, dst, site = m.groups()
                        edges[canon(src)].append((canon(dst), site))
    for k in edges:  # keep call-site order inside each caller, drop exact duplicates
        seen, uniq = set(), []
        for dst, site in sorted(edges[k], key=lambda e: site_key(e[1])):
            if (dst, site) not in seen:
                seen.add((dst, site))
                uniq.append((dst, site))
        edges[k] = uniq
    return defs, edges, n_files


def site_key(site):
    m = re.match(r'(.*):(\d+):(\d+)$', site)
    return (m.group(1), int(m.group(2)), int(m.group(3))) if m else (site, 0, 0)


def category(title, defs):
    if title == "__indirect_call":
        return "indirect"
    loc = defs.get(title)
    if loc is None:
        return "undefined"
    if SKIP_NAME.match(short(title)):
        return "skip"
    for cat, sub in CATEGORIES:
        if sub in loc:
            return cat
    return "skip"


def rel(path):
    for marker in ("/bootloader/mcuboot/", "/modules/", "/zephyr/"):
        if marker in path:
            return path.split(marker, 1)[1]
    return path


def walk(entry, defs, edges):
    """DFS in call-site order. Each function is expanded once; later visits are references."""
    lines, chains, expanded = [], [], set()

    def rec(fn, depth, chain, site):
        cat = category(fn, defs)
        tag = {"mcuboot": "", "crypto": " [crypto]", "flash": " [flash]",
               "indirect": " [indirect call]", "undefined": " [no definition in build]"}.get(cat, "")
        where = f"  @{rel(site)}" if site else ""
        name = short(fn)
        if fn in chain:
            lines.append(f"{'  ' * depth}{name}{tag} (recursion){where}")
            return
        if fn in expanded and edges.get(fn):
            lines.append(f"{'  ' * depth}{name}{tag} (see above){where}")
            return
        lines.append(f"{'  ' * depth}{name}{tag}{where}")
        chains.append((name, cat, rel(defs.get(fn, "")), " -> ".join(short(c) for c in chain + [fn])))
        expanded.add(fn)
        if cat in ("flash", "crypto"):  # library boundary: keep the API call, not its internals
            return
        for dst, s in edges.get(fn, []):
            if category(dst, defs) in ("skip",):
                continue
            rec(dst, depth + 1, chain + [fn], s)

    rec(entry, 0, [], None)
    return lines, chains


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir")
    ap.add_argument("--entry", default="boot_go")
    ap.add_argument("--out")
    a = ap.parse_args()

    defs, edges, n_files = load(a.build_dir)
    if a.entry not in defs:
        sys.exit(f"entry {a.entry!r} not defined in any .ci under {a.build_dir}")
    lines, chains = walk(a.entry, defs, edges)

    cats = defaultdict(int)
    for _, c, _, _ in chains:
        cats[c] += 1
    summary = (f"# .ci files: {n_files}, defined functions: {len(defs)}, "
               f"call edges: {sum(len(v) for v in edges.values())}\n"
               f"# reachable from {a.entry} after pruning: {len(chains)} "
               + ", ".join(f"{k}={v}" for k, v in sorted(cats.items())))
    print(summary)
    print("\n".join(lines))

    if a.out:
        os.makedirs(a.out, exist_ok=True)
        with open(os.path.join(a.out, "tree.txt"), "w") as f:
            f.write(summary + "\n" + "\n".join(lines) + "\n")
        with open(os.path.join(a.out, "chains.tsv"), "w") as f:
            f.write("function\tcategory\tdefined_at\tchain\n")
            for row in chains:
                f.write("\t".join(row) + "\n")
        with open(os.path.join(a.out, "callgraph.json"), "w") as f:
            json.dump({"defs": defs, "edges": {k: v for k, v in edges.items()}}, f, indent=1)


if __name__ == "__main__":
    main()
