# mldsa44_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:06:40 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa44: ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa44_measure_sig_detail |

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
| total | 8,312,820 | 8,312,820 | 8,312,820 | 0.0 | 49.48 |
| validate | 4,697,869 | 4,697,869 | 4,697,869 | 0.0 | 27.96 |
| hash | 1,650,275 | 1,650,275 | 1,650,275 | 0.0 | 9.82 |
| sig | 2,901,973 | 2,901,973 | 2,901,973 | 0.0 | 17.27 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 47144 / 57344

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa44_measure_sig_detail | 39744 | 132 | 66440 | 39876 | 66624 | 1312 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa44_measure_sig_detail.build.log`
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
