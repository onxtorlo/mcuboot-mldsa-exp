# 2026-09-30_stage4_mldsa87_bench

mldsa87 verify on STM32F429I-DISC1 (168 MHz), mldsa-native C backend, standalone app (not in MCUboot).

Public key 2592 B, signature 4627 B, message 32 B (SHA-256 of the test image, empty context).

| Case | n | rc | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|---|---|
| valid | 30 | [0] | 8,328,090 | 8,327,305 | 8,328,886 | 761.3 | 49.57 |
| bad_sig | 3 | [-1] | 707,634 | 707,634 | 707,634 | 0.0 | 4.21 |

Main stack peak use (bytes used / size): 105224 / 131072
