# 2026-09-30_stage4_mldsa44_bench

mldsa44 verify on STM32F429I-DISC1 (168 MHz), mldsa-native C backend, standalone app (not in MCUboot).

Public key 1312 B, signature 2420 B, message 32 B (SHA-256 of the test image, empty context).

| Case | n | rc | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|---|---|
| valid | 30 | [0] | 2,983,424 | 2,982,118 | 2,983,618 | 435.8 | 17.76 |
| bad_sig | 3 | [-1] | 329,725 | 329,725 | 329,725 | 0.0 | 1.96 |

Main stack peak use (bytes used / size): 44488 / 65536
