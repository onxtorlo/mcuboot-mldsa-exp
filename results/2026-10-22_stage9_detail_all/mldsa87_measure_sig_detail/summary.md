# mldsa87_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:19:43 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_measure_sig_detail |

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
| total | 14,209,337 | 14,209,337 | 14,209,337 | 0.0 | 84.58 |
| validate | 10,566,650 | 10,566,650 | 10,566,650 | 0.0 | 62.90 |
| hash | 1,823,731 | 1,823,731 | 1,823,731 | 0.0 | 10.86 |
| sig | 8,448,038 | 8,448,038 | 8,448,038 | 0.0 | 50.29 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110112 / 118784

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure_sig_detail | 40888 | 132 | 127880 | 41020 | 128064 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87_measure_sig_detail.build.log`
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
