# ecdsa_p256_measure_sig_detail_opt_lto

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:14:10 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 (dirty) |
| exp | dev @ a6fca6b (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_sig_detail_opt_lto |

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
| total | 23,437,386 | 23,437,386 | 23,437,386 | 0.0 | 139.51 |
| validate | 19,830,067 | 19,830,067 | 19,830,067 | 0.0 | 118.04 |
| hash | 1,699,160 | 1,699,160 | 1,699,160 | 0.0 | 10.11 |
| sig | 18,104,178 | 18,104,178 | 18,104,178 | 0.0 | 107.76 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1240 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_sig_detail_opt_lto | 24456 | 5468 | 19327 | 28716 | 18496 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_sig_detail_opt_lto.build.log`
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
