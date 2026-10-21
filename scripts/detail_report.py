#!/usr/bin/env python3
"""Tabulate the "MEASD" lines (steps / primitives inside signature verification).

usage: scripts/detail_report.py <outdir> <measure dir> [<measure dir> ...]
  each <measure dir> is the output of scripts/measure_boot.sh (logs/boot_ok_run*.log)
  writes <outdir>/detail.csv  one row per build, run and item (plus the "sig" stage)
         <outdir>/detail.md   per build: mean cycles per item, % of the "sig" stage;
                              then the "sig" stage of every build (instrumentation cost)

Top-level steps (one dot, e.g. "rsa.public", "psa.verify_hash") together cover the
signature check; "(rest of sig)" is the "sig" stage minus their sum (glue code, FIH,
key lookup inside bootutil_verify_sig). Deeper names are parts of a top-level step;
names of primitives (tc., mpi., ecp., fiat., mld.) are summed over all calls and
nest (e.g. ecp.mul_mod includes mpi.mul_mpi).
"""
import csv
import re
import statistics
import sys
from pathlib import Path

DETAIL = re.compile(r"MEASD (\S+) n=(\d+) sum_cyc=(\d+) sum_us=(\d+)")
STAGE = re.compile(r"MEAS (\w+) n=(\d+) last_cyc=(\d+)")
CLOCK = re.compile(r"MEAS clock_hz=(\d+)")
STEP_PREFIXES = ("ecdsa", "rsa", "psa", "ed25519", "mldsa")


def read_run(path):
    text = path.read_text(errors="replace")
    items = {m[1]: (int(m[2]), int(m[3])) for m in DETAIL.finditer(text)}
    stages = {m[1]: int(m[3]) for m in STAGE.finditer(text)}
    clock = CLOCK.search(text)
    return items, stages, int(clock[1]) if clock else 168000000


def is_top(name):
    return name.count(".") == 1 and name.split(".")[0] in STEP_PREFIXES


def main():
    out = Path(sys.argv[1])
    rows = []
    md = []
    sig_rows = []
    for d in map(Path, sys.argv[2:]):
        build = d.name
        runs = sorted((d / "logs").glob("boot_ok_run*.log"))
        per_item = {}
        sig = []
        mhz = 168.0
        incomplete = []
        for log in runs:
            items, stages, clock = read_run(log)
            if "sig" not in stages:
                incomplete.append(log.name)   # capture ended before the MEAS report
                continue
            mhz = clock / 1e6
            sig.append(stages.get("sig", 0))
            for name, (n, cyc) in items.items():
                per_item.setdefault(name, []).append((n, cyc))
                rows.append([build, log.stem, name, n, cyc])
            rows.append([build, log.stem, "stage.sig", 1, stages.get("sig", 0)])
        if not sig:
            md.append(f"\n### {build}\n\n(no boot_ok logs)\n")
            continue
        sig_mean = statistics.mean(sig)
        sig_rows.append((build, sig_mean, statistics.pstdev(sig), len(sig)))
        md.append(f"\n### {build} ({len(sig)} runs)\n")
        if incomplete:
            md.append(f"incomplete log, not counted: {', '.join(incomplete)}\n")
        md.append(f"sig stage: {sig_mean:,.0f} cyc = {sig_mean / mhz / 1000:.3f} ms "
                  f"(stdev {statistics.pstdev(sig):.1f} cyc)\n")
        if not per_item:
            md.append("(no MEASD lines)\n")
            continue
        md.append("| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |")
        md.append("|---|---|---|---|---|---|---|")
        top_sum = 0
        for name, vals in per_item.items():
            cyc = [v[1] for v in vals]
            n = vals[0][0]
            calls_vary = len({v[0] for v in vals}) > 1
            mean = statistics.mean(cyc)
            if is_top(name):
                top_sum += mean
            md.append(f"| {name} | {n}{'*' if calls_vary else ''} | {mean:,.0f} | "
                      f"{mean / mhz / 1000:.3f} | {100 * mean / sig_mean:.1f} | "
                      f"{mean / n:,.0f} | {statistics.pstdev(cyc):.1f} |")
        rest = sig_mean - top_sum
        md.append(f"| (rest of sig) | | {rest:,.0f} | {rest / mhz / 1000:.3f} | "
                  f"{100 * rest / sig_mean:.1f} | | |")
        md.append("")
    md.append("\n## sig stage per build (instrumentation cost)\n")
    md.append("| build | runs | sig cycles | sig ms | stdev cyc |")
    md.append("|---|---|---|---|---|")
    for build, mean, sd, n in sig_rows:
        md.append(f"| {build} | {n} | {mean:,.0f} | {mean / 168000:.3f} | {sd:.1f} |")
    text = "\n".join(md) + "\n"
    (out / "detail.md").write_text(text)
    print(text)
    with open(out / "detail.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["build", "run", "item", "calls", "cycles"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
