# Notes: 2026-10-07_stage4_mldsa65_bench_recheck

Recheck of 2026-09-30_stage4_mldsa65_bench, same setup and board state as
2026-10-07_stage4_mldsa44_bench_recheck (see its notes.md), with ML-DSA-65 and a
128 KB main stack (run: apps/mldsa_bench/run_bench.sh 65 <dir> 131072).

| Case | 2026-09-30 | 2026-10-07 | diff |
|---|---|---|---|
| valid, mean cycles (n=30, rc=0) | 4,924,765 | 4,924,653 | -0.00 % |
| valid, mean ms | 29.31 | 29.31 | |
| bad_sig, cycles (n=3, rc=-1) | 456,451 | 456,483 | +0.01 % |
| main stack peak (B) | 68,104 | 68,104 | 0 |
