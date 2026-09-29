# ed25519_psa_fix

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T05:53:56 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519_psa_fix: Ed25519 over SHA-256 image hash, PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_psa_fix_measure, ed25519_psa_fix |

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
| total | 6,702,444 | 6,702,444 | 6,702,444 | 0.0 | 39.90 |
| validate | 2,446,393 | 2,446,393 | 2,446,393 | 0.0 | 14.56 |
| hash | 1,942,074 | 1,942,074 | 1,942,074 | 0.0 | 11.56 |
| sig | 485,024 | 485,024 | 485,024 | 0.0 | 2.89 |

All runs booted: False; results: ['bad_sig']
Main stack peak use (bytes used / size): 1344 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.58 | 11.56 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 14.56 | 11.56 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.67 | 11.56 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_psa_fix_measure | 44216 | 152 | 21052 | 44368 | 21248 | 44 |
| ed25519_psa_fix | 43504 | 152 | 20987 | 43656 | 21184 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_psa_fix.build.log`
- `build_logs/boot_ed25519_psa_fix_measure.build.log`
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
