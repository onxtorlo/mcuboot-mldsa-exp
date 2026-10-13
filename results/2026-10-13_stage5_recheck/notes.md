# Notes: 2026-10-13_stage5_recheck (stage 3 re-examined)

Stage 3 (2026-09-30) tried 24 MCUboot v2.4.0 signature configurations and 7 worked.
This stage (1) sorts the 24 into combinations that are possible / not possible on this
platform, (2) finds why the possible ones failed and fixes them, (3) re-measures every
possible combination (10 boots + bad payload / bad signature / wrong key each), and
(4) looks into why Ed25519 verification is slow.

Platform: STM32F429I-DISC1 (Cortex-M4, 168 MHz), Zephyr v4.4.2 (Mbed TLS 4.1 /
TF-PSA-Crypto 1.x), MCUboot fork `sign-replace` @ e45b6b1e (v2.4.0 + timing), -Os.
The fixes are configuration only; MCUboot source is unchanged.

## 1. Possible / not possible

The 24 entries are 18 distinct combinations (signature x crypto backend x hash/pure)
plus 6 "_fix" variants that only add Kconfig workarounds to one of them.

### Possible (10) - all boot 10/10 and reject all three bad images

| # | Combination | Stage 3 entry | Stage 3 | Stage 5 configuration | Fix |
|---|---|---|---|---|---|
| 1 | none (SHA-256 only) | none | ok | none | - |
| 2 | RSA-2048, TF-PSA-Crypto legacy | rsa2048 | ok | rsa2048 | - |
| 3 | RSA-2048, PSA | rsa2048_psa | ok | rsa2048_psa | - |
| 4 | RSA-3072, TF-PSA-Crypto legacy | rsa3072 | ok | rsa3072 | - |
| 5 | RSA-3072, PSA | rsa3072_psa | rejected valid image | rsa3072_psa_heap16k | Mbed TLS heap 8 -> 16 KB |
| 6 | ECDSA P-256, TinyCrypt | ecdsa_p256 | ok | ecdsa_p256 | - |
| 7 | ECDSA P-256, PSA, SHA-256 | ecdsa_p256_psa / _psa_fix | build fail / rejected | ecdsa_p256_psa_heap (+ _nistopt) | enable Mbed TLS + PSA core, add 8 KB heap |
| 8 | Ed25519 over SHA-256, TinyCrypt | ed25519 | ok | ed25519 | - |
| 9 | Ed25519 over SHA-512, TinyCrypt | ed25519_sha512 | ok | ed25519_sha512 | - |
| 10 | Ed25519 pure, TinyCrypt | ed25519_pure | rejected valid image | ed25519_pure_sha512 | build MCUboot with SHA-512 |

### Not possible (8) on this platform without changing MCUboot code

| # | Combination | Stage 3 entries | Reason (verified) |
|---|---|---|---|
| 11 | RSA-2048, Mbed TLS 3.x legacy | rsa2048_mbedtls | Option is for Mbed TLS 3.x; Zephyr 4.4 ships Mbed TLS 4.x, which removed `mbedtls/sha256.h` and the legacy RSA API |
| 12 | RSA-3072, Mbed TLS 3.x legacy | rsa3072_mbedtls | same |
| 13 | ECDSA P-256, Mbed TLS legacy | ecdsa_p256_mbedtls, _mbedtls_fix | legacy ECP/ECDSA API is private in TF-PSA-Crypto 1.x; Kconfig dependency errors even with the workaround |
| 14 | ECDSA P-256, PSA, SHA-512 | ecdsa_p256_psa_sha512, _sha512_fix | MCUboot builds, but imgtool refuses `--sha 512` for a P-256 private key (allowed: 256), so no image can be signed. P-256 + SHA-512 is not a standard pairing |
| 15 | Ed25519, Mbed TLS | ed25519_mbedtls, _mbedtls_fix | fiat curve25519.c includes `mbedtls/sha512.h` (gone in 4.x) |
| 16 | Ed25519 pure, Mbed TLS | ed25519_pure_mbedtls | same |
| 17 | Ed25519, PSA | ed25519_psa, _psa_fix | TF-PSA-Crypto has no EdDSA: key import returns -135 `PSA_ERROR_NOT_SUPPORTED` (Kconfig itself notes "upstream mbedTLS does not have TE"; only Nordic Oberon provides it) |
| 18 | Ed25519 pure, PSA | ed25519_pure_psa, _psa_fix | same |

24 entries = 10 possible combinations (12 entries: rsa3072_psa, ecdsa_p256_psa(+_fix),
ed25519_pure among them) + 8 impossible combinations (12 entries).

