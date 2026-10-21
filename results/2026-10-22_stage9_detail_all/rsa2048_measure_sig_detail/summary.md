# rsa2048_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:30:53 |
| Board | stm32f429i_disc1 |
| Configuration | rsa2048: RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa2048_measure_sig_detail |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV RSA2048_PSS | 256 |
| TLV area total | 336 |
| File | 18304 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 14,253,528 | 14,253,528 | 14,253,528 | 0.0 | 84.84 |
| validate | 10,616,716 | 10,616,716 | 10,616,716 | 0.0 | 63.19 |
| hash | 1,818,478 | 1,818,478 | 1,818,478 | 0.0 | 10.82 |
| sig | 8,750,723 | 8,750,723 | 8,750,723 | 0.0 | 52.09 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2616 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa2048_measure_sig_detail | 39796 | 152 | 34716 | 39948 | 34880 | 270 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa2048_measure_sig_detail.build.log`
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
