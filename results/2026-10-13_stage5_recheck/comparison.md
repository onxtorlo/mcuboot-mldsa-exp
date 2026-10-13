# 2026-10-13_stage5_recheck: signature comparison

Valid image, mean of all runs (stdev in cycles). ms at 168 MHz.

## Verification time (configurations that boot a valid image)

| Configuration | sig ms | hash ms | validate ms | total ms | sig stdev (cyc) | valid image |
|---|---|---|---|---|---|---|
| ecdsa_p256 | 107.89 | 9.828 | 117.832 | 139.367 | 0.0 | booted 10/10 |
| ecdsa_p256_psa_heap | 2139.262 | 10.955 | 2150.361 | 2171.914 | 0.0 | booted 10/10 |
| ecdsa_p256_psa_heap_nistopt | 360.452 | 11.563 | 372.167 | 393.711 | 0.0 | booted 10/10 |
| ed25519 | 24.049 | 9.938 | 34.072 | 55.633 | 0.0 | booted 10/10 |
| ed25519_pure_sha512 | 40.436 |  | 40.623 | 62.158 | 0.0 | booted 10/10 |
| ed25519_sha512 | 24.188 | 17.054 | 41.423 | 62.95 | 0.0 | booted 10/10 |
| none |  | 9.942 | 9.962 | 31.488 |  | booted 10/10 |
| rsa2048 | 52.49 | 10.815 | 63.556 | 85.238 | 0.0 | booted 10/10 |
| rsa2048_psa | 53.681 | 11.463 | 65.413 | 86.948 | 0.0 | booted 10/10 |
| rsa3072 | 103.989 | 10.827 | 115.132 | 137.023 | 0.0 | booted 10/10 |
| rsa3072_psa_heap16k | 107.487 | 11.46 | 119.295 | 140.812 | 0.0 | booted 10/10 |

## Size and memory

| Configuration | MCUboot FLASH (B) | MCUboot RAM (B) | stack peak (B) | public key (B) | signature (B) | TLV area (B) | works |
|---|---|---|---|---|---|---|---|
| ecdsa_p256 | 31108 | 18240 | 1424 | 91 | 71 | 151 | yes |
| ecdsa_p256_psa_heap | 49012 | 27328 | 1600 | 91 | 72 | 152 | yes |
| ecdsa_p256_psa_heap_nistopt | 49996 | 27328 | 1528 | 91 | 72 | 152 | yes |
| ed25519 | 42224 | 18240 | 4028 | 44 | 64 | 144 | yes |
| ed25519_pure_sha512 | 41024 | 18240 | 3988 | 44 | 64 | 213 | yes |
| ed25519_sha512 | 41176 | 18240 | 4060 | 44 | 64 | 208 | yes |
| none | 26448 | 18240 | 680 |  | 0 | 40 | yes |
| rsa2048 | 37260 | 33664 | 2616 | 270 | 256 | 336 | yes |
| rsa2048_psa | 43456 | 27328 | 2336 | 270 | 256 | 336 | yes |
| rsa3072 | 37392 | 39552 | 2904 | 398 | 384 | 464 | yes |
| rsa3072_psa_heap16k | 43584 | 35520 | 2464 | 398 | 384 | 464 | yes |

MCUboot FLASH/RAM: build without measurement. Stack peak: measurement build (for configurations that do not work it is the peak up to the failure).

## Rejection tests

| Configuration | bad payload | bad signature | wrong key |
|---|---|---|---|
| ecdsa_p256 | hash_mismatch | bad_sig | no_key |
| ecdsa_p256_psa_heap | hash_mismatch | bad_sig | no_key |
| ecdsa_p256_psa_heap_nistopt | hash_mismatch | bad_sig | no_key |
| ed25519 | hash_mismatch | bad_sig | no_key |
| ed25519_pure_sha512 | bad_sig | bad_sig | no_key |
| ed25519_sha512 | hash_mismatch | bad_sig | no_key |
| none | hash_mismatch | - | - |
| rsa2048 | hash_mismatch | bad_sig | no_key |
| rsa2048_psa | hash_mismatch | bad_sig | no_key |
| rsa3072 | hash_mismatch | bad_sig | no_key |
| rsa3072_psa_heap16k | hash_mismatch | bad_sig | no_key |

## Configurations

| Configuration | Description |
|---|---|
| ecdsa_p256 | ECDSA P-256, TinyCrypt (default) |
| ecdsa_p256_psa_heap | ECDSA P-256, PSA API + Mbed TLS/PSA core + 8 KB Mbed TLS heap |
| ecdsa_p256_psa_heap_nistopt | ECDSA P-256, PSA API + 8 KB Mbed TLS heap + NIST curve fast reduction (BOOT_ECDSA_MBEDTLS selects it, BOOT_ECDSA_PSA does not) |
| ed25519 | Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| ed25519_pure_sha512 | Ed25519 pure (signature over the whole image), TinyCrypt, SHA-512 |
| ed25519_sha512 | Ed25519 over SHA-512 image hash, TinyCrypt |
| none | No signature: SHA-256 hash check only (TinyCrypt) |
| rsa2048 | RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| rsa2048_psa | RSA-2048, PSA API |
| rsa3072 | RSA-3072, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| rsa3072_psa_heap16k | RSA-3072, PSA API + 16 KB Mbed TLS heap (default 8 KB is too small: psa_verify_hash -> PSA_ERROR_INSUFFICIENT_MEMORY) |
