# rsa2048_measure

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T02:29:12 |
| Board | stm32f429i_disc1 |
| Configuration | rsa2048: RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ b4fb053 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa2048_measure |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV KEYHASH | 32 |
| TLV RSA2048_PSS | 256 |
| TLV area total | 336 |
| File | 18304 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 14,312,825 | 14,312,825 | 14,312,825 | 0.0 | 85.20 |
| validate | 10,676,021 | 10,676,021 | 10,676,021 | 0.0 | 63.55 |
| hash | 1,818,213 | 1,818,213 | 1,818,213 | 0.0 | 10.82 |
| sig | 8,817,441 | 8,817,441 | 8,817,441 | 0.0 | 52.48 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2616 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.84 | 10.82 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 63.08 | 10.82 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.05 | 10.82 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa2048_measure | 37832 | 152 | 33532 | 37984 | 33728 | 270 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa2048_measure.build.log`
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
