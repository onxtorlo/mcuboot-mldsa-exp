# mldsa87_measure_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T04:14:06 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_measure_opt_o3 |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV MLDSA87 | 4627 |
| TLV area total | 4707 |
| File | 22675 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 13,409,606 | 13,409,606 | 13,409,606 | 0.0 | 79.82 |
| validate | 9,806,336 | 9,806,336 | 9,806,336 | 0.0 | 58.37 |
| hash | 1,683,643 | 1,683,643 | 1,683,643 | 0.0 | 10.02 |
| sig | 7,869,341 | 7,869,341 | 7,869,341 | 0.0 | 46.84 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110168 / 118784

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.04 | 10.02 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 12.38 | 10.02 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.48 | 10.02 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure_opt_o3 | 48184 | 132 | 126699 | 48316 | 126848 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87_measure_opt_o3.build.log`
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
