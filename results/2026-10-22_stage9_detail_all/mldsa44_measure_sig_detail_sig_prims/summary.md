# mldsa44_measure_sig_detail_sig_prims

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:08:09 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa44: ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa44_measure_sig_detail_sig_prims |

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
| total | 8,330,904 | 8,330,904 | 8,330,904 | 0.0 | 49.59 |
| validate | 4,705,746 | 4,705,746 | 4,705,746 | 0.0 | 28.01 |
| hash | 1,652,451 | 1,652,451 | 1,652,451 | 0.0 | 9.84 |
| sig | 2,907,419 | 2,907,419 | 2,907,419 | 0.0 | 17.31 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 47152 / 57344

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa44_measure_sig_detail_sig_prims | 39800 | 132 | 66440 | 39932 | 66624 | 1312 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa44_measure_sig_detail_sig_prims.build.log`
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
