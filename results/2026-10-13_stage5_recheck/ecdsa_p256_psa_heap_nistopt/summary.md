# ecdsa_p256_psa_heap_nistopt

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T15:47:40 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256_psa_heap_nistopt: ECDSA P-256, PSA API + 8 KB Mbed TLS heap + NIST curve fast reduction (BOOT_ECDSA_MBEDTLS selects it, BOOT_ECDSA_PSA does not) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot |  @ e45b6b1 |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_nistopt_measure, ecdsa_p256_psa_heap_nistopt |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV ECDSA_SIG | 72 |
| TLV area total | 152 |
| File | 18120 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 66,143,479 | 66,143,479 | 66,143,479 | 0.0 | 393.71 |
| validate | 62,524,132 | 62,524,132 | 62,524,132 | 0.0 | 372.17 |
| hash | 1,942,660 | 1,942,660 | 1,942,660 | 0.0 | 11.56 |
| sig | 60,555,916 | 60,555,916 | 60,555,916 | 0.0 | 360.45 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1528 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.58 | 11.56 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 373.60 | 11.56 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.71 | 11.56 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_nistopt_measure | 50556 | 152 | 27196 | 50708 | 27392 | 91 |
| ecdsa_p256_psa_heap_nistopt | 49844 | 152 | 27131 | 49996 | 27328 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap_nistopt.build.log`
- `build_logs/boot_ecdsa_p256_psa_heap_nistopt_measure.build.log`
- `build_size.csv`
- `logs/boot_ok_run01.log`
- `logs/boot_ok_run02.log`
- `logs/boot_ok_run03.log`
- `logs/boot_ok_run04.log`
- `logs/boot_ok_run05.log`
- `logs/boot_ok_run06.log`
- `logs/boot_ok_run07.log`
- `logs/boot_ok_run08.log`
- `logs/boot_ok_run09.log`
- `logs/boot_ok_run10.log`
- `logs/reject_bad_key.log`
- `logs/reject_bad_payload.log`
- `logs/reject_bad_sig.log`
- `meta.json`
- `reject.csv`
