# ecdsa_p256

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T05:42:59 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_measure, ecdsa_p256 |

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
| total | 22,925,683 | 22,925,683 | 22,925,683 | 0.0 | 136.46 |
| validate | 19,307,839 | 19,307,839 | 19,307,839 | 0.0 | 114.93 |
| hash | 1,651,091 | 1,651,091 | 1,651,091 | 0.0 | 9.83 |
| sig | 17,637,474 | 17,637,474 | 17,637,474 | 0.0 | 104.98 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1400 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.85 | 9.83 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 121.35 | 9.83 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 9.93 | 9.83 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_measure | 31696 | 132 | 18152 | 31828 | 18304 | 91 |
| ecdsa_p256 | 30984 | 132 | 18087 | 31116 | 18240 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256.build.log`
- `build_logs/boot_ecdsa_p256_measure.build.log`
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
