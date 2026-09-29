# none

## Environment

| Item | Value |
|---|---|
| Date | 2026-09-30T06:06:54 |
| Board | stm32f429i_disc1 |
| Configuration | none: No signature: SHA-256 hash check only (TinyCrypt) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ e45b6b1e |
| exp | dev @ 124d1cd |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | none_measure, none |

## Signed image

| Part | Bytes |
|---|---|
| Header | 512 |
| Payload | 17456 |
| TLV SHA256 | 32 |
| TLV area total | 40 |
| File | 18008 |

## Boot timing (valid image, 10 runs, 168 MHz)

| Stage | mean cycles | min | max | stdev | mean ms |
|---|---|---|---|---|---|
| total | 5,289,985 | 5,289,985 | 5,289,985 | 0.0 | 31.49 |
| validate | 1,673,540 | 1,673,540 | 1,673,540 | 0.0 | 9.96 |
| hash | 1,670,229 | 1,670,229 | 1,670,229 | 0.0 | 9.94 |
| sig | 0 | 0 | 0 | 0.0 | 0.00 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 680 / 10240

## Rejection tests

| Case | result | booted | validate ms | hash ms | sig run | log |
|---|---|---|---|---|---|---|
| bad_payload | hash_mismatch | False | 9.96 | 9.94 | 0 | reject_bad_payload.log |

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| none_measure | 26996 | 132 | 18152 | 27128 | 18304 |  |
| none | 26324 | 132 | 18087 | 26456 | 18240 |  |

## Files

- `boot_ok.csv`
- `build_logs/boot_none.build.log`
- `build_logs/boot_none_measure.build.log`
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
- `logs/reject_bad_payload.log`
- `meta.json`
- `reject.csv`
