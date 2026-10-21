
### ecdsa_p256_measure (10 runs)

sig stage: 18,150,957 cyc = 108.041 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail (10 runs)

sig stage: 18,145,740 cyc = 108.010 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 769 | 0.005 | 0.0 | 769 | 0.0 |
| ecdsa.sig_decode | 1 | 456 | 0.003 | 0.0 | 456 | 0.0 |
| ecdsa.verify | 1 | 18,144,154 | 108.001 | 100.0 | 18,144,154 | 0.0 |
| ecdsa.verify.load | 1 | 3,372 | 0.020 | 0.0 | 3,372 | 0.0 |
| ecdsa.verify.inv_s | 1 | 226,015 | 1.345 | 1.2 | 226,015 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 331,689 | 1.974 | 1.8 | 331,689 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 268,403 | 1.598 | 1.5 | 268,403 | 0.0 |
| ecdsa.verify.loop | 1 | 17,073,614 | 101.629 | 94.1 | 17,073,614 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 8,502,082 | 50.608 | 46.9 | 33,341 | 0.0 |
| ecdsa.verify.loop.add | 195 | 8,530,745 | 50.778 | 47.0 | 43,747 | 0.0 |
| ecdsa.verify.final | 1 | 240,766 | 1.433 | 1.3 | 240,766 | 0.0 |
| (rest of sig) | | 361 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_sig_detail_sig_prims (10 runs)

sig stage: 19,324,694 cyc = 115.028 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 788 | 0.005 | 0.0 | 788 | 0.0 |
| ecdsa.sig_decode | 1 | 451 | 0.003 | 0.0 | 451 | 0.0 |
| ecdsa.verify | 1 | 19,323,111 | 115.019 | 100.0 | 19,323,111 | 0.0 |
| ecdsa.verify.load | 1 | 3,333 | 0.020 | 0.0 | 3,333 | 0.0 |
| ecdsa.verify.inv_s | 1 | 226,886 | 1.351 | 1.2 | 226,886 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 336,973 | 2.006 | 1.7 | 336,973 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 272,036 | 1.619 | 1.4 | 272,036 | 0.0 |
| ecdsa.verify.loop | 1 | 18,241,125 | 108.578 | 94.4 | 18,241,125 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 9,059,120 | 53.923 | 46.9 | 35,526 | 0.0 |
| ecdsa.verify.loop.add | 195 | 9,142,602 | 54.420 | 47.3 | 46,885 | 0.0 |
| ecdsa.verify.final | 1 | 242,451 | 1.443 | 1.3 | 242,451 | 0.0 |
| tc.vli_mult | 4201 | 6,537,774 | 38.915 | 33.8 | 1,556 | 0.0 |
| tc.mmod_fast | 4199 | 9,575,204 | 56.995 | 49.5 | 2,280 | 0.0 |
| tc.mmod | 2 | 332,586 | 1.980 | 1.7 | 166,293 | 0.0 |
| tc.modinv | 3 | 682,113 | 4.060 | 3.5 | 227,371 | 0.0 |
| tc.double_jacobian | 255 | 8,992,743 | 53.528 | 46.5 | 35,266 | 0.0 |
| tc.xycz_add | 196 | 5,137,971 | 30.583 | 26.6 | 26,214 | 0.0 |
| tc.apply_z | 197 | 3,134,000 | 18.655 | 16.2 | 15,909 | 0.0 |
| (rest of sig) | | 344 | 0.002 | 0.0 | | |


### ecdsa_p256_psa_heap_measure (10 runs)

sig stage: 370,863,606 cyc = 2207.521 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_psa_heap_measure_sig_detail (10 runs)

