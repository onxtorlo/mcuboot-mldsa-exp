# mldsa44_lowram

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:45:25 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa44_lowram: ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | mldsa @ e45b6b1e (dirty) |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa44_lowram_measure, mldsa44_lowram |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV MLDSA44 | 2420 |
| TLV area total | 2500 |
| File | 20468 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 8,298,411 | 8,298,411 | 8,298,411 | 0.0 | 49.40 |
| validate | 4,674,687 | 4,674,687 | 4,674,687 | 0.0 | 27.83 |
| hash | 1,672,043 | 1,672,043 | 1,672,043 | 0.0 | 9.95 |
| sig | 2,862,593 | 2,862,593 | 2,862,593 | 0.0 | 17.04 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 27304 / 36864

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.97 | 9.95 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 12.10 | 9.95 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.68 | 9.95 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa44_lowram_measure | 37392 | 132 | 44776 | 37528 | 44928 | 1312 |
| mldsa44_lowram | 36688 | 132 | 44711 | 36824 | 44864 | 1312 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa44_lowram.build.log`
- `build_logs/boot_mldsa44_lowram_measure.build.log`
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
