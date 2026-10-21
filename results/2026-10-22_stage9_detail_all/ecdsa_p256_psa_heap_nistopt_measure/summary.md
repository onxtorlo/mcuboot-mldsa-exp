# ecdsa_p256_psa_heap_nistopt_measure

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:51:56 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_nistopt_measure |

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
| total | 64,457,245 | 64,457,245 | 64,457,245 | 0.0 | 383.67 |
| validate | 60,836,453 | 60,836,453 | 60,836,453 | 0.0 | 362.12 |
| hash | 1,841,351 | 1,841,351 | 1,841,351 | 0.0 | 10.96 |
| sig | 58,970,947 | 58,970,947 | 58,970,947 | 0.0 | 351.02 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1512 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.98 | 10.96 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 362.68 | 10.96 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.10 | 10.96 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_nistopt_measure | 50564 | 152 | 27196 | 50716 | 27392 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap_nistopt_measure.build.log`
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
