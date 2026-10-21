# mldsa65_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:13:10 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_measure_sig_detail |

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
| total | 10,447,220 | 10,447,220 | 10,447,220 | 0.0 | 62.19 |
| validate | 6,822,043 | 6,822,043 | 6,822,043 | 0.0 | 40.61 |
| hash | 1,670,655 | 1,670,655 | 1,670,655 | 0.0 | 9.94 |
| sig | 4,940,810 | 4,940,810 | 4,940,810 | 0.0 | 29.41 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 71680 / 81920

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_measure_sig_detail | 40488 | 132 | 91016 | 40620 | 91200 | 1952 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa65_measure_sig_detail.build.log`
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
- `meta.json`
