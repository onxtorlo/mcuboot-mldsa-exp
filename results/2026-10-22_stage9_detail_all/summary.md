# 2026-10-22_stage9_detail_all: where the verification time goes (all backends, -Os)

STM32F429I-DISC1, 168 MHz, DWT cycle counter, MCUboot sign-replace @ 6a809c68
(+ tf-psa-crypto / mldsa-native hooks, exp `patches/`). Same signed images as stage 7
(one image per key; the TinyCrypt and PSA ECDSA builds verify the very same signature).
10 boots per build, cycles identical on every boot (stdev 0). ms = cycles / 168,000.
Step tables: `_sig_detail` builds (<= 0.9 % counting cost; PSA ECDSA builds +-3 %,
code placement, section 8). Primitive tables: `_sig_prims`
builds (shares only; they add up to 7 %, see section 7). Full tables: `detail.md`.

## 1. Overview

| configuration | sig ms | where the time is (step) | main primitive |
|---|---|---|---|
| ML-DSA-44 (mldsa-native) | 17.25 | expand A from rho: 56.5 % | Keccak-f1600: 99 x 16.5k cyc = 56 % |
| ML-DSA-65 | 29.47 | expand A: 62.8 % | Keccak-f1600: 174 x 16.5k cyc = 58 % |
| ML-DSA-87 | 50.15 | expand A: 68.7 % | Keccak-f1600: 311 x 16.5k cyc = 61 % |
| Ed25519 (fiat, TinyCrypt SHA-512) | 24.05 | h·A + s·B: 89.3 % | field mul/sq: ~3,000 x ~520 cyc = 36 % |
| RSA-2048 (TF-PSA-Crypto legacy) | 52.49 | s^e mod N: 99.0 %, of it R² mod N 37.8 % | montmul 37 x 143k cyc = 60 %; long division 1 x 3.3M cyc = 38 % |
| RSA-2048 (PSA) | 53.67 | psa_verify_hash 99.7 %, R² mod N 37.5 % | same as legacy |
| ECDSA P-256 (TinyCrypt) | 108.04 | Shamir loop: 94.1 % | field mul 4,200 x ~3,800 cyc = 84 % |
| ECDSA P-256 (PSA, NIST fast reduction) | 351.02 | u2·Q 65 %, u1·G 23 % | inversion 6 x 3.46M cyc = 35 %; mul_mod 3,916 x 6.8k cyc = 45 % |
| ECDSA P-256 (PSA, generic reduction) | 2,207.52 | u2·Q 72.5 %, u1·G 25.1 % | reduction by division 3,919 x 82k cyc = 87 % |

## 2. ECDSA P-256, TinyCrypt (sig 108.01 ms in the detail build)

| step | calls | ms | % |
|---|---|---|---|
| key parse + signature decode (ASN.1) | 2 | 0.007 | 0.0 |
| 1/s mod n (binary inversion) | 1 | 1.345 | 1.2 |
| u1, u2 mod n | 1 | 1.974 | 1.8 |
| G + Q precompute | 1 | 1.598 | 1.5 |
| Shamir loop | 1 | 101.629 | 94.1 |
| - doubling | 255 | 50.608 | 46.9 |
| - addition | 195 | 50.778 | 47.0 |
| final inversion, compare | 1 | 1.433 | 1.3 |

Primitives: `vli_mult` 4,201 x 1,556 cyc (33.8 %), `mmod_fast` 4,199 x 2,280 cyc (49.5 %),
bit-serial `modInv` 3 x 227k + `mmod` 2 x 166k = 5.2 %. Details and compiler options:
stage 8.

## 3. ECDSA P-256 over PSA (TF-PSA-Crypto `ecp.c`), same signature

| step | generic reduction ms | % | NIST fast reduction ms | % |
|---|---|---|---|---|
| key import (ASN.1 + `psa_import_key`, point check) | 1.665 | 0.1 | 0.216 | 0.1 |
| 1/s mod n | 21.374 | 1.0 | 20.616 | 5.8 |
| u1, u2 | 0.983 | 0.0 | 0.948 | 0.3 |
| u1·G (comb, fixed point) | 554.616 | 25.1 | 81.026 | 22.7 |
| u2·Q (comb; table for Q built every time) | 1,601.410 | 72.5 | 232.912 | 65.2 |
| add + to affine | 26.766 | 1.2 | 21.354 | 6.0 |
| final mod n, compare | 0.006 | 0.0 | 0.007 | 0.0 |

