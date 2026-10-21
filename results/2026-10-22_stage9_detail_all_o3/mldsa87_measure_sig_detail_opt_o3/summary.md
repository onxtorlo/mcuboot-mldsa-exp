# mldsa87_measure_sig_detail_opt_o3

## Environment

| Item | Value |
|---|---|
| Date | 2026-10-22T04:15:36 |
| Board | stm32f429i_disc1 |
| Configuration | mldsa87: ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| Zephyr | v4.4.2 (dccb0959) |
| MCUboot | sign-replace @ 6a809c68 |
| exp | dev @ 00476a4 |
| Zephyr SDK | 1.0.1 |
| Bootloader builds | mldsa87_measure_sig_detail_opt_o3 |

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
| total | 13,431,093 | 13,431,093 | 13,431,093 | 0.0 | 79.95 |
| validate | 9,827,818 | 9,827,818 | 9,827,818 | 0.0 | 58.50 |
| hash | 1,681,309 | 1,681,309 | 1,681,309 | 0.0 | 10.01 |
| sig | 7,892,556 | 7,892,556 | 7,892,556 | 0.0 | 46.98 |

All runs booted: True; results: ['ok']
Main stack peak use (bytes used / size): 110168 / 118784

## Bootloader size

| Build | text | data | bss | FLASH used | RAM used | public key |
|---|---|---|---|---|---|---|
| mldsa87_measure_sig_detail_opt_o3 | 50880 | 132 | 127883 | 51012 | 128064 | 2592 |

## Files

- `boot_ok.csv`
- `build_logs/boot_mldsa87_measure_sig_detail_opt_o3.build.log`
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
- `meta.json`
