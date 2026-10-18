# mldsa44

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-19T02:41:02 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa44: ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 |
| exp | dev @ 58f0823 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa44_measure, mldsa44 |

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
| total | 8,312,091 | 8,312,091 | 8,312,091 | 0.0 | 49.48 |
| validate | 4,691,299 | 4,691,299 | 4,691,299 | 0.0 | 27.92 |
| hash | 1,653,840 | 1,653,840 | 1,653,840 | 0.0 | 9.84 |
| sig | 2,898,689 | 2,898,689 | 2,898,689 | 0.0 | 17.25 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 47144 / 57344

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.86 | 9.84 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 12.39 | 9.84 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.57 | 9.84 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa44_measure | 37872 | 132 | 65256 | 38004 | 65408 | 1312 |
| mldsa44 | 37168 | 132 | 65191 | 37300 | 65344 | 1312 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa44.build.log`
- `build_logs/boot_mldsa44_measure.build.log`
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
