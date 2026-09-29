#!/usr/bin/env python3
"""Parse BENCH lines from benchmark serial logs into CSV and a summary table.

usage: apps/mldsa_bench/parse_bench.py <result dir>
  reads  <result dir>/logs/bench_boot*.log
  writes <result dir>/bench.csv, <result dir>/summary.md
"""
import csv
import glob
import os
import re
import statistics
import sys

d = sys.argv[1]
rows, stack, hdr = [], set(), {}
for path in sorted(glob.glob(os.path.join(d, "logs", "bench_boot*.log"))):
    boot = re.search(r"bench_boot(\d+)", path).group(1)
    text = open(path).read()
    m = re.search(r"BENCH (\w+) clock_hz=(\d+) pk=(\d+) sig=(\d+) msg=(\d+)", text)
    hdr = {"alg": m.group(1), "clock_hz": int(m.group(2)), "pk": int(m.group(3)),
           "sig": int(m.group(4)), "msg": int(m.group(5))}
    for run, case, rc, cyc, us in re.findall(
            r"BENCH run=(\d+) case=(\w+) rc=(-?\d+) cyc=(\d+) us=(\d+)", text):
        rows.append({"boot": boot, "run": int(run), "case": case, "rc": int(rc),
                     "cyc": int(cyc), "us": int(us), "log": os.path.basename(path)})
    m = re.search(r"BENCH stack size=(\d+) used=(\d+)", text)
    if m:
        stack.add((int(m.group(2)), int(m.group(1))))

with open(os.path.join(d, "bench.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

hz = hdr["clock_hz"]
L = [f"# {os.path.basename(os.path.normpath(d))}", "",
     f"{hdr['alg']} verify on STM32F429I-DISC1 ({hz // 1_000_000} MHz), mldsa-native C backend, "
     f"standalone app (not in MCUboot).", "",
     f"Public key {hdr['pk']} B, signature {hdr['sig']} B, message {hdr['msg']} B "
     "(SHA-256 of the test image, empty context).", "",
     "| Case | n | rc | mean cycles | min | max | stdev | mean ms |", "|---|---|---|---|---|---|---|---|"]
for case in sorted({r["case"] for r in rows}, key=lambda c: c != "valid"):
    v = [r["cyc"] for r in rows if r["case"] == case]
    rcs = sorted({r["rc"] for r in rows if r["case"] == case})
    L.append(f"| {case} | {len(v)} | {rcs} | {statistics.mean(v):,.0f} | {min(v):,} | {max(v):,} | "
             f"{statistics.pstdev(v):,.1f} | {statistics.mean(v) / hz * 1000:.2f} |")
L += ["", "Main stack peak use (bytes used / size): "
      + ", ".join(f"{u} / {s}" for u, s in sorted(stack))]
with open(os.path.join(d, "summary.md"), "w") as f:
    f.write("\n".join(L) + "\n")
print("\n".join(L))
