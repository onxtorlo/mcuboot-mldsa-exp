# ecdsa_p256_psa_heap_measure

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:44:14 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_measure |

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
| total | 376,453,353 | 376,453,353 | 376,453,353 | 0.0 | 2240.79 |
| validate | 372,831,098 | 372,831,098 | 372,831,098 | 0.0 | 2219.23 |
| hash | 1,941,887 | 1,941,887 | 1,941,887 | 0.0 | 11.56 |
| sig | 370,863,606 | 370,863,606 | 370,863,606 | 0.0 | 2207.52 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1568 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.58 | 11.56 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 2217.04 | 11.56 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.70 | 11.56 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_measure | 49584 | 152 | 27196 | 49736 | 27392 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap_measure.build.log`
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
