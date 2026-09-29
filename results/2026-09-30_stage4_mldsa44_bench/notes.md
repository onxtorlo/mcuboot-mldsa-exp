# Notes: 2026-09-30_stage4_mldsa44_bench

Quick standalone measurement of ML-DSA-44 signature verification on the same
board, done before the MCUboot integration (stage 4) is finished.

## What was measured

- App `apps/mldsa_bench`: calls mldsa-native `crypto_sign_verify()` (ML-DSA-44,
  portable C backend, Zephyr fork 3fc1998) 10 times on a valid signature and once
  on a signature with its last byte flipped; board reset 3 times -> 30 valid runs.
- Message: SHA-256 of the test application image (32 B), empty context, i.e. what
  MCUboot would sign. Key pair and signature made on the host with pyca
  cryptography 50.0.1 (OpenSSL) and verified there first; `bench_vectors.h` holds
  the public key and signature used (private key not kept).
- Same board, 168 MHz, Zephyr v4.4.2, SDK 1.0.1, -Os as the bootloader builds.
  Cycles from the DWT counter; stack peak from Zephyr stack painting.

## Comparison with the stage 3 baseline (signature verification only)

| Algorithm | verify ms | stack peak (B) | public key (B) | signature (B) | source |
|---|---|---|---|---|---|
| **ML-DSA-44** | **17.76** | **44,488** | 1,312 | 2,420 | this run (standalone) |
| Ed25519 (TinyCrypt) | 24.05 | 4,028 | 44 | 64 | stage 3, in MCUboot |
| RSA-2048 | 52.49 | 2,616 | 270 | 256 | stage 3, in MCUboot |
| RSA-3072 | 103.99 | 2,872 | 398 | 384 | stage 3, in MCUboot |
| ECDSA P-256 (TinyCrypt) | 104.99 | 1,400 | 91 | 71 | stage 3, in MCUboot |

Stage 3 public key sizes are the encoded keys MCUboot embeds (DER); ML-DSA-44 is
the raw FIPS 204 public key.

## Caveats

- Not integrated into MCUboot yet. ML-DSA timing is the bare verify call; the
  stage 3 `sig` stage times `bootutil_verify_sig()` inside MCUboot (includes key
  parsing). The difference is expected to be small but is not measured.
- Stack: 44.5 KB here vs 10 KB main stack in the MCUboot build. Integration will
  need a larger stack or mldsa-native's reduced-RAM option; the stack figure here
  also includes the benchmark's own printf use (small).
- Valid-signature runs vary by up to ~1,500 cycles (stdev 436, < 0.02 %), unlike
  the fully deterministic MCUboot runs.
- The bad signature is rejected in 1.96 ms: the flipped last byte lands in the
  hint encoding, which is likely rejected before the full computation. Other
  corruptions may take longer to reject.
- Only ML-DSA-44; mldsa-native C code, no Cortex-M4 specific optimisation.
