
### ecdsa_p256_measure_opt_o3 (10 runs)

sig stage: 11,666,220 cyc = 69.442 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail_opt_o3 (10 runs)

sig stage: 11,689,102 cyc = 69.578 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 551 | 0.003 | 0.0 | 551 | 0.0 |
| ecdsa.sig_decode | 1 | 288 | 0.002 | 0.0 | 288 | 0.0 |
| ecdsa.verify | 1 | 11,687,931 | 69.571 | 100.0 | 11,687,931 | 0.0 |
| ecdsa.verify.load | 1 | 3,012 | 0.018 | 0.0 | 3,012 | 0.0 |
| ecdsa.verify.inv_s | 1 | 165,565 | 0.986 | 1.4 | 165,565 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 277,232 | 1.650 | 2.4 | 277,232 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 194,214 | 1.156 | 1.7 | 194,214 | 0.0 |
| ecdsa.verify.loop | 1 | 10,871,417 | 64.711 | 93.0 | 10,871,417 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 5,413,166 | 32.221 | 46.3 | 21,228 | 0.0 |
| ecdsa.verify.loop.add | 195 | 5,430,479 | 32.324 | 46.5 | 27,849 | 0.0 |
| ecdsa.verify.final | 1 | 176,360 | 1.050 | 1.5 | 176,360 | 0.0 |
| (rest of sig) | | 332 | 0.002 | 0.0 | | |


### ecdsa_p256_psa_heap_measure_opt_o3 (10 runs)

sig stage: 201,068,662 cyc = 1196.837 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_psa_heap_measure_sig_detail_opt_o3 (10 runs)

sig stage: 200,901,844 cyc = 1195.844 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 151,005 | 0.899 | 0.1 | 151,005 | 0.0 |
| psa.verify_hash | 1 | 200,750,049 | 1194.941 | 99.9 | 200,750,049 | 0.0 |
| mbecdsa.verify | 1 | 200,598,505 | 1194.039 | 99.8 | 200,598,505 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 1,887,643 | 11.236 | 0.9 | 1,887,643 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 89,199 | 0.531 | 0.0 | 89,199 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 50,556,154 | 300.929 | 25.2 | 50,556,154 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 145,679,844 | 867.142 | 72.5 | 145,679,844 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 2,377,813 | 14.154 | 1.2 | 2,377,813 | 0.0 |
| mbecdsa.verify.final | 1 | 603 | 0.004 | 0.0 | 603 | 0.0 |
| (rest of sig) | | 790 | 0.005 | 0.0 | | |


### ecdsa_p256_psa_heap_nistopt_measure_opt_o3 (10 runs)

sig stage: 35,500,857 cyc = 211.315 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_psa_heap_nistopt_measure_sig_detail_opt_o3 (10 runs)

sig stage: 35,671,151 cyc = 212.328 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 21,890 | 0.130 | 0.1 | 21,890 | 0.0 |
| psa.verify_hash | 1 | 35,648,471 | 212.193 | 99.9 | 35,648,471 | 0.0 |
| mbecdsa.verify | 1 | 35,626,028 | 212.060 | 99.9 | 35,626,028 | 0.0 |
| mbecdsa.verify.inv_s | 1 | 1,896,311 | 11.288 | 5.3 | 1,896,311 | 0.0 |
| mbecdsa.verify.u1u2 | 1 | 88,786 | 0.528 | 0.2 | 88,786 | 0.0 |
| mbecdsa.verify.mul_u1g | 1 | 8,238,215 | 49.037 | 23.1 | 8,238,215 | 0.0 |
| mbecdsa.verify.mul_u2q | 1 | 23,423,757 | 139.427 | 65.7 | 23,423,757 | 0.0 |
| mbecdsa.verify.add_norm | 1 | 1,970,950 | 11.732 | 5.5 | 1,970,950 | 0.0 |
| mbecdsa.verify.final | 1 | 598 | 0.004 | 0.0 | 598 | 0.0 |
| (rest of sig) | | 790 | 0.005 | 0.0 | | |


