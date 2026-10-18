# 2026-10-19_stage7_compare: signature comparison

Valid image, mean of all runs (stdev in cycles). ms at 168 MHz.

## Verification time (configurations that boot a valid image)

| Configuration | sig ms | hash ms | validate ms | total ms | sig stdev (cyc) | valid image |
|---|---|---|---|---|---|---|
| ecdsa_p256 | 108.041 | 9.828 | 117.984 | 139.519 | 0.0 | booted 10/10 |
| ed25519 | 24.05 | 9.938 | 34.072 | 55.633 | 0.0 | booted 10/10 |
| mldsa44 | 17.254 | 9.844 | 27.924 | 49.477 | 0.0 | booted 10/10 |
| mldsa65 | 29.472 | 9.94 | 40.615 | 62.159 | 0.0 | booted 10/10 |
| mldsa87 | 50.145 | 10.856 | 62.706 | 84.38 | 0.0 | booted 10/10 |
| rsa2048 | 52.49 | 10.825 | 63.556 | 85.238 | 0.0 | booted 10/10 |

## Size and memory

| Configuration | MCUboot FLASH (B) | MCUboot RAM (B) | stack peak (B) | public key (B) | signature (B) | TLV area (B) | works |
|---|---|---|---|---|---|---|---|
| ecdsa_p256 | 31124 | 18240 | 1400 | 91 | 71 | 151 | yes |
| ed25519 | 42240 | 18240 | 4028 | 44 | 64 | 144 | yes |
| mldsa44 | 37300 | 65344 | 47144 | 1312 | 2420 | 2500 | yes |
| mldsa65 | 38044 | 89920 | 71680 | 1952 | 3309 | 3389 | yes |
| mldsa87 | 38436 | 126784 | 110112 | 2592 | 4627 | 4707 | yes |
| rsa2048 | 37276 | 33664 | 2616 | 270 | 256 | 336 | yes |

MCUboot FLASH/RAM: build without measurement. Stack peak: measurement build (for configurations that do not work it is the peak up to the failure).

## Rejection tests

| Configuration | bad payload | bad signature | wrong key |
|---|---|---|---|
| ecdsa_p256 | hash_mismatch | bad_sig | no_key |
| ed25519 | hash_mismatch | bad_sig | no_key |
| mldsa44 | hash_mismatch | bad_sig | no_key |
| mldsa65 | hash_mismatch | bad_sig | no_key |
| mldsa87 | hash_mismatch | bad_sig | no_key |
| rsa2048 | hash_mismatch | bad_sig | no_key |

## Configurations

| Configuration | Description |
|---|---|
| ecdsa_p256 | ECDSA P-256, TinyCrypt (default) |
| ed25519 | Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| mldsa44 | ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C) |
| mldsa65 | ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| mldsa87 | ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| rsa2048 | RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