(generic: `.pre_fix` detail build, 2,208.6 ms; NIST: prims build, 357.4 ms. The final
detail builds give the same shares within 0.3 points, see section 8.)

Primitives (prims builds):

| primitive | generic: calls x cyc | % | NIST: calls x cyc | % |
|---|---|---|---|---|
| `ecp.mul_mod` (product + reduction) | 3,916 x 86,222 | 90.9 | 3,916 x 6,838 | 44.6 |
| - `mpi.mul_mpi` (product) | 3,918 x 3,710 | 3.9 | 3,918 x 3,619 | 23.6 |
| - `ecp.modp` (reduction) | 3,916 x 82,341 | 86.8 | 3,916 x 3,035 | 19.8 |
| `mpi.inv_mod` (binary GCD inversion) | 6 x 3.58M | 5.8 | 6 x 3.46M | 34.6 |
| `ecp.precompute_comb` (table for Q) | 1 x 156M | 42.0 | 1 x 23.4M | 38.9 |
| `ecp.double_jac` | 308 x 718k | 59.5 | 308 x 80k | 41.0 |
| `ecp.add_mixed` | 124 x 965k | 32.2 | 124 x 100k | 20.6 |
| `ecp.normalize` (one inversion each) | 5 x 4.93M | 6.6 | 5 x 3.60M | 30.0 |

- Without `MBEDTLS_ECP_NIST_OPTIM` every field reduction is a long division
  (`mbedtls_mpi_mod_mpi`): 82k cycles instead of 3k. That alone is the 2.2 s.
- With it, the field multiplication (6.8k cyc) is still ~1.8x TinyCrypt's (3.8k), and
  verification needs 6 inversions (5 mod p in the point normalizations + 1/s mod n;
  binary GCD, ~3.5M cyc = ~21 ms each) where TinyCrypt needs 2 mod p + 1 mod n
  (~227k cyc each, 15x cheaper).
- The comb method does fewer additions (124 vs 195) but more doublings (308 vs 255), and
  builds a precomputation table for the public key Q on every verify (23.4M cyc, 39 %).

## 4. RSA-2048 (e = 65537)

| step | legacy ms | % | PSA ms | % |
|---|---|---|---|---|
| key parse (legacy: ASN.1 + `check_pubkey`; PSA: `psa_import_key`) | 0.043 | 0.1 | 0.120 | 0.2 |
| s^e mod N (legacy: `mbedtls_rsa_public`; PSA: inside `psa_verify_hash`) | 51.541 | 99.0 | | |
| - R² mod N (long division) | 19.667 | 37.8 | 20.113 | 37.5 |
| - to Montgomery | 0.816 | 1.6 | 0.840 | 1.6 |
| - square-and-multiply, 17 bits | 28.678 | 55.1 | 29.547 | 55.0 |
| - from Montgomery | 2.181 | 4.2 | 2.204 | 4.1 |
| PSS: MGF1 mask | 0.358 | 0.7 | (in psa_verify_hash) | |
| PSS: H' and compare | 0.090 | 0.2 | (in psa_verify_hash) | |

- 37 Montgomery multiplications x 143k cycles (window size 1 for a 17-bit exponent:
  17 squarings + 17 multiplications, 1 table entry, to/from Montgomery).
- R² mod N is recomputed by long division on every verify because the key context is
  new each time (`ctx->RN` empty). It is 38 % of RSA verification.

## 5. Ed25519 (sig 24.27 ms in the detail build)

| step | calls | ms | % |
|---|---|---|---|
| key parse (ASN.1) | 1 | 0.004 | 0.0 |
| public key decompression (square root) | 1 | 1.255 | 5.2 |
| SHA-512(R, A, M) | 1 | 0.131 | 0.5 |
| h mod l | 1 | 0.012 | 0.0 |
| h·A + s·B, all | 1 | 21.683 | 89.3 |
| - sliding windows + table of A | 1 | 0.781 | 3.2 |
| - doubling | 252 | 10.767 | 44.4 |
| - add ±kA | 41 | 2.881 | 11.9 |
| - add ±kB (fixed table) | 40 | 2.603 | 10.7 |
| encode (inversion) + compare | 1 | 1.178 | 4.9 |

