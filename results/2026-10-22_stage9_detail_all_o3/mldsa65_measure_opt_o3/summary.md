# mldsa65_measure_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T04:09:04 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_measure_opt_o3 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV MLDSA65 | 3309 |
| TLV area total | 3389 |
| File | 21357 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 9,937,934 | 9,937,934 | 9,937,934 | 0.0 | 59.15 |
| validate | 6,346,349 | 6,346,349 | 6,346,349 | 0.0 | 37.78 |
| hash | 1,579,298 | 1,579,298 | 1,579,298 | 0.0 | 9.40 |
| sig | 4,587,861 | 4,587,861 | 4,587,861 | 0.0 | 27.31 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 71720 / 81920

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.42 | 9.40 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 11.02 | 9.40 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.44 | 9.40 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_measure_opt_o3 | 47840 | 132 | 89835 | 47972 | 89984 | 1952 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa65_measure_opt_o3.build.log`
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
