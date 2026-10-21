# ecdsa_p256_measure_sig_detail_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:34:05 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_sig_detail_opt_o3 |

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
| total | 16,875,277 | 16,875,277 | 16,875,277 | 0.0 | 100.45 |
| validate | 13,286,628 | 13,286,628 | 13,286,628 | 0.0 | 79.09 |
| hash | 1,580,309 | 1,580,309 | 1,580,309 | 0.0 | 9.41 |
| sig | 11,689,102 | 11,689,102 | 11,689,102 | 0.0 | 69.58 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1456 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_sig_detail_opt_o3 | 46532 | 132 | 19339 | 46664 | 19520 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_sig_detail_opt_o3.build.log`
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
