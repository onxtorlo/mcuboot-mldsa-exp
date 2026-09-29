# 2026-09-30_stage3: signature comparison

Valid image, mean of all runs (stdev in cycles). ms at 168 MHz.

## Verification time (configurations that boot a valid image)

| Configuration | sig ms | hash ms | validate ms | total ms | sig stdev (cyc) | valid image |
|---|---|---|---|---|---|---|
| ecdsa_p256 | 104.985 | 9.828 | 114.928 | 136.462 | 0.0 | booted 10/10 |
| ed25519 | 24.05 | 9.938 | 34.072 | 55.633 | 0.0 | booted 10/10 |
| ed25519_sha512 | 24.188 | 17.054 | 41.423 | 62.949 | 0.0 | booted 10/10 |
| none |  | 9.942 | 9.962 | 31.488 |  | booted 10/10 |
| rsa2048 | 52.491 | 10.825 | 63.556 | 85.239 | 0.0 | booted 10/10 |
| rsa2048_psa | 53.682 | 11.463 | 65.413 | 86.948 | 0.0 | booted 10/10 |
| rsa3072 | 103.989 | 10.827 | 115.131 | 137.022 | 0.0 | booted 10/10 |

## Built but rejected the valid image (timings are time to fail, not comparable)

| Configuration | valid image | result | validate ms | sig ms |
|---|---|---|---|---|
| ecdsa_p256_psa_fix | booted 0/10 | bad_sig | 11.715 | 0.005 |
| ed25519_psa_fix | booted 0/10 | bad_sig | 14.562 | 2.887 |
| ed25519_pure | booted 0/10 | other | 0.035 | - |
| ed25519_pure_psa_fix | booted 0/10 | other | 0.035 | - |
| rsa3072_psa | booted 0/10 | bad_sig | 12.848 | 1.041 |

## Size and memory

| Configuration | MCUboot FLASH (B) | MCUboot RAM (B) | stack peak (B) | public key (B) | signature (B) | TLV area (B) | works |
|---|---|---|---|---|---|---|---|
| ecdsa_p256 | 31116 | 18240 | 1400 | 91 | 71 | 151 | yes |
| ed25519 | 42232 | 18240 | 4028 | 44 | 64 | 144 | yes |
| ed25519_sha512 | 41184 | 18240 | 4060 | 44 | 64 | 208 | yes |
| none | 26456 | 18240 | 680 |  | 0 | 40 | yes |
| rsa2048 | 37272 | 33664 | 2616 | 270 | 256 | 336 | yes |
| rsa2048_psa | 43464 | 27328 | 2336 | 270 | 256 | 336 | yes |
| rsa3072 | 37404 | 39552 | 2872 | 398 | 384 | 464 | yes |
| ecdsa_p256_psa_fix | 48020 | 20096 | 1152 | 91 | 71 | 151 | no |
| ed25519_psa_fix | 43656 | 21184 | 1344 | 44 | 64 | 144 | no |
| ed25519_pure | 42092 | 18240 | 472 | 44 | 64 | 213 | no |
| ed25519_pure_psa_fix | 43468 | 21184 | 1344 | 44 | 64 | 213 | no |
| rsa3072_psa | 43592 | 27328 | 2376 | 398 | 384 | 464 | no |

MCUboot FLASH/RAM: build without measurement. Stack peak: measurement build (for configurations that do not work it is the peak up to the failure).

## Rejection tests

| Configuration | bad payload | bad signature | wrong key |
|---|---|---|---|
| ecdsa_p256 | hash_mismatch | bad_sig | no_key |
| ecdsa_p256_psa_fix | hash_mismatch | bad_sig | no_key |
| ed25519 | hash_mismatch | bad_sig | no_key |
| ed25519_psa_fix | hash_mismatch | bad_sig | no_key |
| ed25519_pure | other | other | other |
| ed25519_pure_psa_fix | other | other | other |
| ed25519_sha512 | hash_mismatch | bad_sig | no_key |
| none | hash_mismatch | - | - |
| rsa2048 | hash_mismatch | bad_sig | no_key |
| rsa2048_psa | hash_mismatch | bad_sig | no_key |
| rsa3072 | hash_mismatch | bad_sig | no_key |
| rsa3072_psa | hash_mismatch | bad_sig | no_key |

## Configurations

| Configuration | Description |
|---|---|
| ecdsa_p256 | ECDSA P-256, TinyCrypt (default) |
| ecdsa_p256_psa_fix | ECDSA P-256, PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| ed25519 | Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| ed25519_psa_fix | Ed25519 over SHA-256 image hash, PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| ed25519_pure | Ed25519 pure (signature over the whole image), TinyCrypt |
| ed25519_pure_psa_fix | Ed25519 pure (signature over the whole image), PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| ed25519_sha512 | Ed25519 over SHA-512 image hash, TinyCrypt |
| none | No signature: SHA-256 hash check only (TinyCrypt) |
| rsa2048 | RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| rsa2048_psa | RSA-2048, PSA API |
| rsa3072 | RSA-3072, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| rsa3072_psa | RSA-3072, PSA API |

## Configurations that did not build

| Configuration | variant | first error |
|---|---|---|
| rsa2048_mbedtls | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| rsa2048_mbedtls | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| rsa3072_mbedtls | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| rsa3072_mbedtls | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| ecdsa_p256_mbedtls | plain | error: Aborting due to Kconfig warnings |
| ecdsa_p256_mbedtls | measure | error: Aborting due to Kconfig warnings |
| ecdsa_p256_psa | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:54:10: fatal error: psa/crypto.h: No such file or directory |
| ecdsa_p256_psa | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:54:10: fatal error: psa/crypto.h: No such file or directory |
| ecdsa_p256_psa_sha512 | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:54:10: fatal error: psa/crypto.h: No such file or directory |
| ecdsa_p256_psa_sha512 | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:54:10: fatal error: psa/crypto.h: No such file or directory |
| ed25519_mbedtls | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| ed25519_mbedtls | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| ed25519_psa | plain | error: Aborting due to Kconfig warnings |
| ed25519_psa | measure | error: Aborting due to Kconfig warnings |
| ed25519_pure_mbedtls | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| ed25519_pure_mbedtls | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/boot/bootutil/include/bootutil/crypto/sha.h:61:10: fatal error: mbedtls/sha256.h: No such file or directory |
| ed25519_pure_psa | plain | error: Aborting due to Kconfig warnings |
| ed25519_pure_psa | measure | error: Aborting due to Kconfig warnings |
| ecdsa_p256_mbedtls_fix | plain | error: PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC (defined at modules/mbedtls/Kconfig.psa.logic:36 |
| ecdsa_p256_mbedtls_fix | measure | error: PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_BASIC (defined at modules/mbedtls/Kconfig.psa.logic:36 |
| ed25519_mbedtls_fix | plain | /home/onxtorlo/secureboot/bootloader/mcuboot/ext/fiat/src/curve25519.c:37:10: fatal error: mbedtls/sha512.h: No such file or directory |
| ed25519_mbedtls_fix | measure | /home/onxtorlo/secureboot/bootloader/mcuboot/ext/fiat/src/curve25519.c:37:10: fatal error: mbedtls/sha512.h: No such file or directory |
