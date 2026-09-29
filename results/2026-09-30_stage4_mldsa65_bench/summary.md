# 2026-09-30_stage4_mldsa65_bench

mldsa65 verify on STM32F429I-DISC1 (168 MHz), mldsa-native C backend, standalone app (not in MCUboot).

Public key 1952 B, signature 3309 B, message 32 B (SHA-256 of the test image, empty context).

| Case | n | rc | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|---|---|
| valid | 30 | [0] | 4,924,765 | 4,924,301 | 4,925,855 | 699.6 | 29.31 |
| bad_sig | 3 | [-1] | 456,451 | 456,451 | 456,451 | 0.0 | 2.72 |

Main stack peak use (bytes used / size): 68104 / 131072
