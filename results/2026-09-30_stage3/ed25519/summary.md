# ed25519

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T05:50:13 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519: Ed25519 over SHA-256 image hash, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_measure, ed25519 |

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
| total | 9,346,396 | 9,346,396 | 9,346,396 | 0.0 | 55.63 |
| validate | 5,724,140 | 5,724,140 | 5,724,140 | 0.0 | 34.07 |
| hash | 1,669,644 | 1,669,644 | 1,669,644 | 0.0 | 9.94 |
| sig | 4,040,420 | 4,040,420 | 4,040,420 | 0.0 | 24.05 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4028 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 33.95 | 9.94 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 10.01 | 9.94 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_measure | 42812 | 132 | 18152 | 42944 | 18304 | 44 |
| ed25519 | 42100 | 132 | 18087 | 42232 | 18240 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519.build.log`
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