## 2. Why the possible ones failed (found with debug builds on the board)

- **RSA-3072 PSA**: `psa_verify_hash()` returned -141 `PSA_ERROR_INSUFFICIENT_MEMORY`.
  `BOOT_RSA_PSA` sets `MBEDTLS_HEAP_SIZE` 8192, enough for 2048-bit but not 3072-bit
  bignums. 16 KB works (107.5 ms).
- **ECDSA P-256 PSA**: `BOOT_ECDSA_PSA` selects `PSA_CRYPTO_C`, which no longer enables
  the library under Zephyr 4.4 (build fails: `psa/crypto.h` missing). With
  `CONFIG_MBEDTLS=y` + `CONFIG_PSA_CRYPTO=y` it builds, but key import returned -137
  `PSA_ERROR_BAD_STATE`: the PSA core was never initialised. Zephyr calls
  `psa_crypto_init()` at boot (SYS_INIT), but it failed with -141 because
  `BOOT_ECDSA_PSA` (unlike the RSA/Ed25519 PSA options) does not select
  `MBEDTLS_ENABLE_HEAP`. With an 8 KB heap everything works. The verify is then very
  slow (2139 ms) because `MBEDTLS_ECP_NIST_OPTIM` is off (`BOOT_ECDSA_MBEDTLS` selects it,
  `BOOT_ECDSA_PSA` does not); with it on: 360 ms. Still slower than TinyCrypt (108 ms):
  generic Mbed TLS bignum + heap allocator, window size 2.
- **Ed25519 pure**: rejected after 34 us, before any signature work. imgtool always uses
  SHA-512 for `--pure` (`ALLOWED_PURE_KEY_SHA = {Ed25519: [512]}`), so the KEYHASH TLV is
  64 bytes, while MCUboot built with the default SHA-256 has a 32-byte key buffer:
  `len > KEY_BUF_SIZE` -> `rc = -1` (`result=other`). Building MCUboot with
  `BOOT_IMG_HASH_ALG_SHA512` makes it work (40.4 ms, includes SHA-512 over the image).
  MCUboot Kconfig does not force SHA-512 for pure, so the default build cannot work.

## 3. Ed25519 verification time (24.05 ms = 4.04 M cycles)

Measured with temporary DWT counters inside `ED25519_verify()` (ed25519, TinyCrypt):

| Step | cycles | share |
|---|---|---|
| point decompression (public key) | 207,665 | 5.1 % |
| SHA-512(R, A, M) | 23,686 | 0.6 % |
| double scalar multiplication sB - hA | 3,610,877 | 89.4 % |
| encode result point (field inversion) | 197,527 | 4.9 % |

- The time is in the field arithmetic, not in hashing or key parsing. The inversion step
  is ~265 field squarings/multiplications, so one field operation costs ~745 cycles.
- MCUboot uses BoringSSL/fiat-crypto portable C (`ext/fiat/src/curve25519.c`, 10 x 25.5-bit
  limbs, 64-bit products), not a Cortex-M4 assembly implementation. Assembly
  implementations for this core (UMAAL-based field multiplication) are several times
  faster per field operation, which is where "Ed25519 is fast" comes from.
- `-Os` (Zephyr default, also for MCUboot) costs ~20 %: with `CONFIG_SPEED_OPTIMIZATIONS`
  sig drops from 4.04 M to 3.25 M cycles (19.4 ms).
- Flash wait states are not the cause: Zephyr enables the ART accelerator (prefetch,
  I/D cache) on STM32F4.
- Verification also does more than signing would: a double scalar multiplication with a
  variable base point (only the base-point half uses the precomputed table).
- Relative order is as expected for portable C: Ed25519 (24 ms) < RSA-2048 (52 ms,
  e = 65537 makes RSA verify cheap) < ECDSA P-256 TinyCrypt (108 ms). ML-DSA-44 (17.8 ms
  standalone) being faster than Ed25519 matches the literature: ML-DSA verify is NTT +
  SHAKE, no big-integer/field inversion work.

## Reading the numbers

- Same image (17,456 B payload), same keys as stage 3. ECDSA timings differ slightly from
  stage 3 (107.9 vs 105.0 ms) because the image was re-signed (new random ECDSA nonce ->
  different signature values -> different scalar bit patterns).
- `ed25519_pure_sha512`: no separate hash stage; the signature step covers SHA-512 of the
  whole image (`hash` empty). Its bad payload is rejected as `bad_sig` (no hash TLV).
- ECDSA PSA signature TLV is 72 B vs 71 B for TinyCrypt only because of the DER encoding
  of the re-signed signature (leading zero byte).
