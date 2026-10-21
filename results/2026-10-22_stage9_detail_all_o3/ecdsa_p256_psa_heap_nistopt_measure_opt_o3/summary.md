# ecdsa_p256_psa_heap_nistopt_measure_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T03:43:31 |
| Board | stm32f429i_disc1 |
| Configuration | ecdsa_p256: ECDSA P-256, TinyCrypt (default) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | ecdsa_p256_psa_heap_nistopt_measure_opt_o3 |

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
| total | 40,146,462 | 40,146,462 | 40,146,462 | 0.0 | 238.97 |
| validate | 36,557,818 | 36,557,818 | 36,557,818 | 0.0 | 217.61 |
| hash | 1,042,907 | 1,042,907 | 1,042,907 | 0.0 | 6.21 |
| sig | 35,500,857 | 35,500,857 | 35,500,857 | 0.0 | 211.31 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 1540 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 6.22 | 6.21 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 217.94 | 6.21 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 6.29 | 6.21 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| ecdsa_p256_psa_heap_nistopt_measure_opt_o3 | 66752 | 152 | 27199 | 66904 | 27392 | 91 |

## Files

- `boot_ok.csv`
- `build_logs/boot_ecdsa_p256_psa_heap_nistopt_measure_opt_o3.build.log`
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