sig stage: 358,836,011 cyc = 2135.929 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 269,757 | 1.606 | 0.1 | 269,757 | 0.0 |
| psa.verify_hash | 1 | 358,564,804 | 2134.314 | 99.9 | 358,564,804 | 0.0 |
| mbecdsa.verify | 1 | 358,292,863 | 2132.696 | 99.8 | 358,292,863 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 3,463,502 | 20.616 | 1.0 | 3,463,502 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 159,530 | 0.950 | 0.0 | 159,530 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 90,122,330 | 536.442 | 25.1 | 90,122,330 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 260,193,123 | 1548.769 | 72.5 | 260,193,123 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 4,338,535 | 25.825 | 1.2 | 4,338,535 | 0.0 |
| mbecdsa.verify.final | 1 | 995 | 0.006 | 0.0 | 995 | 0.0 |
| (rest of sig) | | 1,450 | 0.009 | 0.0 | | |


### ecdsa_p256_psa_heap_measure_sig_detail_sig_prims (10 runs)

sig stage: 371,536,797 cyc = 2211.529 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 280,072 | 1.667 | 0.1 | 280,072 | 0.0 |
| psa.verify_hash | 1 | 371,255,121 | 2209.852 | 99.9 | 371,255,121 | 0.0 |
| mbecdsa.verify | 1 | 370,972,604 | 2208.170 | 99.8 | 370,972,604 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 3,578,230 | 21.299 | 1.0 | 3,578,230 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 164,825 | 0.981 | 0.0 | 164,825 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 93,299,930 | 555.357 | 25.1 | 93,299,930 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 269,424,746 | 1603.719 | 72.5 | 269,424,746 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 4,487,431 | 26.711 | 1.2 | 4,487,431 | 0.0 |
| mbecdsa.verify.final | 1 | 1,079 | 0.006 | 0.0 | 1,079 | 0.0 |
| mpi.mul_mpi | 3918 | 14,534,001 | 86.512 | 3.9 | 3,710 | 0.0 |
| mpi.mod_mpi | 3919 | 322,053,116 | 1916.983 | 86.7 | 82,177 | 0.0 |
| mpi.inv_mod | 6 | 21,469,447 | 127.794 | 5.8 | 3,578,241 | 0.0 |
| ecp.mul_mod | 3916 | 337,644,633 | 2009.789 | 90.9 | 86,222 | 0.0 |
| ecp.modp | 3916 | 322,449,213 | 1919.341 | 86.8 | 82,341 | 0.0 |
| ecp.double_jac | 308 | 221,159,053 | 1316.423 | 59.5 | 718,049 | 0.0 |
| ecp.add_mixed | 124 | 119,625,720 | 712.058 | 32.2 | 964,724 | 0.0 |
| ecp.normalize | 5 | 24,653,263 | 146.746 | 6.6 | 4,930,653 | 0.0 |
| ecp.precompute_comb | 1 | 156,132,844 | 929.362 | 42.0 | 156,132,844 | 0.0 |
| (rest of sig) | | 1,604 | 0.010 | 0.0 | | |


### ecdsa_p256_psa_heap_nistopt_measure (10 runs)

sig stage: 58,970,947 cyc = 351.018 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_psa_heap_nistopt_measure_sig_detail (10 runs)

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


### ecdsa_p256_psa_heap_nistopt_measure_sig_detail_sig_prims (9 runs)

incomplete log, not counted: boot_ok_run01.log