### rsa2048_measure_opt_o3 (10 runs)

sig stage: 6,386,688 cyc = 38.016 ms (stdev 0.0 cyc)

(no MEASD lines)


### rsa2048_measure_sig_detail_opt_o3 (10 runs)

sig stage: 6,389,177 cyc = 38.031 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 2,869 | 0.017 | 0.0 | 2,869 | 0.0 |
| rsa.public | 1 | 6,342,497 | 37.753 | 99.3 | 6,342,497 | 0.0 |
| rsa.pss_mgf1 | 1 | 31,274 | 0.186 | 0.5 | 31,274 | 0.0 |
| rsa.pss_hash | 1 | 8,378 | 0.050 | 0.1 | 8,378 | 0.0 |
| mpi.exp_mod.r2 | 1 | 1,635,418 | 9.735 | 25.6 | 1,635,418 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 123,860 | 0.737 | 1.9 | 123,860 | 0.0 |
| mpi.exp_mod.core | 1 | 4,341,264 | 25.841 | 67.9 | 4,341,264 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 232,146 | 1.382 | 3.6 | 232,146 | 0.0 |
| (rest of sig) | | 4,159 | 0.025 | 0.1 | | |


### rsa2048_psa_measure_opt_o3 (10 runs)

sig stage: 6,401,274 cyc = 38.103 ms (stdev 0.0 cyc)

(no MEASD lines)


### rsa2048_psa_measure_sig_detail_opt_o3 (10 runs)

sig stage: 6,401,237 cyc = 38.103 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| rsa.key_parse | 1 | 9,564 | 0.057 | 0.1 | 9,564 | 0.0 |
| psa.verify_hash | 1 | 6,390,525 | 38.039 | 99.8 | 6,390,525 | 0.0 |
| mpi.exp_mod.r2 | 1 | 1,634,853 | 9.731 | 25.5 | 1,634,853 | 0.0 |
| mpi.exp_mod.to_mont | 1 | 123,855 | 0.737 | 1.9 | 123,855 | 0.0 |
| mpi.exp_mod.core | 1 | 4,340,535 | 25.837 | 67.8 | 4,340,535 | 0.0 |
| mpi.exp_mod.from_mont | 1 | 232,126 | 1.382 | 3.6 | 232,126 | 0.0 |
| (rest of sig) | | 1,148 | 0.007 | 0.0 | | |


### ed25519_measure_opt_o3 (10 runs)

sig stage: 2,240,224 cyc = 13.335 ms (stdev 0.0 cyc)

(no MEASD lines)


### ed25519_measure_sig_detail_opt_o3 (10 runs)

sig stage: 2,212,608 cyc = 13.170 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ed25519.key_parse | 1 | 391 | 0.002 | 0.0 | 391 | 0.0 |
| ed25519.verify | 1 | 2,211,992 | 13.167 | 100.0 | 2,211,992 | 0.0 |
| ed25519.verify.decompress | 1 | 137,725 | 0.820 | 6.2 | 137,725 | 0.0 |
| ed25519.verify.sha512 | 1 | 17,234 | 0.103 | 0.8 | 17,234 | 0.0 |
| ed25519.verify.sc_reduce | 1 | 1,737 | 0.010 | 0.1 | 1,737 | 0.0 |
| ed25519.verify.smul | 1 | 1,923,618 | 11.450 | 86.9 | 1,923,618 | 0.0 |
| ed25519.verify.smul.precomp | 1 | 76,547 | 0.456 | 3.5 | 76,547 | 0.0 |
| ed25519.verify.smul.loop | 1 | 1,847,017 | 10.994 | 83.5 | 1,847,017 | 0.0 |
| ed25519.verify.smul.loop.dbl | 252 | 890,531 | 5.301 | 40.2 | 3,534 | 0.0 |
| ed25519.verify.smul.loop.add_a | 41 | 254,578 | 1.515 | 11.5 | 6,209 | 0.0 |
| ed25519.verify.smul.loop.add_b | 40 | 226,291 | 1.347 | 10.2 | 5,657 | 0.0 |
| ed25519.verify.encode | 1 | 131,406 | 0.782 | 5.9 | 131,406 | 0.0 |
| (rest of sig) | | 225 | 0.001 | 0.0 | | |


