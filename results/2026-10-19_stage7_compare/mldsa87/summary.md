# mldsa87

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-19T02:48:09 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 |
| exp | dev @ 58f0823 |
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
| total | 14,175,831 | 14,175,831 | 14,175,831 | 0.0 | 84.38 |
| validate | 10,534,594 | 10,534,594 | 10,534,594 | 0.0 | 62.71 |
| hash | 1,823,727 | 1,823,727 | 1,823,727 | 0.0 | 10.86 |
| sig | 8,424,283 | 8,424,283 | 8,424,283 | 0.0 | 50.14 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110112 / 118784

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.87 | 10.86 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 17.41 | 10.86 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 12.35 | 10.86 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure | 39020 | 132 | 126696 | 39156 | 126848 | 2592 |
| mldsa87 | 38300 | 132 | 126631 | 38436 | 126784 | 2592 |

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