sig stage: 60,044,399 cyc = 357.407 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 36,262 | 0.216 | 0.1 | 36,262 | 0.0 |
| psa.verify_hash | 1 | 60,006,674 | 357.183 | 99.9 | 60,006,674 | 0.0 |
| mbecdsa.verify | 1 | 59,968,325 | 356.954 | 99.9 | 59,968,325 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 3,463,563 | 20.616 | 5.8 | 3,463,563 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 159,284 | 0.948 | 0.3 | 159,284 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 13,612,287 | 81.026 | 22.7 | 13,612,287 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 39,129,136 | 232.912 | 65.2 | 39,129,136 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 3,587,428 | 21.354 | 6.0 | 3,587,428 | 0.0 |
| mbecdsa.verify.final | 1 | 1,105 | 0.007 | 0.0 | 1,105 | 0.0 |
| mpi.mul_mpi | 3918 | 14,180,673 | 84.409 | 23.6 | 3,619 | 0.0 |
| mpi.mod_mpi | 3 | 152,506 | 0.908 | 0.3 | 50,835 | 0.0 |
| mpi.inv_mod | 6 | 20,781,933 | 123.702 | 34.6 | 3,463,656 | 0.0 |
| ecp.mul_mod | 3916 | 26,776,212 | 159.382 | 44.6 | 6,838 | 0.0 |
| ecp.modp | 3916 | 11,884,678 | 70.742 | 19.8 | 3,035 | 0.0 |
| ecp.double_jac | 308 | 24,592,539 | 146.384 | 41.0 | 79,846 | 0.0 |
| ecp.add_mixed | 124 | 12,398,583 | 73.801 | 20.6 | 99,989 | 0.0 |
| ecp.normalize | 5 | 18,020,507 | 107.265 | 30.0 | 3,604,101 | 0.0 |
| ecp.precompute_comb | 1 | 23,361,282 | 139.055 | 38.9 | 23,361,282 | 0.0 |
| (rest of sig) | | 1,463 | 0.009 | 0.0 | | |


### rsa2048_measure (10 runs)

sig stage: 8,817,441 cyc = 52.485 ms (stdev 0.0 cyc)

(no MEASD lines)


### rsa2048_measure_sig_detail (10 runs)

sig stage: 8,750,723 cyc = 52.088 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 7,178 | 0.043 | 0.1 | 7,178 | 0.0 |
| rsa.public | 1 | 8,658,903 | 51.541 | 99.0 | 8,658,903 | 0.0 |
| rsa.pss_mgf1 | 1 | 60,096 | 0.358 | 0.7 | 60,096 | 0.0 |
| rsa.pss_hash | 1 | 15,174 | 0.090 | 0.2 | 15,174 | 0.0 |
| mpi.exp_mod.r2 | 1 | 3,304,090 | 19.667 | 37.8 | 3,304,090 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 137,017 | 0.816 | 1.6 | 137,017 | 0.0 |
| mpi.exp_mod.core | 1 | 4,817,972 | 28.678 | 55.1 | 4,817,972 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 366,339 | 2.181 | 4.2 | 366,339 | 0.0 |
| (rest of sig) | | 9,372 | 0.056 | 0.1 | | |


### rsa2048_measure_sig_detail_sig_prims (10 runs)

sig stage: 8,753,525 cyc = 52.104 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 7,189 | 0.043 | 0.1 | 7,189 | 0.0 |
| rsa.public | 1 | 8,661,735 | 51.558 | 99.0 | 8,661,735 | 0.0 |
| rsa.pss_mgf1 | 1 | 60,093 | 0.358 | 0.7 | 60,093 | 0.0 |
| rsa.pss_hash | 1 | 15,167 | 0.090 | 0.2 | 15,167 | 0.0 |
| mpi.exp_mod.r2 | 1 | 3,304,879 | 19.672 | 37.8 | 3,304,879 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 137,067 | 0.816 | 1.6 | 137,067 | 0.0 |
| mpi.exp_mod.core | 1 | 4,819,846 | 28.690 | 55.1 | 4,819,846 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 366,428 | 2.181 | 4.2 | 366,428 | 0.0 |
| mpi.montmul | 37 | 5,292,516 | 31.503 | 60.5 | 143,041 | 0.0 |
| mpi.mod_mpi | 1 | 3,292,291 | 19.597 | 37.6 | 3,292,291 | 0.0 |
| (rest of sig) | | 9,341 | 0.056 | 0.1 | | |


### rsa2048_psa_measure (10 runs)

sig stage: 9,017,159 cyc = 53.674 ms (stdev 0.0 cyc)

