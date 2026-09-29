# rsa3072

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:17:53 |
| Board | stm32f429i_disc1 |
| Configuration | rsa3072: RSA-3072, TF-PSA-Crypto legacy (default for Mbed TLS 4.x) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | rsa3072_measure, rsa3072 |

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
| total | 23,019,704 | 23,019,704 | 23,019,704 | 0.0 | 137.02 |
| validate | 19,342,080 | 19,342,080 | 19,342,080 | 0.0 | 115.13 |
| hash | 1,818,923 | 1,818,923 | 1,818,923 | 0.0 | 10.83 |
| sig | 17,470,170 | 17,470,170 | 17,470,170 | 0.0 | 103.99 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 2872 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.84 | 10.83 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 114.45 | 10.83 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.12 | 10.83 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| rsa3072_measure | 37952 | 152 | 39420 | 38104 | 39616 | 398 |
| rsa3072 | 37252 | 152 | 39355 | 37404 | 39552 | 398 |

## Files

- `boot_ok.csv`
- `build_logs/boot_rsa3072.build.log`
- `build_logs/boot_rsa3072_measure.build.log`
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
