# Notes: 2026-10-07_stage4_mldsa44_bench_recheck

Recheck of 2026-09-30_stage4_mldsa44_bench (see its notes.md for the method),
run on a second PC to confirm the benchmark reproduces.

## Setup

- New west workspace set up per README: Zephyr v4.4.2 (dccb095), SDK 1.0.1,
  mldsa-native 3fc1998 (same as 2026-09-30). Host pyca cryptography 50.0.2
  (2026-09-30: 50.0.1); it only generates the test vector.
- The board held firmware from another experiment, and OpenOCD could not attach
  to it (`DP initialisation failed`). Full chip erase first (`scripts/flash.sh
  erase`, whole 2 MB read back as 0xFF), then `run_bench.sh 44 <dir>` unmodified.
- A new key pair and signature are generated on every run (`bench_vectors.h`).

## Comparison with 2026-09-30

| Case | 2026-09-30 | 2026-10-07 | diff |
|---|---|---|---|
| valid, mean cycles (n=30, rc=0) | 2,983,424 | 2,986,375 | +0.10 % |
| valid, mean ms | 17.76 | 17.78 | |
| bad_sig, cycles (n=3, rc=-1) | 329,725 | 329,570 | -0.05 % |
| main stack peak (B) | 44,488 | 44,488 | 0 |

Reproduces: every valid signature verifies, the bad one is rejected, and the
small cycle difference is within what a different key/signature gives.
