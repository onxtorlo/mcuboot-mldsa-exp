# 2026-09-30_stage2_rsa2048

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T04:12:56 |
| Board | stm32f429i_disc1 |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 155e48c2 |
| exp | dev @ bbc09b6 |
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
| total | 14,311,303 | 14,311,303 | 14,311,303 | 0.0 | 85.19 |
| validate | 10,674,486 | 10,674,486 | 10,674,486 | 0.0 | 63.54 |
| hash | 1,818,252 | 1,818,252 | 1,818,252 | 0.0 | 10.82 |
| sig | 8,815,930 | 8,815,930 | 8,815,930 | 0.0 | 52.48 |

All runs booted: True; results: ['ok']

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 10.84 | 10.82 | 0 | reject_bad_payload.log |
| bad_sig | bad_sig | False | 63.07 | 10.82 | 1 | reject_bad_sig.log |
| bad_key | no_key | False | 11.05 | 10.82 | 0 | reject_bad_key.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used |
|---|---|---|---|---|---|
| rsa2048_measure | 37684 | 152 | 33532 | 37836 | 33728 |
| rsa2048 | 37120 | 152 | 33467 | 37272 | 33664 |

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
