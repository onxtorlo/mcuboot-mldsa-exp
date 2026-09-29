# ecdsa_p256_psa_fix

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T05:46:30 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256_psa_fix: ECDSA P-256, PSA API + config workaround (enable Mbed TLS/PSA core explicitly) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_fix_measure, ecdsa_p256_psa_fix |

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
| total | 6,199,452 | 6,199,452 | 6,199,452 | 0.0 | 36.90 |
| validate | 1,968,140 | 1,968,140 | 1,968,140 | 0.0 | 11.72 |
| hash | 1,941,731 | 1,941,731 | 1,941,731 | 0.0 | 11.56 |
| sig | 869 | 869 | 869 | 0.0 | 0.01 |

All runs booted: False; results: ['bad_sig']
Main stack peak use (bytes used / size): 1152 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.57 | 11.56 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 11.72 | 11.56 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.70 | 11.56 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_fix_measure | 48584 | 148 | 20008 | 48732 | 20160 | 91 |
| ecdsa_p256_psa_fix | 47872 | 148 | 19943 | 48020 | 20096 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_fix.build.log`
- `build_logs/boot_ecdsa_p256_psa_fix_measure.build.log`
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
