# ed25519_pure_sha512

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T15:54:38 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519_pure_sha512: Ed25519 pure (signature over the whole image), TinyCrypt, SHA-512 |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot |  @ e45b6b1 |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_pure_sha512_measure, ed25519_pure_sha512 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA512 | 64 |
| TLV SIG_PURE | 1 |
| TLV KEYHASH | 64 |
| TLV ED25519 | 64 |
| TLV area total | 213 |
| File | 18181 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 10,442,550 | 10,442,550 | 10,442,550 | 0.0 | 62.16 |
| validate | 6,824,663 | 6,824,663 | 6,824,663 | 0.0 | 40.62 |
| hash | 0 | 0 | 0 | 0.0 | 0.00 |
| sig | 6,793,285 | 6,793,285 | 6,793,285 | 0.0 | 40.44 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 3988 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | bad_sig | False | 40.82 | 0.00 | 1 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 40.62 | 0.00 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 0.18 | 0.00 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_pure_sha512_measure | 41580 | 132 | 18152 | 41712 | 18304 | 44 |
| ed25519_pure_sha512 | 40892 | 132 | 18087 | 41024 | 18240 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_pure_sha512.build.log`
- `build_logs/boot_ed25519_pure_sha512_measure.build.log`
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
