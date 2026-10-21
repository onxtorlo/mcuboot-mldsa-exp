# ecdsa_p256_measure_sig_detail_opt_o2

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:00:26 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 (dirty) |
| exp | dev @ a6fca6b (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_sig_detail_opt_o2 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV ECDSA_SIG | 71 |
| TLV area total | 151 |
| File | 18119 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 19,502,999 | 19,502,999 | 19,502,999 | 0.0 | 116.09 |
| validate | 15,904,148 | 15,904,148 | 15,904,148 | 0.0 | 94.67 |
| hash | 1,480,803 | 1,480,803 | 1,480,803 | 0.0 | 8.81 |
| sig | 14,407,159 | 14,407,159 | 14,407,159 | 0.0 | 85.76 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1464 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_sig_detail_opt_o2 | 39140 | 132 | 18371 | 39272 | 18496 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_sig_detail_opt_o2.build.log`
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
