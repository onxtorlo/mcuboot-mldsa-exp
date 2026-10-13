# rsa3072_psa_heap16k

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-13T16:14:09 |
| Board | stm32f429i_disc1 |
| Configuration | rsa3072_psa_heap16k: RSA-3072, PSA API + 16 KB Mbed TLS heap (default 8 KB is too small: psa_verify_hash -> PSA_ERROR_INSUFFICIENT_MEMORY) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot |  @ e45b6b1 |
| exp | dev @ 53ca9e6 (dirty) |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa3072_psa_heap16k_measure, rsa3072_psa_heap16k |

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
| total | 23,656,481 | 23,656,481 | 23,656,481 | 0.0 | 140.81 |
| validate | 20,041,536 | 20,041,536 | 20,041,536 | 0.0 | 119.29 |
| hash | 1,925,301 | 1,925,301 | 1,925,301 | 0.0 | 11.46 |
| sig | 18,057,803 | 18,057,803 | 18,057,803 | 0.0 | 107.49 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2464 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 11.48 | 11.46 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 118.63 | 11.46 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.79 | 11.46 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa3072_psa_heap16k_measure | 44132 | 152 | 35388 | 44284 | 35584 | 398 |
| rsa3072_psa_heap16k | 43432 | 152 | 35323 | 43584 | 35520 | 398 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa3072_psa_heap16k.build.log`
- `build_logs/boot_rsa3072_psa_heap16k_measure.build.log`
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