Primitives: field multiplication 1,464 x 565 cyc, squaring 1,521 x 480 cyc, one inversion
229k cyc. Loop steps also include carries/additions/point format conversions outside
the multiplications (field mul + sq = 36 % of sig).

## 6. ML-DSA (mldsa-native, portable C, default RAM mode)

| step | 44 ms | % | 65 ms | % | 87 ms | % |
|---|---|---|---|---|---|---|
| unpack pk, sig; norm check | 0.447 | 2.6 | 0.645 | 2.2 | 0.922 | 1.8 |
| mu = H(H(pk), M) (SHAKE256) | 1.235 | 7.1 | 1.775 | 6.0 | 2.316 | 4.6 |
| challenge c, NTT(c) | 0.353 | 2.0 | 0.365 | 1.2 | 0.396 | 0.8 |
| NTT(t1·2^d), c·t1 | 0.872 | 5.0 | 1.317 | 4.5 | 1.768 | 3.5 |
| **expand A (SHAKE128 + rejection)** | **9.756** | **56.5** | **18.481** | **62.8** | **34.571** | **68.7** |
| NTT(z) | 0.718 | 4.2 | 0.899 | 3.1 | 1.400 | 2.8 |
| A·z - c·t1 | 0.441 | 2.6 | 0.744 | 2.5 | 1.357 | 2.7 |
| inverse NTT | 0.748 | 4.3 | 1.123 | 3.8 | 1.497 | 3.0 |
| use hint, pack w1 | 0.530 | 3.1 | 0.668 | 2.3 | 0.896 | 1.8 |
| c' = H(mu, w1), compare | 0.767 | 4.4 | 0.771 | 2.6 | 0.994 | 2.0 |

| primitive | 44 | 65 | 87 |
|---|---|---|---|
| Keccak-f1600 permutation (calls, % of sig) | 99, 56.0 % | 174, 57.9 % | 311, 60.5 % |
| cycles per permutation | 16,455 | 16,515 | 16,459 |
| forward NTT (calls x cyc) | 9 x 30.2k | 12 x 30.2k | 16 x 31.9k |
| inverse NTT (calls x cyc) | 4 x 31.4k | 6 x 31.4k | 8 x 31.4k |

- ML-DSA verification time is mostly Keccak (SHAKE128 for A, SHAKE256 for mu and c),
  not polynomial arithmetic: forward + inverse NTTs together are 13.7 % (44), 11.1 % (65),
  9.0 % (87) of the prims-build sig stage.
- A grows with K x L (4x4, 6x5, 8x7 = 16, 30, 56 polynomials), which is why expand A
  goes from 56 % to 69 %.

## 7. Counting cost (sig stage per build)

| configuration | stages only | + steps | + primitives |
|---|---|---|---|
| ECDSA TinyCrypt | 108.041 | 108.010 (-0.0 %) | 115.028 (+6.5 %) |
| ECDSA PSA generic | 2,207.521 | 2,135.929 (-3.2 %; pre-fix build 2,208.606) | 2,211.529 (+0.2 %) |
| ECDSA PSA NIST | 351.018 | 361.070 (+2.9 %) | 357.407 (+1.8 %, 9 runs) |
| RSA-2048 legacy | 52.485 | 52.088 (-0.8 %) | 52.104 (-0.7 %) |
| RSA-2048 PSA | 53.674 | 53.679 (+0.0 %) | 53.678 (+0.0 %) |
| Ed25519 | 24.050 | 24.267 (+0.9 %) | 25.939 (+7.9 %) |
| ML-DSA-44 | 17.254 | 17.274 (+0.1 %) | 17.306 (+0.3 %) |
| ML-DSA-65 | 29.472 | 29.410 (-0.2 %) | 29.561 (+0.3 %) |
| ML-DSA-87 | 50.145 | 50.286 (+0.3 %) | 50.370 (+0.4 %) |

"Stages only" equals stage 7 to the cycle for every configuration, so the hooks cost
nothing when disabled. Negative values = code layout effects of a different build.

## 8. ECDSA over PSA: final detail builds and build-to-build variation

