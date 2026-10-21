
### ecdsa_p256_psa_heap_measure_sig_detail.pre_fix (10 runs)

sig stage: 371,045,868 cyc = 2208.606 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 279,707 | 1.665 | 0.1 | 279,707 | 0.0 |
| psa.verify_hash | 1 | 370,764,566 | 2206.932 | 99.9 | 370,764,566 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 3,590,882 | 21.374 | 1.0 | 3,590,882 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 165,115 | 0.983 | 0.0 | 165,115 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 93,175,554 | 554.616 | 25.1 | 93,175,554 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 269,036,850 | 1601.410 | 72.5 | 269,036,850 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 4,496,640 | 26.766 | 1.2 | 4,496,640 | 0.0 |
| mbecdsa.verify.final | 1 | 997 | 0.006 | 0.0 | 997 | 0.0 |
| (rest of sig) | | 1,595 | 0.009 | 0.0 | | |


### ecdsa_p256_psa_heap_nistopt_measure_sig_detail.pre_fix (10 runs)

sig stage: 60,659,741 cyc = 361.070 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 37,479 | 0.223 | 0.1 | 37,479 | 0.0 |
| psa.verify_hash | 1 | 60,620,664 | 360.837 | 99.9 | 60,620,664 | 0.0 |
| mbecdsa.verify | 1 | 60,580,641 | 360.599 | 99.9 | 60,580,641 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 3,590,841 | 21.374 | 5.9 | 3,590,841 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 164,941 | 0.982 | 0.3 | 164,941 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 13,701,648 | 81.557 | 22.6 | 13,701,648 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 39,390,203 | 234.465 | 64.9 | 39,390,203 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 3,714,842 | 22.112 | 6.1 | 3,714,842 | 0.0 |
| mbecdsa.verify.final | 1 | 1,024 | 0.006 | 0.0 | 1,024 | 0.0 |
| (rest of sig) | | 1,598 | 0.010 | 0.0 | | |


## sig stage per build (instrumentation cost)

| build | runs | sig cycles | sig ms | stdev cyc |
|---|---|---|---|---|
| ecdsa_p256_psa_heap_measure_sig_detail.pre_fix | 10 | 371,045,868 | 2208.606 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure_sig_detail.pre_fix | 10 | 60,659,741 | 361.070 | 0.0 |
