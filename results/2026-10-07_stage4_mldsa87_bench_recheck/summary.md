# 2026-10-07_stage4_mldsa87_bench_recheck

mldsa87 verify on STM32F429I-DISC1 (168 MHz), mldsa-native C backend, standalone app (not in MCUboot).

Public key 2592 B, signature 4627 B, message 32 B (SHA-256 of the test image, empty context).

| Case | n | rc | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|---|---|
| valid | 30 | [0] | 8,328,058 | 8,327,279 | 8,328,858 | 760.7 | 49.57 |
| bad_sig | 3 | [-1] | 707,700 | 707,700 | 707,700 | 0.0 | 4.21 |

Main stack peak use (bytes used / size): 105224 / 131072