(no MEASD lines)


### rsa2048_psa_measure_sig_detail (10 runs)

sig stage: 9,018,097 cyc = 53.679 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 20,080 | 0.120 | 0.2 | 20,080 | 0.0 |
| psa.verify_hash | 1 | 8,994,320 | 53.538 | 99.7 | 8,994,320 | 0.0 |
| mpi.exp_mod.r2 | 1 | 3,378,978 | 20.113 | 37.5 | 3,378,978 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 141,196 | 0.840 | 1.6 | 141,196 | 0.0 |
| mpi.exp_mod.core | 1 | 4,963,975 | 29.547 | 55.0 | 4,963,975 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 370,308 | 2.204 | 4.1 | 370,308 | 0.0 |
| (rest of sig) | | 3,697 | 0.022 | 0.0 | | |


### rsa2048_psa_measure_sig_detail_sig_prims (10 runs)

sig stage: 9,017,903 cyc = 53.678 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 20,093 | 0.120 | 0.2 | 20,093 | 0.0 |
| psa.verify_hash | 1 | 8,994,097 | 53.536 | 99.7 | 8,994,097 | 0.0 |
| mpi.exp_mod.r2 | 1 | 3,377,486 | 20.104 | 37.5 | 3,377,486 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 141,251 | 0.841 | 1.6 | 141,251 | 0.0 |
| mpi.exp_mod.core | 1 | 4,965,185 | 29.555 | 55.1 | 4,965,185 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 370,425 | 2.205 | 4.1 | 370,425 | 0.0 |
| mpi.montmul | 37 | 5,446,378 | 32.419 | 60.4 | 147,199 | 0.0 |
| mpi.mod_mpi | 1 | 3,363,537 | 20.021 | 37.3 | 3,363,537 | 0.0 |
| (rest of sig) | | 3,713 | 0.022 | 0.0 | | |


### ed25519_measure (10 runs)

sig stage: 4,040,436 cyc = 24.050 ms (stdev 0.0 cyc)

(no MEASD lines)


### ed25519_measure_sig_detail (10 runs)

sig stage: 4,076,907 cyc = 24.267 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ed25519.key_parse | 1 | 627 | 0.004 | 0.0 | 627 | 0.0 |
| ed25519.verify | 1 | 4,076,012 | 24.262 | 100.0 | 4,076,012 | 0.0 |
| ed25519.verify.decompress | 1 | 210,879 | 1.255 | 5.2 | 210,879 | 0.0 |
| ed25519.verify.sha512 | 1 | 22,055 | 0.131 | 0.5 | 22,055 | 0.0 |
| ed25519.verify.sc_reduce | 1 | 2,000 | 0.012 | 0.0 | 2,000 | 0.0 |
| ed25519.verify.smul | 1 | 3,642,676 | 21.683 | 89.3 | 3,642,676 | 0.0 |
| ed25519.verify.smul.precomp | 1 | 131,152 | 0.781 | 3.2 | 131,152 | 0.0 |
| ed25519.verify.smul.loop | 1 | 3,511,401 | 20.901 | 86.1 | 3,511,401 | 0.0 |
| ed25519.verify.smul.loop.dbl | 252 | 1,808,810 | 10.767 | 44.4 | 7,178 | 0.0 |
| ed25519.verify.smul.loop.add_a | 41 | 483,963 | 2.881 | 11.9 | 11,804 | 0.0 |
| ed25519.verify.smul.loop.add_b | 40 | 437,238 | 2.603 | 10.7 | 10,931 | 0.0 |
| ed25519.verify.encode | 1 | 197,927 | 1.178 | 4.9 | 197,927 | 0.0 |
| (rest of sig) | | 268 | 0.002 | 0.0 | | |


### ed25519_measure_sig_detail_sig_prims (10 runs)

