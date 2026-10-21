# ecdsa_p256_measure_sig_detail

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T01:46:16 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 (dirty) |
| exp | dev @ a6fca6b |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_sig_detail |

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
| total | 23,401,409 | 23,401,409 | 23,401,409 | 0.0 | 139.29 |
| validate | 19,786,415 | 19,786,415 | 19,786,415 | 0.0 | 117.78 |
| hash | 1,651,101 | 1,651,101 | 1,651,101 | 0.0 | 9.83 |
| sig | 18,114,764 | 18,114,764 | 18,114,764 | 0.0 | 107.83 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1424 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.84 | 9.83 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 117.30 | 9.83 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 9.93 | 9.83 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_sig_detail | 32512 | 132 | 18368 | 32644 | 18496 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_sig_detail.build.log`
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