| build | sig ms | 1/s mod n (cyc) | u1·G ms | u2·Q ms |
|---|---|---|---|---|
| generic, `_measure` | 2,207.521 | | | |
| generic, `_sig_detail` before the counter fix (`.pre_fix`) | 2,208.606 | 3,590,882 | 554.616 | 1,601.410 |
| generic, `_sig_detail` after the fix (+1 counter pair, +32 B) | **2,135.929** | 3,463,502 | 536.442 | 1,548.769 |
| generic, `_sig_detail_sig_prims` | 2,211.529 | 3,578,230 | 555.357 | 1,603.719 |
| NIST, `_measure` | 351.018 | | | |
| NIST, `_sig_detail` (fixed) | 361.070 | 3,590,841 | 81.557 | 234.465 |
| NIST, `_sig_detail_sig_prims` (9 runs) | 357.407 | 3,463,563 | 81.026 | 232.912 |

- The same source with one more counter pair runs 3.3 % faster (generic) and the same
  bignum routine (1/s mod n, identical in both configurations) takes either ~3.46M or
  ~3.59M cycles depending on the build. For these large Mbed TLS builds, code placement
  alone moves the time by about +-3 %. Shares (% of sig) stay the same; absolute ms
  should be quoted from the `_measure` builds.
- Steps (from the fixed detail builds): generic: u2·Q 72.5 %, u1·G 25.1 %, rest 2.4 %;
  NIST: u2·Q 64.9 %, u1·G 22.6 %, add+normalize 6.1 %, 1/s 5.9 %.

## 9. Supplement: whole bootloader at -O3 (`_o3/`, stages + steps, 10 boots each)

| configuration | sig -Os ms | sig -O3 ms | change | hash -Os | hash -O3 | FLASH -Os | FLASH -O3 |
|---|---|---|---|---|---|---|---|
| ECDSA P-256 TinyCrypt | 108.041 | 69.442 | -35.7 % | 9.828 | 9.418 | 31,836 | 44,072 |
| ECDSA P-256 PSA generic | 2,207.521 | 1,196.837 | -45.8 % | 11.559 | 6.212 | 49,736 | 65,740 |
| ECDSA P-256 PSA NIST | 351.018 | 211.315 | -39.8 % | 10.960 | 6.208 | 50,716 | 66,904 |
| RSA-2048 legacy | 52.485 | 38.016 | -27.6 % | 10.823 | 6.155 | 37,984 | 48,160 |
| RSA-2048 PSA | 53.674 | 38.103 | -29.0 % | 11.467 | 6.204 | 44,184 | 57,904 |
| Ed25519 | 24.050 | 13.335 | -44.6 % | 9.941 | 9.406 | 42,956 | 58,764 |
| ML-DSA-44 | 17.254 | 16.187 | -6.2 % | 9.844 | 9.410 | 38,004 | 46,956 |
| ML-DSA-65 | 29.472 | 27.309 | -7.3 % | 9.940 | 9.401 | 38,748 | 47,972 |
| ML-DSA-87 | 50.145 | 46.841 | -6.6 % | 10.856 | 10.022 | 39,152 | 48,316 |

All 9 at -O3: valid image 10/10, bad payload / signature / key rejected as at -Os.
Stack peak changes by < 80 B.

- Order at -Os: ML-DSA-44 17.3 < Ed25519 24.1 < ML-DSA-65 29.5 < ML-DSA-87 50.1 <
  RSA-2048 52.5 < ECDSA TinyCrypt 108.0 ms.
  Order at -O3: Ed25519 13.3 < ML-DSA-44 16.2 < ML-DSA-65 27.3 < RSA-2048 38.0 <
  ML-DSA-87 46.8 < ECDSA TinyCrypt 69.4 ms.
- ML-DSA barely gains: at -O3 every polynomial step is faster, but the Keccak-heavy
  steps get slower (ML-DSA-44: expand A 9.756 -> 10.226 ms, mu 1.235 -> 1.350,
  c hash 0.767 -> 0.849). No primitives build at -O3, so the per-permutation cost was
  not measured directly.
- RSA at -O3: R² mod N (long division) 19.67 -> 9.74 ms, square-and-multiply only
  28.68 -> 25.84 ms (the Montgomery inner loop is already tight at -Os).
- Ed25519 at -O3: one doubling 7.2k -> 3.5k cycles.
- SHA-256 image hash is TinyCrypt in the TinyCrypt/Ed25519/ML-DSA builds and Mbed TLS in
  RSA / PSA builds; only the latter gets much faster at -O3 (~11 -> ~6.2 ms).
