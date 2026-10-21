# ed25519_measure_sig_detail_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T04:00:30 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519: Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_measure_sig_detail_opt_o3 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV ED25519 | 64 |
| TLV area total | 144 |
| File | 18112 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 7,394,511 | 7,394,511 | 7,394,511 | 0.0 | 44.01 |
| validate | 3,805,866 | 3,805,866 | 3,805,866 | 0.0 | 22.65 |
| hash | 1,581,153 | 1,581,153 | 1,581,153 | 0.0 | 9.41 |
| sig | 2,212,608 | 2,212,608 | 2,212,608 | 0.0 | 13.17 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4120 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_measure_sig_detail_opt_o3 | 61672 | 132 | 19339 | 61804 | 19520 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_measure_sig_detail_opt_o3.build.log`
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
