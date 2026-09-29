# Notes: 2026-09-30_stage3 (baseline, all MCUboot v2.4.0 signature configurations)

Every signature type / crypto backend / hash option that MCUboot v2.4.0's
`boot/zephyr/Kconfig` offers on a non-Nordic Cortex-M4 was built and, if it
built, measured on the board: 10 boots of a valid image plus 3 rejection
cases (bad payload, bad signature byte, wrong key). Same application image
(17,456 B payload) for every configuration.

Environment: Zephyr v4.4.2 (Mbed TLS 4.1 / TF-PSA-Crypto), MCUboot fork
`sign-replace` @ e45b6b1e (v2.4.0 + boot timing instrumentation),
exp `dev` @ 124d1cd. Run log: `run.log`. Build results: `build_status.csv`.
Tables: `comparison.md` / `comparison.csv`; per configuration: `<conf>/`.

## Outcome per configuration (24 attempted = 18 from Kconfig + 6 config-only workarounds)

| Status | Configurations |
|---|---|
| Works (7) | none, rsa2048, rsa2048_psa, rsa3072, ecdsa_p256, ed25519, ed25519_sha512 |
| Builds, rejects valid image (5) | rsa3072_psa, ecdsa_p256_psa_fix, ed25519_psa_fix, ed25519_pure, ed25519_pure_psa_fix |
| Builds, cannot be signed (1) | ecdsa_p256_psa_sha512_fix |
| Does not build (11) | *_mbedtls (5), ecdsa_p256_psa, ecdsa_p256_psa_sha512, ed25519_psa, ed25519_pure_psa, ecdsa_p256_mbedtls_fix, ed25519_mbedtls_fix |

Defaults per algorithm (what MCUboot picks with no backend option) are:
rsa2048 / rsa3072 (TF-PSA-Crypto legacy), ecdsa_p256 (TinyCrypt), ed25519 (TinyCrypt).
All default configurations work.

## Why the others fail (observed; causes marked "likely" were not traced further)

- **Mbed TLS legacy backends** (`BOOT_*_MBEDTLS*`): MCUboot includes Mbed TLS 3.x
  headers (`mbedtls/sha256.h`, `mbedtls/sha512.h`) that Mbed TLS 4.x no longer
  provides. Config-only workarounds (`*_mbedtls_fix`) do not help. Needs code changes.
- **ECDSA / Ed25519 PSA backends** (`BOOT_ECDSA_PSA`, `BOOT_ED25519_PSA`): they select
  `PSA_CRYPTO_C` / `MBEDTLS_PSA_CRYPTO_C`, which under Zephyr 4.4's Kconfig do not
  enable the crypto library (`psa/crypto.h` missing, or Kconfig dependency errors).
  With `CONFIG_MBEDTLS=y` + `CONFIG_PSA_CRYPTO=y` (`*_psa_fix`) they build, but
  signature verification fails for the valid image in a few thousand cycles
  (likely PSA init or key import not done on this path).
- **RSA-3072 PSA** (`rsa3072_psa`): builds, verification of the valid image fails
  in ~1 ms (RSA-2048 PSA works). Likely the PSA/Mbed TLS heap
  (`MBEDTLS_HEAP_SIZE` 8192 by default for RSA PSA) is too small for 3072-bit keys.
- **Ed25519 pure** (`ed25519_pure`, `ed25519_pure_psa_fix`): builds, valid image
  rejected after ~34 us, before any signature work (`sig n=0`, `result=other`).
  Likely `flash_device_base()` fails in the pure path (the signature is checked
  directly on memory-mapped flash); not traced further.
- **ECDSA P-256 with SHA-512** (`ecdsa_p256_psa_sha512_fix`): imgtool 2.4.0 refuses
  `--sha 512` for an ECDSA P-256 key, so no image can be signed for it.

## Reading the numbers

- `sig`/`validate` are the comparison metrics; `total` includes UART log output.
- Cycle counts are identical across runs within a build (stdev 0). Between builds
  they can shift by ~0.02-0.1 % (see stage 2 notes); e.g. rsa2048 sig was
  8,815,930 cycles in stage 2 and 8,818,448 here (~52.49 ms both).
- For configurations that do not work, timings and stack peak cover only the
  path up to the failure and are not comparable.
- `ed25519_sha512` hashes the image with SHA-512 (17.05 ms vs 9.94 ms for SHA-256).
- ECDSA P-256 on TinyCrypt (105 ms) is slower than RSA-2048 (52.5 ms) here:
  RSA verify uses the small public exponent, ECDSA verify needs full scalar
  multiplications on an unoptimized C implementation.
- CSV `time` columns use the WSL clock and are not reliable; order by `run`.
