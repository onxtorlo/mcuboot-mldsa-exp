# rsa2048

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:10:35 |
| Board | stm32f429i_disc1 |
| Configuration | rsa2048: RSA-2048, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa2048_measure, rsa2048 |

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
| total | 14,320,091 | 14,320,091 | 14,320,091 | 0.0 | 85.24 |
| validate | 10,677,455 | 10,677,455 | 10,677,455 | 0.0 | 63.56 |
| hash | 1,818,644 | 1,818,644 | 1,818,644 | 0.0 | 10.83 |
| sig | 8,818,448 | 8,818,448 | 8,818,448 | 0.0 | 52.49 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2616 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.84 | 10.83 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 63.09 | 10.83 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.05 | 10.83 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa2048_measure | 37824 | 152 | 33532 | 37976 | 33728 | 270 |
| rsa2048 | 37120 | 152 | 33467 | 37272 | 33664 | 270 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa2048.build.log`
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
