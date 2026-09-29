# rsa3072_psa

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:21:32 |
| Board | stm32f429i_disc1 |
| Configuration | rsa3072_psa: RSA-3072, PSA API |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa3072_psa_measure, rsa3072_psa |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV RSA3072_PSS | 384 |
| TLV area total | 464 |
| File | 18432 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 6,387,532 | 6,387,532 | 6,387,532 | 0.0 | 38.02 |
| validate | 2,158,452 | 2,158,452 | 2,158,452 | 0.0 | 12.85 |
| hash | 1,925,262 | 1,925,262 | 1,925,262 | 0.0 | 11.46 |
| sig | 174,847 | 174,847 | 174,847 | 0.0 | 1.04 |

All runs booted: False; results: ['bad_sig']
Main stack peak use (bytes used / size): 2376 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.48 | 11.46 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 12.85 | 11.46 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.79 | 11.46 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa3072_psa_measure | 44140 | 152 | 27196 | 44292 | 27392 | 398 |
| rsa3072_psa | 43440 | 152 | 27131 | 43592 | 27328 | 398 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa3072_psa.build.log`
- `build_logs/boot_rsa3072_psa_measure.build.log`
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
