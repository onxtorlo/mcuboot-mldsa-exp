# ed25519_pure_psa_fix

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:01:06 |
| Board | stm32f429i_disc1 |
| Configuration | ed25519_pure_psa_fix: Ed25519 pure (signature over the whole image), PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ed25519_pure_psa_fix_measure, ed25519_pure_psa_fix |

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
| total | 4,261,771 | 4,261,771 | 4,261,771 | 0.0 | 25.37 |
| validate | 5,911 | 5,911 | 5,911 | 0.0 | 0.04 |
| hash | 0 | 0 | 0 | 0.0 | 0.00 |
| sig | 0 | 0 | 0 | 0.0 | 0.00 |

All runs booted: False; results: ['other']
Main stack peak use (bytes used / size): 1344 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | other | False | 0.04 | 0.00 | 0 | reject_bad_payload.log |
| bad_sig | other | False | 0.04 | 0.00 | 0 | reject_bad_sig.log |
| bad_key | other | False | 0.04 | 0.00 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ed25519_pure_psa_fix_measure | 44004 | 152 | 21052 | 44156 | 21248 | 44 |
| ed25519_pure_psa_fix | 43316 | 152 | 20987 | 43468 | 21184 | 44 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ed25519_pure_psa_fix.build.log`
- `build_logs/boot_ed25519_pure_psa_fix_measure.build.log`
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
