# mldsa87

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:41:58 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | mldsa @ e45b6b1e (dirty) |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_measure, mldsa87 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV MLDSA87 | 4627 |
| TLV area total | 4707 |
| File | 22675 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 14,175,877 | 14,175,877 | 14,175,877 | 0.0 | 84.38 |
| validate | 10,534,636 | 10,534,636 | 10,534,636 | 0.0 | 62.71 |
| hash | 1,822,126 | 1,822,126 | 1,822,126 | 0.0 | 10.85 |
| sig | 8,424,378 | 8,424,378 | 8,424,378 | 0.0 | 50.15 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110112 / 118784

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.86 | 10.85 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 17.42 | 10.85 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 12.35 | 10.85 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure | 39008 | 132 | 126696 | 39144 | 126848 | 2592 |
| mldsa87 | 38288 | 132 | 126631 | 38424 | 126784 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87.build.log`
- `build_logs/boot_mldsa87_measure.build.log`
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
