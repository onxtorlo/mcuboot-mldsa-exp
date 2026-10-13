# mldsa87_lowram

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:52:21 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87_lowram: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | mldsa @ e0e92c72 |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_lowram_measure, mldsa87_lowram |

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
| total | 13,562,606 | 13,562,606 | 13,562,606 | 0.0 | 80.73 |
| validate | 9,941,800 | 9,941,800 | 9,941,800 | 0.0 | 59.18 |
| hash | 1,670,653 | 1,670,653 | 1,670,653 | 0.0 | 9.94 |
| sig | 8,005,089 | 8,005,089 | 8,005,089 | 0.0 | 47.65 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 48288 / 57344

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 13.92 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.31 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_lowram_measure | 38532 | 132 | 65256 | 38664 | 65408 | 2592 |
| mldsa87_lowram | 37812 | 132 | 65191 | 37944 | 65344 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87_lowram.build.log`
- `build_logs/boot_mldsa87_lowram_measure.build.log`
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
