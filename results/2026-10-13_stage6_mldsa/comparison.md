# 2026-10-13_stage6_mldsa: signature comparison

Valid image, mean of all runs (stdev in cycles). ms at 168 MHz.

## Verification time (configurations that boot a valid image)

| Configuration | sig ms | hash ms | validate ms | total ms | sig stdev (cyc) | valid image |
|---|---|---|---|---|---|---|
| mldsa44 | 17.26 | 9.844 | 27.921 | 49.474 | 0.0 | booted 10/10 |
| mldsa44_lowram | 17.039 | 9.953 | 27.826 | 49.395 | 0.0 | booted 10/10 |
| mldsa65 | 29.479 | 9.94 | 40.613 | 62.157 | 0.0 | booted 10/10 |
| mldsa65_lowram | 28.286 | 9.94 | 39.419 | 60.937 | 0.0 | booted 10/10 |
| mldsa87 | 50.145 | 10.846 | 62.706 | 84.38 | 0.0 | booted 10/10 |
| mldsa87_lowram | 47.649 | 9.944 | 59.177 | 80.73 | 0.0 | booted 10/10 |

## Size and memory

| Configuration | MCUboot FLASH (B) | MCUboot RAM (B) | stack peak (B) | public key (B) | signature (B) | TLV area (B) | works |
|---|---|---|---|---|---|---|---|
| mldsa44 | 37288 | 65344 | 47144 | 1312 | 2420 | 2500 | yes |
| mldsa44_lowram | 36824 | 44864 | 27304 | 1312 | 2420 | 2500 | yes |
| mldsa65 | 38032 | 89920 | 71680 | 1952 | 3309 | 3389 | yes |
| mldsa65_lowram | 37264 | 53056 | 36480 | 1952 | 3309 | 3389 | yes |
| mldsa87 | 38424 | 126784 | 110112 | 2592 | 4627 | 4707 | yes |
| mldsa87_lowram | 37944 | 65344 | 48288 | 2592 | 4627 | 4707 | yes |

MCUboot FLASH/RAM: build without measurement. Stack peak: measurement build (for configurations that do not work it is the peak up to the failure).

## Rejection tests

| Configuration | bad payload | bad signature | wrong key |
|---|---|---|---|
| mldsa44 | hash_mismatch | bad_sig | no_key |
| mldsa44_lowram | hash_mismatch | bad_sig | no_key |
| mldsa65 | hash_mismatch | bad_sig | no_key |
| mldsa65_lowram | hash_mismatch | bad_sig | no_key |
| mldsa87 | hash_mismatch | bad_sig | no_key |
| mldsa87_lowram | hash_mismatch | bad_sig | no_key |

## Configurations

| Configuration | Description |
|---|---|
| mldsa44 | ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C) |
| mldsa44_lowram | ML-DSA-44 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
| mldsa65 | ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C) |
| mldsa65_lowram | ML-DSA-65 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
| mldsa87 | ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C) |
| mldsa87_lowram | ML-DSA-87 over SHA-256 image hash, mldsa-native (portable C), MLD_CONFIG_REDUCE_RAM |