sig stage: 4,357,764 cyc = 25.939 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ed25519.key_parse | 1 | 637 | 0.004 | 0.0 | 637 | 0.0 |
| ed25519.verify | 1 | 4,356,866 | 25.934 | 100.0 | 4,356,866 | 0.0 |
| ed25519.verify.decompress | 1 | 245,912 | 1.464 | 5.6 | 245,912 | 0.0 |
| ed25519.verify.sha512 | 1 | 22,068 | 0.131 | 0.5 | 22,068 | 0.0 |
| ed25519.verify.sc_reduce | 1 | 2,027 | 0.012 | 0.0 | 2,027 | 0.0 |
| ed25519.verify.smul | 1 | 3,853,576 | 22.938 | 88.4 | 3,853,576 | 0.0 |
| ed25519.verify.smul.precomp | 1 | 137,541 | 0.819 | 3.2 | 137,541 | 0.0 |
| ed25519.verify.smul.loop | 1 | 3,715,923 | 22.119 | 85.3 | 3,715,923 | 0.0 |
| ed25519.verify.smul.loop.dbl | 252 | 1,908,123 | 11.358 | 43.8 | 7,572 | 0.0 |
| ed25519.verify.smul.loop.add_a | 41 | 510,432 | 3.038 | 11.7 | 12,450 | 0.0 |
| ed25519.verify.smul.loop.add_b | 40 | 459,246 | 2.734 | 10.5 | 11,481 | 0.0 |
| ed25519.verify.encode | 1 | 232,805 | 1.386 | 5.3 | 232,805 | 0.0 |
| fiat.fe_mul | 1464 | 826,583 | 4.920 | 19.0 | 565 | 0.0 |
| fiat.fe_sq | 1521 | 729,998 | 4.345 | 16.8 | 480 | 0.0 |
| fiat.fe_invert | 1 | 229,439 | 1.366 | 5.3 | 229,439 | 0.0 |
| (rest of sig) | | 261 | 0.002 | 0.0 | | |


### mldsa44_measure (10 runs)

sig stage: 2,898,689 cyc = 17.254 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa44_measure_sig_detail (10 runs)

sig stage: 2,901,973 cyc = 17.274 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 2,899,564 | 17.259 | 99.9 | 2,899,564 | 0.0 |
| mldsa.verify.unpack | 1 | 75,116 | 0.447 | 2.6 | 75,116 | 0.0 |
| mldsa.verify.mu | 1 | 207,468 | 1.235 | 7.1 | 207,468 | 0.0 |
| mldsa.verify.challenge | 1 | 59,270 | 0.353 | 2.0 | 59,270 | 0.0 |
| mldsa.verify.t1 | 1 | 146,447 | 0.872 | 5.0 | 146,447 | 0.0 |
| mldsa.verify.expand_a | 1 | 1,639,076 | 9.756 | 56.5 | 1,639,076 | 0.0 |
| mldsa.verify.z_ntt | 1 | 120,668 | 0.718 | 4.2 | 120,668 | 0.0 |
| mldsa.verify.matmul | 1 | 74,109 | 0.441 | 2.6 | 74,109 | 0.0 |
| mldsa.verify.invntt | 1 | 125,740 | 0.748 | 4.3 | 125,740 | 0.0 |
| mldsa.verify.w1 | 1 | 89,079 | 0.530 | 3.1 | 89,079 | 0.0 |
| mldsa.verify.c_hash | 1 | 128,884 | 0.767 | 4.4 | 128,884 | 0.0 |
| (rest of sig) | | 2,409 | 0.014 | 0.1 | | |


### mldsa44_measure_sig_detail_sig_prims (10 runs)

