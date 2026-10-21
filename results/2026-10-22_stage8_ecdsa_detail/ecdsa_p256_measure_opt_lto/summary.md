# ecdsa_p256_measure_opt_lto

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:12:23 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 (dirty) |
| exp | dev @ a6fca6b (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_opt_lto |

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
| total | 23,388,500 | 23,388,500 | 23,388,500 | 0.0 | 139.22 |
| validate | 19,773,900 | 19,773,900 | 19,773,900 | 0.0 | 117.70 |
| hash | 1,701,796 | 1,701,796 | 1,701,796 | 0.0 | 10.13 |
| sig | 18,053,671 | 18,053,671 | 18,053,671 | 0.0 | 107.46 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1256 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.14 | 10.13 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 117.22 | 10.13 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.23 | 10.13 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_opt_lto | 24096 | 3900 | 18143 | 27996 | 18304 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_opt_lto.build.log`
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
