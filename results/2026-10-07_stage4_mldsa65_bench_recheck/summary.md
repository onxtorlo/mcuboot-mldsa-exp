# 2026-10-07_stage4_mldsa65_bench_recheck

mldsa65 verify on STM32F429I-DISC1 (168 MHz), mldsa-native C backend, standalone app (not in MCUboot).

Public key 1952 B, signature 3309 B, message 32 B (SHA-256 of the test image, empty context).

| Case | n | rc | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|---|---|
| valid | 30 | [0] | 4,924,653 | 4,924,192 | 4,925,745 | 700.6 | 29.31 |
| bad_sig | 3 | [-1] | 456,483 | 456,483 | 456,483 | 0.0 | 2.72 |

Main stack peak use (bytes used / size): 68104 / 131072
