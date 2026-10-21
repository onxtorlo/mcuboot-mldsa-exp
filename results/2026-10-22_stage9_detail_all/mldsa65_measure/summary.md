# mldsa65_measure

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:11:40 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_measure |

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
| total | 10,442,677 | 10,442,677 | 10,442,677 | 0.0 | 62.16 |
| validate | 6,823,338 | 6,823,338 | 6,823,338 | 0.0 | 40.62 |
| hash | 1,669,849 | 1,669,849 | 1,669,849 | 0.0 | 9.94 |
| sig | 4,951,334 | 4,951,334 | 4,951,334 | 0.0 | 29.47 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 71680 / 81920

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 14.24 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.99 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_measure | 38616 | 132 | 89832 | 38748 | 89984 | 1952 |

## Files

- `boot_ok.csv`
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
