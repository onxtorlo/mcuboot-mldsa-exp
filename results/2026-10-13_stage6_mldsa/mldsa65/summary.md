# mldsa65

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:38:31 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | mldsa @ e45b6b1e (dirty) |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_measure, mldsa65 |

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
| total | 10,442,345 | 10,442,345 | 10,442,345 | 0.0 | 62.16 |
| validate | 6,823,004 | 6,823,004 | 6,823,004 | 0.0 | 40.61 |
| hash | 1,669,849 | 1,669,849 | 1,669,849 | 0.0 | 9.94 |
| sig | 4,952,534 | 4,952,534 | 4,952,534 | 0.0 | 29.48 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 71680 / 81920

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 14.24 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.98 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_measure | 38604 | 132 | 89832 | 38736 | 89984 | 1952 |
| mldsa65 | 37900 | 132 | 89767 | 38032 | 89920 | 1952 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa65.build.log`
- `build_logs/boot_mldsa65_measure.build.log`
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
