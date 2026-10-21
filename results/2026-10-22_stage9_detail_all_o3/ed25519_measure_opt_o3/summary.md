# ed25519_measure_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:58:58 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519: Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_measure_opt_o3 |

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
| total | 7,424,545 | 7,424,545 | 7,424,545 | 0.0 | 44.19 |
| validate | 3,831,541 | 3,831,541 | 3,831,541 | 0.0 | 22.81 |
| hash | 1,580,216 | 1,580,216 | 1,580,216 | 0.0 | 9.41 |
| sig | 2,240,224 | 2,240,224 | 2,240,224 | 0.0 | 13.33 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4104 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.42 | 9.41 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 22.74 | 9.41 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 9.47 | 9.41 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_measure_opt_o3 | 58632 | 132 | 18155 | 58764 | 18304 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_measure_opt_o3.build.log`
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