sig stage: 2,907,419 cyc = 17.306 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 2,905,033 | 17.292 | 99.9 | 2,905,033 | 0.0 |
| mldsa.verify.unpack | 1 | 75,121 | 0.447 | 2.6 | 75,121 | 0.0 |
| mldsa.verify.mu | 1 | 207,946 | 1.238 | 7.2 | 207,946 | 0.0 |
| mldsa.verify.challenge | 1 | 59,470 | 0.354 | 2.0 | 59,470 | 0.0 |
| mldsa.verify.t1 | 1 | 146,770 | 0.874 | 5.0 | 146,770 | 0.0 |
| mldsa.verify.expand_a | 1 | 1,642,605 | 9.777 | 56.5 | 1,642,605 | 0.0 |
| mldsa.verify.z_ntt | 1 | 120,986 | 0.720 | 4.2 | 120,986 | 0.0 |
| mldsa.verify.matmul | 1 | 74,112 | 0.441 | 2.5 | 74,112 | 0.0 |
| mldsa.verify.invntt | 1 | 126,061 | 0.750 | 4.3 | 126,061 | 0.0 |
| mldsa.verify.w1 | 1 | 89,112 | 0.530 | 3.1 | 89,112 | 0.0 |
| mldsa.verify.c_hash | 1 | 129,151 | 0.769 | 4.4 | 129,151 | 0.0 |
| mld.keccakf1600 | 99 | 1,629,006 | 9.696 | 56.0 | 16,455 | 0.0 |
| mld.poly_ntt | 9 | 271,557 | 1.616 | 9.3 | 30,173 | 0.0 |
| mld.poly_invntt | 4 | 125,770 | 0.749 | 4.3 | 31,442 | 0.0 |
| mld.poly_uniform | 4 | 1,640,081 | 9.762 | 56.4 | 410,020 | 0.0 |
| (rest of sig) | | 2,386 | 0.014 | 0.1 | | |


### mldsa65_measure (10 runs)

sig stage: 4,951,334 cyc = 29.472 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa65_measure_sig_detail (10 runs)

sig stage: 4,940,810 cyc = 29.410 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 4,938,096 | 29.393 | 99.9 | 4,938,096 | 0.0 |
| mldsa.verify.unpack | 1 | 108,432 | 0.645 | 2.2 | 108,432 | 0.0 |
| mldsa.verify.mu | 1 | 298,144 | 1.775 | 6.0 | 298,144 | 0.0 |
| mldsa.verify.challenge | 1 | 61,373 | 0.365 | 1.2 | 61,373 | 0.0 |
| mldsa.verify.t1 | 1 | 221,316 | 1.317 | 4.5 | 221,316 | 0.0 |
| mldsa.verify.expand_a | 1 | 3,104,851 | 18.481 | 62.8 | 3,104,851 | 0.0 |
| mldsa.verify.z_ntt | 1 | 150,953 | 0.899 | 3.1 | 150,953 | 0.0 |
| mldsa.verify.matmul | 1 | 124,958 | 0.744 | 2.5 | 124,958 | 0.0 |
| mldsa.verify.invntt | 1 | 188,711 | 1.123 | 3.8 | 188,711 | 0.0 |
| mldsa.verify.w1 | 1 | 112,234 | 0.668 | 2.3 | 112,234 | 0.0 |
| mldsa.verify.c_hash | 1 | 129,513 | 0.771 | 2.6 | 129,513 | 0.0 |
| (rest of sig) | | 2,714 | 0.016 | 0.1 | | |


### mldsa65_measure_sig_detail_sig_prims (10 runs)

