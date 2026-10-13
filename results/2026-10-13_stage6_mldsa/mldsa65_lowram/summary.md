# mldsa65_lowram

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:48:53 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65_lowram: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | mldsa @ e45b6b1e (dirty) |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_lowram_measure, mldsa65_lowram |

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
| total | 10,237,430 | 10,237,430 | 10,237,430 | 0.0 | 60.94 |
| validate | 6,622,475 | 6,622,475 | 6,622,475 | 0.0 | 39.42 |
| hash | 1,669,852 | 1,669,852 | 1,669,852 | 0.0 | 9.94 |
| sig | 4,752,092 | 4,752,092 | 4,752,092 | 0.0 | 28.29 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 36480 / 45056

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 12.92 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.98 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_lowram_measure | 37832 | 132 | 52968 | 37968 | 53120 | 1952 |
| mldsa65_lowram | 37128 | 132 | 52903 | 37264 | 53056 | 1952 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa65_lowram.build.log`
- `build_logs/boot_mldsa65_lowram_measure.build.log`
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
