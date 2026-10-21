# ecdsa_p256_measure_opt_o2

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T01:58:54 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e0e92c72 (dirty) |
| exp | dev @ a6fca6b (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure_opt_o2 |

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
| total | 19,448,306 | 19,448,306 | 19,448,306 | 0.0 | 115.76 |
| validate | 15,852,394 | 15,852,394 | 15,852,394 | 0.0 | 94.36 |
| hash | 1,480,436 | 1,480,436 | 1,480,436 | 0.0 | 8.81 |
| sig | 14,356,092 | 14,356,092 | 14,356,092 | 0.0 | 85.45 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1440 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 8.83 | 8.81 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 94.00 | 8.81 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 8.90 | 8.81 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure_opt_o2 | 38120 | 132 | 18155 | 38252 | 18304 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_measure_opt_o2.build.log`
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
