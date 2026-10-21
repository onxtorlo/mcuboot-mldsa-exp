# 2026-10-22_stage8_ecdsa_detail: where ECDSA P-256 (TinyCrypt) spends its time

Board STM32F429I-DISC1, 168 MHz, DWT cycle counter. Same signed image as stage 7
(`hello_v1_ecdsa_p256.bin`). 10 boots per build; every build gave identical cycles on all
10 boots (stdev 0). ms = cycles / 168,000.

## 1. Steps inside the signature check (-Os, detail build, sig = 107.83 ms)

| step | calls | ms | % of sig |
|---|---|---|---|
| key parse (ASN.1) + signature decode (ASN.1) | 1 + 1 | 0.007 | 0.0 |
| load r, s, Q; range checks | 1 | 0.020 | 0.0 |
| 1/s mod n | 1 | 1.345 | 1.2 |
| u1 = e/s, u2 = r/s mod n | 1 | 1.974 | 1.8 |
| precompute G + Q | 1 | 1.598 | 1.5 |
| **Shamir loop u1·G + u2·Q** | 1 | **101.446** | **94.1** |
| - point doubling (every bit) | 255 | 50.516 | 46.8 |
| - point addition (bits where u1 or u2 is 1) | 195 | 50.751 | 47.1 |
| 1/Z mod p, to affine, compare | 1 | 1.433 | 1.3 |

## 2. Arithmetic primitives (-Os, prims build, sig = 112.93 ms, +4.5 % from counting)

| primitive | calls | ms | % of sig | cycles/call |
|---|---|---|---|---|
| `uECC_vli_mult` 256x256 bit, word-wise (32x32->64) | 4,201 | 39.28 | 34.8 | 1,571 |
| `vli_mmod_fast_secp256r1` P-256 reduction, word-wise | 4,199 | 56.13 | 49.7 | 2,246 |
| `uECC_vli_modInv` binary inversion, bit by bit | 3 | 4.06 | 3.6 | 227,344 |
| `uECC_vli_mmod` generic mod n, bit by bit | 2 | 1.98 | 1.8 | 166,282 |

Field multiplication (product + reduction) = 4,200 calls x ~3,800 cycles = 84.5 % of sig.
Bit-by-bit routines (modInv, mmod) = 5.4 %.

## 3. Compiler options (whole bootloader rebuilt; TinyCrypt unchanged)

| build | sig ms | vs -Os | validate ms | hash ms | total ms | FLASH (measure build) | stack peak |
|---|---|---|---|---|---|---|---|
| -Os (Zephyr default) | 108.041 | - | 117.984 | 9.828 | 139.519 | 31,836 B | 1,400 B |
| -O2 (`CONFIG_SPEED_OPTIMIZATIONS`) | 85.453 | -20.9 % | 94.359 | 8.812 | 115.764 | 38,252 B | 1,440 B |
| -O3 (+ `CONFIG_COMPILER_OPT="-O3"`) | **69.442** | **-35.7 %** | 78.957 | 9.418 | 100.344 | 44,072 B | 1,448 B |
| LTO, -Os (`CONFIG_LTO`) | 107.462 | -0.5 % | 117.702 | 10.130 | 139.217 | 27,996 B | 1,256 B |

All four builds: valid image boots 10/10; bad payload -> hash_mismatch, bad signature ->
bad_sig, wrong key -> no_key.

Per call (prims builds): `vli_mult` 1,571 (-Os) -> 1,484 (-O2) -> 1,441 (-O3) cycles;
`mmod_fast` 2,246 -> 1,462 -> 847 cycles. The gain comes almost entirely from the
reduction (add/sub helpers inlined); the 32x32 multiply loop stays ~1,450 cycles.

## 4. Answer to "it is slow because it works one bit at a time"

- Bit-serial arithmetic (binary inversion, generic reduction) is only ~5-6 % of the time.
- The scalar multiplication does process the scalars one bit per iteration (no window):
  255 doublings + 195 additions = 94 % of the time. But the cost is in each iteration:
  ~9-11 field multiplications per iteration at ~3,800 cycles each (-Os).
- So the time is set by the cost of one 256-bit field multiplication in portable C.