### mldsa44_measure_opt_o3 (10 runs)

sig stage: 2,719,452 cyc = 16.187 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa44_measure_sig_detail_opt_o3 (10 runs)

sig stage: 2,733,858 cyc = 16.273 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 2,733,267 | 16.269 | 100.0 | 2,733,267 | 0.0 |
| mldsa.verify.unpack | 1 | 69,061 | 0.411 | 2.5 | 69,061 | 0.0 |
| mldsa.verify.mu | 1 | 226,845 | 1.350 | 8.3 | 226,845 | 0.0 |
| mldsa.verify.challenge | 1 | 51,380 | 0.306 | 1.9 | 51,380 | 0.0 |
| mldsa.verify.t1 | 1 | 133,448 | 0.794 | 4.9 | 133,448 | 0.0 |
| mldsa.verify.expand_a | 1 | 1,717,984 | 10.226 | 62.8 | 1,717,984 | 0.0 |
| mldsa.verify.z_ntt | 1 | 106,674 | 0.635 | 3.9 | 106,674 | 0.0 |
| mldsa.verify.matmul | 1 | 47,271 | 0.281 | 1.7 | 47,271 | 0.0 |
| mldsa.verify.invntt | 1 | 123,158 | 0.733 | 4.5 | 123,158 | 0.0 |
| mldsa.verify.w1 | 1 | 84,771 | 0.505 | 3.1 | 84,771 | 0.0 |
| mldsa.verify.c_hash | 1 | 142,642 | 0.849 | 5.2 | 142,642 | 0.0 |
| (rest of sig) | | 591 | 0.004 | 0.0 | | |


### mldsa65_measure_opt_o3 (10 runs)

sig stage: 4,587,861 cyc = 27.309 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa65_measure_sig_detail_opt_o3 (10 runs)

sig stage: 4,582,524 cyc = 27.277 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 4,581,928 | 27.273 | 100.0 | 4,581,928 | 0.0 |
| mldsa.verify.unpack | 1 | 91,419 | 0.544 | 2.0 | 91,419 | 0.0 |
| mldsa.verify.mu | 1 | 326,931 | 1.946 | 7.1 | 326,931 | 0.0 |
| mldsa.verify.challenge | 1 | 51,629 | 0.307 | 1.1 | 51,629 | 0.0 |
| mldsa.verify.t1 | 1 | 201,651 | 1.200 | 4.4 | 201,651 | 0.0 |
| mldsa.verify.expand_a | 1 | 3,219,541 | 19.164 | 70.3 | 3,219,541 | 0.0 |
| mldsa.verify.z_ntt | 1 | 138,493 | 0.824 | 3.0 | 138,493 | 0.0 |
| mldsa.verify.matmul | 1 | 81,619 | 0.486 | 1.8 | 81,619 | 0.0 |
| mldsa.verify.invntt | 1 | 184,706 | 1.099 | 4.0 | 184,706 | 0.0 |
| mldsa.verify.w1 | 1 | 95,640 | 0.569 | 2.1 | 95,640 | 0.0 |
| mldsa.verify.c_hash | 1 | 142,596 | 0.849 | 3.1 | 142,596 | 0.0 |
| (rest of sig) | | 596 | 0.004 | 0.0 | | |


### mldsa87_measure_opt_o3 (10 runs)

