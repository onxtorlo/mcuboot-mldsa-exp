# Notes: 2026-10-07_stage4_mldsa87_bench_recheck

Recheck of 2026-09-30_stage4_mldsa87_bench, same setup and board state as
2026-10-07_stage4_mldsa44_bench_recheck (see its notes.md), with ML-DSA-87 and a
128 KB main stack (run: apps/mldsa_bench/run_bench.sh 87 <dir> 131072).

| Case | 2026-09-30 | 2026-10-07 | diff |
|---|---|---|---|
| valid, mean cycles (n=30, rc=0) | 8,328,090 | 8,328,058 | -0.00 % |
| valid, mean ms | 49.57 | 49.57 | |
| bad_sig, cycles (n=3, rc=-1) | 707,634 | 707,700 | +0.01 % |
| main stack peak (B) | 105,224 | 105,224 | 0 |
