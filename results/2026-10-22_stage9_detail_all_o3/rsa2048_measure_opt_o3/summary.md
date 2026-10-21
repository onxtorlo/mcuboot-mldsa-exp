# rsa2048_measure_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:48:41 |
| Board | stm32f429i_disc1 |
| Configuration | rsa2048: RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa2048_measure_opt_o3 |

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
| total | 11,033,022 | 11,033,022 | 11,033,022 | 0.0 | 65.67 |
| validate | 7,444,369 | 7,444,369 | 7,444,369 | 0.0 | 44.31 |
| hash | 1,033,996 | 1,033,996 | 1,033,996 | 0.0 | 6.15 |
| sig | 6,386,688 | 6,386,688 | 6,386,688 | 0.0 | 38.02 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2640 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 6.17 | 6.15 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 44.06 | 6.15 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 6.29 | 6.15 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa2048_measure_opt_o3 | 48008 | 152 | 33535 | 48160 | 33728 | 270 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa2048_measure_opt_o3.build.log`
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
- `logs/reject_bad_key.log`
- `logs/reject_bad_payload.log`
- `logs/reject_bad_sig.log`
- `meta.json`
- `reject.csv`
