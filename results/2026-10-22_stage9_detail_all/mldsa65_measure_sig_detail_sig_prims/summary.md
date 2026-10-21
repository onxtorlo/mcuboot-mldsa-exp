# mldsa65_measure_sig_detail_sig_prims

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:14:40 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa65: ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa65_measure_sig_detail_sig_prims |

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
| total | 10,468,255 | 10,468,255 | 10,468,255 | 0.0 | 62.31 |
| validate | 6,847,429 | 6,847,429 | 6,847,429 | 0.0 | 40.76 |
| hash | 1,670,647 | 1,670,647 | 1,670,647 | 0.0 | 9.94 |
| sig | 4,966,230 | 4,966,230 | 4,966,230 | 0.0 | 29.56 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 71672 / 81920

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa65_measure_sig_detail_sig_prims | 40564 | 132 | 91016 | 40700 | 91200 | 1952 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa65_measure_sig_detail_sig_prims.build.log`
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
