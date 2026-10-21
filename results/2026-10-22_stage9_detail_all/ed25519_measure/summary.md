# ed25519_measure

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:58:39 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519: Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_measure |

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
| total | 9,342,549 | 9,342,549 | 9,342,549 | 0.0 | 55.61 |
| validate | 5,724,664 | 5,724,664 | 5,724,664 | 0.0 | 34.08 |
| hash | 1,670,058 | 1,670,058 | 1,670,058 | 0.0 | 9.94 |
| sig | 4,040,436 | 4,040,436 | 4,040,436 | 0.0 | 24.05 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4028 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 33.95 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.02 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_measure | 42824 | 132 | 18152 | 42960 | 18304 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_measure.build.log`
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