sig stage: 7,869,341 cyc = 46.841 ms (stdev 0.0 cyc)

(no MEASD lines)


### mldsa87_measure_sig_detail_opt_o3 (10 runs)

sig stage: 7,892,556 cyc = 46.980 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| mldsa.verify | 1 | 7,891,905 | 46.976 | 100.0 | 7,891,905 | 0.0 |
| mldsa.verify.unpack | 1 | 133,289 | 0.793 | 1.7 | 133,289 | 0.0 |
| mldsa.verify.mu | 1 | 429,496 | 2.557 | 5.4 | 429,496 | 0.0 |
| mldsa.verify.challenge | 1 | 53,623 | 0.319 | 0.7 | 53,623 | 0.0 |
| mldsa.verify.t1 | 1 | 264,761 | 1.576 | 3.4 | 264,761 | 0.0 |
| mldsa.verify.expand_a | 1 | 6,025,106 | 35.864 | 76.3 | 6,025,106 | 0.0 |
| mldsa.verify.z_ntt | 1 | 206,761 | 1.231 | 2.6 | 206,761 | 0.0 |
| mldsa.verify.matmul | 1 | 143,675 | 0.855 | 1.8 | 143,675 | 0.0 |
| mldsa.verify.invntt | 1 | 246,314 | 1.466 | 3.1 | 246,314 | 0.0 |
| mldsa.verify.w1 | 1 | 128,618 | 0.766 | 1.6 | 128,618 | 0.0 |
| mldsa.verify.c_hash | 1 | 183,764 | 1.094 | 2.3 | 183,764 | 0.0 |
| (rest of sig) | | 651 | 0.004 | 0.0 | | |


## sig stage per build (instrumentation cost)

| build | runs | sig cycles | sig ms | stdev cyc |
|---|---|---|---|---|
| ecdsa_p256_measure_opt_o3 | 10 | 11,666,220 | 69.442 | 0.0 |
| ecdsa_p256_measure_sig_detail_opt_o3 | 10 | 11,689,102 | 69.578 | 0.0 |
| ecdsa_p256_psa_heap_measure_opt_o3 | 10 | 201,068,662 | 1196.837 | 0.0 |
| ecdsa_p256_psa_heap_measure_sig_detail_opt_o3 | 10 | 200,901,844 | 1195.844 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure_opt_o3 | 10 | 35,500,857 | 211.315 | 0.0 |
| ecdsa_p256_psa_heap_nistopt_measure_sig_detail_opt_o3 | 10 | 35,671,151 | 212.328 | 0.0 |
| rsa2048_measure_opt_o3 | 10 | 6,386,688 | 38.016 | 0.0 |
| rsa2048_measure_sig_detail_opt_o3 | 10 | 6,389,177 | 38.031 | 0.0 |
| rsa2048_psa_measure_opt_o3 | 10 | 6,401,274 | 38.103 | 0.0 |
| rsa2048_psa_measure_sig_detail_opt_o3 | 10 | 6,401,237 | 38.103 | 0.0 |
| ed25519_measure_opt_o3 | 10 | 2,240,224 | 13.335 | 0.0 |
| ed25519_measure_sig_detail_opt_o3 | 10 | 2,212,608 | 13.170 | 0.0 |
| mldsa44_measure_opt_o3 | 10 | 2,719,452 | 16.187 | 0.0 |
| mldsa44_measure_sig_detail_opt_o3 | 10 | 2,733,858 | 16.273 | 0.0 |
| mldsa65_measure_opt_o3 | 10 | 4,587,861 | 27.309 | 0.0 |
| mldsa65_measure_sig_detail_opt_o3 | 10 | 4,582,524 | 27.277 | 0.0 |
| mldsa87_measure_opt_o3 | 10 | 7,869,341 | 46.841 | 0.0 |
| mldsa87_measure_sig_detail_opt_o3 | 10 | 7,892,556 | 46.980 | 0.0 |
