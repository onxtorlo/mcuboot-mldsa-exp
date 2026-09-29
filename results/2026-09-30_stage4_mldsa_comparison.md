# ML-DSA levels vs classical signatures (2026-09-30)

Signature verification on STM32F429I-DISC1 (Cortex-M4, 168 MHz), Zephyr v4.4.2.
ML-DSA: standalone benchmark (`apps/mldsa_bench`, mldsa-native C backend, not in
MCUboot yet), 30 runs each. Classical: stage 3, inside MCUboot, 10 runs each.

| Algorithm | NIST level | verify ms | stack peak (B) | public key (B) | signature (B) | source |
|---|---|---|---|---|---|---|
| ML-DSA-44 | 2 | 17.76 | 44,488 | 1,312 | 2,420 | 2026-09-30_stage4_mldsa44_bench |
| ML-DSA-65 | 3 | 29.31 | 68,104 | 1,952 | 3,309 | 2026-09-30_stage4_mldsa65_bench |
| ML-DSA-87 | 5 | 49.57 | 105,224 | 2,592 | 4,627 | 2026-09-30_stage4_mldsa87_bench |
| Ed25519 (TinyCrypt) | - | 24.05 | 4,028 | 44 | 64 | 2026-09-30_stage3/ed25519 |
| RSA-2048 | - | 52.49 | 2,616 | 270 | 256 | 2026-09-30_stage3/rsa2048 |
| RSA-3072 | - | 103.99 | 2,872 | 398 | 384 | 2026-09-30_stage3/rsa3072 |
| ECDSA P-256 (TinyCrypt) | - | 104.99 | 1,400 | 91 | 71 | 2026-09-30_stage3/ecdsa_p256 |

Tampered signature (last byte flipped) rejected in every run: ML-DSA-44 1.96 ms,
ML-DSA-65 2.72 ms, ML-DSA-87 4.21 ms.

## Caveats

- ML-DSA figures are the bare `crypto_sign_verify()` call; classical figures are
  MCUboot's `bootutil_verify_sig()` (includes key parsing). Not yet measured
  inside MCUboot.
- Stack peak: MCUboot's main stack is 10 KB. ML-DSA-44 needs ~44 KB, ML-DSA-87
  ~105 KB (the board has 192 KB RAM). Stack sizes set for the benchmark: 64 KB
  (ML-DSA-44), 128 KB (65, 87); the stack size does not change the timing.
- Classical public key sizes are the DER-encoded keys MCUboot embeds; ML-DSA sizes
  are raw FIPS 204 public keys.
- ML-DSA runs vary by < 0.02 % (stdev 436-761 cycles); MCUboot runs are exact.
- mldsa-native C code, no Cortex-M4 specific optimisation; timing side channels
  only (no power/EM/fault-injection protection).