sig stage: 4,966,230 cyc = 29.561 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 4,963,510 | 29.545 | 99.9 | 4,963,510 | 0.0 |
| mldsa.verify.unpack | 1 | 108,435 | 0.645 | 2.2 | 108,435 | 0.0 |
| mldsa.verify.mu | 1 | 300,305 | 1.788 | 6.0 | 300,305 | 0.0 |
| mldsa.verify.challenge | 1 | 61,460 | 0.366 | 1.2 | 61,460 | 0.0 |
| mldsa.verify.t1 | 1 | 221,696 | 1.320 | 4.5 | 221,696 | 0.0 |
| mldsa.verify.expand_a | 1 | 3,126,051 | 18.607 | 62.9 | 3,126,051 | 0.0 |
| mldsa.verify.z_ntt | 1 | 151,265 | 0.900 | 3.0 | 151,265 | 0.0 |
| mldsa.verify.matmul | 1 | 124,951 | 0.744 | 2.5 | 124,951 | 0.0 |
| mldsa.verify.invntt | 1 | 189,078 | 1.125 | 3.8 | 189,078 | 0.0 |
| mldsa.verify.w1 | 1 | 112,220 | 0.668 | 2.3 | 112,220 | 0.0 |
| mldsa.verify.c_hash | 1 | 130,441 | 0.776 | 2.6 | 130,441 | 0.0 |
| mld.keccakf1600 | 174 | 2,873,627 | 17.105 | 57.9 | 16,515 | 0.0 |
| mld.poly_ntt | 12 | 362,124 | 2.155 | 7.3 | 30,177 | 0.0 |
| mld.poly_invntt | 6 | 188,643 | 1.123 | 3.8 | 31,440 | 0.0 |
| mld.poly_uniform | 9 | 3,122,434 | 18.586 | 62.9 | 346,937 | 0.0 |
| (rest of sig) | | 2,720 | 0.016 | 0.1 | | |


### mldsa87_measure (10 runs)

sig stage: 8,424,283 cyc = 50.145 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa87_measure_sig_detail (10 runs)

sig stage: 8,448,038 cyc = 50.286 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 8,445,302 | 50.270 | 100.0 | 8,445,302 | 0.0 |
| mldsa.verify.unpack | 1 | 154,914 | 0.922 | 1.8 | 154,914 | 0.0 |
| mldsa.verify.mu | 1 | 389,025 | 2.316 | 4.6 | 389,025 | 0.0 |
| mldsa.verify.challenge | 1 | 66,509 | 0.396 | 0.8 | 66,509 | 0.0 |
| mldsa.verify.t1 | 1 | 296,956 | 1.768 | 3.5 | 296,956 | 0.0 |
| mldsa.verify.expand_a | 1 | 5,807,904 | 34.571 | 68.7 | 5,807,904 | 0.0 |
| mldsa.verify.z_ntt | 1 | 235,236 | 1.400 | 2.8 | 235,236 | 0.0 |
| mldsa.verify.matmul | 1 | 228,011 | 1.357 | 2.7 | 228,011 | 0.0 |
| mldsa.verify.invntt | 1 | 251,498 | 1.497 | 3.0 | 251,498 | 0.0 |
| mldsa.verify.w1 | 1 | 150,593 | 0.896 | 1.8 | 150,593 | 0.0 |
| mldsa.verify.c_hash | 1 | 166,969 | 0.994 | 2.0 | 166,969 | 0.0 |
| (rest of sig) | | 2,736 | 0.016 | 0.0 | | |


### mldsa87_measure_sig_detail_sig_prims (10 runs)

sig stage: 8,462,088 cyc = 50.370 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 8,459,348 | 50.353 | 100.0 | 8,459,348 | 0.0 |
| mldsa.verify.unpack | 1 | 154,927 | 0.922 | 1.8 | 154,927 | 0.0 |
| mldsa.verify.mu | 1 | 389,734 | 2.320 | 4.6 | 389,734 | 0.0 |
| mldsa.verify.challenge | 1 | 66,612 | 0.397 | 0.8 | 66,612 | 0.0 |
| mldsa.verify.t1 | 1 | 297,547 | 1.771 | 3.5 | 297,547 | 0.0 |
| mldsa.verify.expand_a | 1 | 5,819,128 | 34.638 | 68.8 | 5,819,128 | 0.0 |
| mldsa.verify.z_ntt | 1 | 235,763 | 1.403 | 2.8 | 235,763 | 0.0 |
| mldsa.verify.matmul | 1 | 228,005 | 1.357 | 2.7 | 228,005 | 0.0 |
| mldsa.verify.invntt | 1 | 252,091 | 1.501 | 3.0 | 252,091 | 0.0 |
| mldsa.verify.w1 | 1 | 150,598 | 0.896 | 1.8 | 150,598 | 0.0 |
| mldsa.verify.c_hash | 1 | 167,270 | 0.996 | 2.0 | 167,270 | 0.0 |
| mld.keccakf1600 | 311 | 5,118,767 | 30.469 | 60.5 | 16,459 | 0.0 |
| mld.poly_ntt | 16 | 511,149 | 3.043 | 6.0 | 31,947 | 0.0 |
| mld.poly_invntt | 8 | 251,530 | 1.497 | 3.0 | 31,441 | 0.0 |
| mld.poly_uniform | 14 | 5,814,402 | 34.610 | 68.7 | 415,314 | 0.0 |
| (rest of sig) | | 2,740 | 0.016 | 0.0 | | |


