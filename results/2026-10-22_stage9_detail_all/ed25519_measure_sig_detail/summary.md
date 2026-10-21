# ed25519_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:00:10 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519: Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_measure_sig_detail |

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
| total | 9,388,513 | 9,388,513 | 9,388,513 | 0.0 | 55.88 |
| validate | 5,769,164 | 5,769,164 | 5,769,164 | 0.0 | 34.34 |
| hash | 1,671,044 | 1,671,044 | 1,671,044 | 0.0 | 9.95 |
| sig | 4,076,907 | 4,076,907 | 4,076,907 | 0.0 | 24.27 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4052 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_measure_sig_detail | 44844 | 132 | 19336 | 44976 | 19520 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_measure_sig_detail.build.log`
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
