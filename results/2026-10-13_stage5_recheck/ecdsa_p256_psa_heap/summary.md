# ecdsa_p256_psa_heap

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T15:44:06 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256_psa_heap: ECDSA P-256, PSA API + Mbed TLS/PSA core + 8 KB Mbed TLS heap |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot |  @ e45b6b1 |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_measure, ecdsa_p256_psa_heap |

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
| total | 364,881,503 | 364,881,503 | 364,881,503 | 0.0 | 2171.91 |
| validate | 361,260,724 | 361,260,724 | 361,260,724 | 0.0 | 2150.36 |
| hash | 1,840,507 | 1,840,507 | 1,840,507 | 0.0 | 10.96 |
| sig | 359,396,060 | 359,396,060 | 359,396,060 | 0.0 | 2139.26 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1600 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.97 | 10.96 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 2148.51 | 10.96 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.09 | 10.96 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_measure | 49572 | 152 | 27196 | 49724 | 27392 | 91 |
| ecdsa_p256_psa_heap | 48860 | 152 | 27131 | 49012 | 27328 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap.build.log`
- `build_logs/boot_ecdsa_p256_psa_heap_measure.build.log`
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