## sig stage per build (instrumentation cost)

| build | runs | sig cycles | sig ms | stdev cyc |
|---|---|---|---|---|
| ecdsa_p256_measure | 10 | 18,150,957 | 108.041 | 0.0 |
| ecdsa_p256_measure_sig_detail | 10 | 18,145,740 | 108.010 | 0.0 |
| ecdsa_p256_measure_sig_detail_sig_prims | 10 | 19,324,694 | 115.028 | 0.0 |
| ecdsa_p256_psa_heap_measure | 10 | 370,863,606 | 2207.521 | 0.0 |
| ecdsa_p256_psa_heap_measure_sig_detail | 10 | 358,836,011 | 2135.929 | 0.0 |
| ecdsa_p256_psa_heap_measure_sig_detail_sig_prims | 10 | 371,536,797 | 2211.529 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure | 10 | 58,970,947 | 351.018 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure_sig_detail | 10 | 60,659,741 | 361.070 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure_sig_detail_sig_prims | 9 | 60,044,399 | 357.407 | 0.0 |
| rsa2048_measure | 10 | 8,817,441 | 52.485 | 0.0 |
| rsa2048_measure_sig_detail | 10 | 8,750,723 | 52.088 | 0.0 |
| rsa2048_measure_sig_detail_sig_prims | 10 | 8,753,525 | 52.104 | 0.0 |
| rsa2048_psa_measure | 10 | 9,017,159 | 53.674 | 0.0 |
| rsa2048_psa_measure_sig_detail | 10 | 9,018,097 | 53.679 | 0.0 |
| rsa2048_psa_measure_sig_detail_sig_prims | 10 | 9,017,903 | 53.678 | 0.0 |
| ed25519_measure | 10 | 4,040,436 | 24.050 | 0.0 |
| ed25519_measure_sig_detail | 10 | 4,076,907 | 24.267 | 0.0 |
| ed25519_measure_sig_detail_sig_prims | 10 | 4,357,764 | 25.939 | 0.0 |
| mldsa44_measure | 10 | 2,898,689 | 17.254 | 0.0 |
| mldsa44_measure_sig_detail | 10 | 2,901,973 | 17.274 | 0.0 |
| mldsa44_measure_sig_detail_sig_prims | 10 | 2,907,419 | 17.306 | 0.0 |
| mldsa65_measure | 10 | 4,951,334 | 29.472 | 0.0 |
| mldsa65_measure_sig_detail | 10 | 4,940,810 | 29.410 | 0.0 |
| mldsa65_measure_sig_detail_sig_prims | 10 | 4,966,230 | 29.561 | 0.0 |
| mldsa87_measure | 10 | 8,424,283 | 50.145 | 0.0 |
| mldsa87_measure_sig_detail | 10 | 8,448,038 | 50.286 | 0.0 |
| mldsa87_measure_sig_detail_sig_prims | 10 | 8,462,088 | 50.370 | 0.0 |
