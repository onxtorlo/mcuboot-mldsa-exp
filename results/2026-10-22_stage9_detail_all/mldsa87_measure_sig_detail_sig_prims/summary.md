# mldsa87_measure_sig_detail_sig_prims

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:21:14 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_measure_sig_detail_sig_prims |

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
| total | 14,223,385 | 14,223,385 | 14,223,385 | 0.0 | 84.66 |
| validate | 10,580,719 | 10,580,719 | 10,580,719 | 0.0 | 62.98 |
| hash | 1,823,699 | 1,823,699 | 1,823,699 | 0.0 | 10.86 |
| sig | 8,462,088 | 8,462,088 | 8,462,088 | 0.0 | 50.37 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110112 / 118784

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure_sig_detail_sig_prims | 40952 | 132 | 127880 | 41084 | 128064 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87_measure_sig_detail_sig_prims.build.log`
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
