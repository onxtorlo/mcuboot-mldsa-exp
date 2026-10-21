# ecdsa_p256_psa_heap_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:46:15 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_measure_sig_detail |

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
| total | 376,635,882 | 376,635,882 | 376,635,882 | 0.0 | 2241.88 |
| validate | 373,020,926 | 373,020,926 | 373,020,926 | 0.0 | 2220.36 |
| hash | 1,941,145 | 1,941,145 | 1,941,145 | 0.0 | 11.55 |
| sig | 371,045,868 | 371,045,868 | 371,045,868 | 0.0 | 2208.61 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1576 / 10240

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_measure_sig_detail | 51744 | 152 | 28380 | 51896 | 28544 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap_measure_sig_detail.build.log`
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
