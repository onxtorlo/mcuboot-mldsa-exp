# ed25519_sha512

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:04:42 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519_sha512: Ed25519 over SHA-512 image hash, TinyCrypt |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_sha512_measure, ed25519_sha512 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA512 | 64 |
| TLV KEYHASH | 64 |
| TLV ED25519 | 64 |
| TLV area total | 208 |
| File | 18176 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 10,575,496 | 10,575,496 | 10,575,496 | 0.0 | 62.95 |
| validate | 6,959,050 | 6,959,050 | 6,959,050 | 0.0 | 41.42 |
| hash | 2,864,994 | 2,864,994 | 2,864,994 | 0.0 | 17.05 |
| sig | 4,063,598 | 4,063,598 | 4,063,598 | 0.0 | 24.19 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 4060 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 17.07 | 17.05 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 41.36 | 17.05 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 17.22 | 17.05 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_sha512_measure | 41760 | 132 | 18152 | 41896 | 18304 | 44 |
| ed25519_sha512 | 41048 | 132 | 18087 | 41184 | 18240 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_sha512.build.log`
- `build_logs/boot_ed25519_sha512_measure.build.log`
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
