
### ecdsa_p256_measure (10 runs)

sig stage: 18,150,957 cyc = 108.041 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail (10 runs)

sig stage: 18,114,764 cyc = 107.826 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 759 | 0.005 | 0.0 | 759 | 0.0 |
| ecdsa.sig_decode | 1 | 455 | 0.003 | 0.0 | 455 | 0.0 |
| ecdsa.verify | 1 | 18,113,230 | 107.817 | 100.0 | 18,113,230 | 0.0 |
| ecdsa.verify.load | 1 | 3,358 | 0.020 | 0.0 | 3,358 | 0.0 |
| ecdsa.verify.inv_s | 1 | 226,017 | 1.345 | 1.2 | 226,017 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 331,675 | 1.974 | 1.8 | 331,675 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 268,383 | 1.598 | 1.5 | 268,383 | 0.0 |
| ecdsa.verify.loop | 1 | 17,042,921 | 101.446 | 94.1 | 17,042,921 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 8,486,665 | 50.516 | 46.8 | 33,281 | 0.0 |
| ecdsa.verify.loop.add | 195 | 8,526,128 | 50.751 | 47.1 | 43,724 | 0.0 |
| ecdsa.verify.final | 1 | 240,745 | 1.433 | 1.3 | 240,745 | 0.0 |
| (rest of sig) | | 320 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_sig_detail_sig_prims (10 runs)

sig stage: 18,972,271 cyc = 112.930 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 765 | 0.005 | 0.0 | 765 | 0.0 |
| ecdsa.sig_decode | 1 | 450 | 0.003 | 0.0 | 450 | 0.0 |
| ecdsa.verify | 1 | 18,970,744 | 112.921 | 100.0 | 18,970,744 | 0.0 |
| ecdsa.verify.load | 1 | 3,317 | 0.020 | 0.0 | 3,317 | 0.0 |
| ecdsa.verify.inv_s | 1 | 226,810 | 1.350 | 1.2 | 226,810 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 336,908 | 2.005 | 1.8 | 336,908 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 270,981 | 1.613 | 1.4 | 270,981 | 0.0 |
| ecdsa.verify.loop | 1 | 17,890,351 | 106.490 | 94.3 | 17,890,351 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 8,896,977 | 52.958 | 46.9 | 34,890 | 0.0 |
| ecdsa.verify.loop.add | 195 | 8,964,500 | 53.360 | 47.3 | 45,972 | 0.0 |
| ecdsa.verify.final | 1 | 242,236 | 1.442 | 1.3 | 242,236 | 0.0 |
| tc.vli_mult | 4201 | 6,599,138 | 39.281 | 34.8 | 1,571 | 0.0 |
| tc.mmod_fast | 4199 | 9,429,136 | 56.126 | 49.7 | 2,246 | 0.0 |
| tc.mmod | 2 | 332,563 | 1.980 | 1.8 | 166,282 | 0.0 |
| tc.modinv | 3 | 682,033 | 4.060 | 3.6 | 227,344 | 0.0 |
| tc.double_jacobian | 255 | 8,840,539 | 52.622 | 46.6 | 34,669 | 0.0 |
| tc.xycz_add | 196 | 5,036,999 | 29.982 | 26.5 | 25,699 | 0.0 |
| tc.apply_z | 197 | 3,078,817 | 18.326 | 16.2 | 15,629 | 0.0 |
| (rest of sig) | | 312 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_opt_o2 (10 runs)

sig stage: 14,356,092 cyc = 85.453 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail_opt_o2 (10 runs)

sig stage: 14,407,159 cyc = 85.757 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 645 | 0.004 | 0.0 | 645 | 0.0 |
| ecdsa.sig_decode | 1 | 387 | 0.002 | 0.0 | 387 | 0.0 |
| ecdsa.verify | 1 | 14,405,838 | 85.749 | 100.0 | 14,405,838 | 0.0 |
| ecdsa.verify.load | 1 | 3,005 | 0.018 | 0.0 | 3,005 | 0.0 |
| ecdsa.verify.inv_s | 1 | 163,260 | 0.972 | 1.1 | 163,260 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 277,142 | 1.650 | 1.9 | 277,142 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 198,333 | 1.181 | 1.4 | 198,333 | 0.0 |
| ecdsa.verify.loop | 1 | 13,587,480 | 80.878 | 94.3 | 13,587,480 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 6,746,439 | 40.157 | 46.8 | 26,457 | 0.0 |
| ecdsa.verify.loop.add | 195 | 6,817,246 | 40.579 | 47.3 | 34,960 | 0.0 |
| ecdsa.verify.final | 1 | 176,545 | 1.051 | 1.2 | 176,545 | 0.0 |
| (rest of sig) | | 289 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_sig_detail_sig_prims_opt_o2 (10 runs)

sig stage: 14,738,178 cyc = 87.727 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 658 | 0.004 | 0.0 | 658 | 0.0 |
| ecdsa.sig_decode | 1 | 387 | 0.002 | 0.0 | 387 | 0.0 |
| ecdsa.verify | 1 | 14,736,839 | 87.719 | 100.0 | 14,736,839 | 0.0 |
| ecdsa.verify.load | 1 | 2,995 | 0.018 | 0.0 | 2,995 | 0.0 |
| ecdsa.verify.inv_s | 1 | 164,345 | 0.978 | 1.1 | 164,345 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 277,394 | 1.651 | 1.9 | 277,394 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 200,231 | 1.192 | 1.4 | 200,231 | 0.0 |
| ecdsa.verify.loop | 1 | 13,913,869 | 82.821 | 94.4 | 13,913,869 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 6,896,874 | 41.053 | 46.8 | 27,047 | 0.0 |
| ecdsa.verify.loop.add | 195 | 6,992,746 | 41.623 | 47.4 | 35,860 | 0.0 |
| ecdsa.verify.final | 1 | 177,934 | 1.059 | 1.2 | 177,934 | 0.0 |
| tc.vli_mult | 4201 | 6,235,765 | 37.118 | 42.3 | 1,484 | 0.0 |
| tc.mmod_fast | 4199 | 6,140,957 | 36.553 | 41.7 | 1,462 | 0.0 |
| tc.mmod | 2 | 273,215 | 1.626 | 1.9 | 136,608 | 0.0 |
| tc.modinv | 3 | 497,262 | 2.960 | 3.4 | 165,754 | 0.0 |
| tc.double_jacobian | 255 | 6,857,913 | 40.821 | 46.5 | 26,894 | 0.0 |
| tc.xycz_add | 196 | 3,926,373 | 23.371 | 26.6 | 20,033 | 0.0 |
| tc.apply_z | 197 | 2,404,460 | 14.312 | 16.3 | 12,205 | 0.0 |
| (rest of sig) | | 294 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_opt_o3 (10 runs)

sig stage: 11,666,220 cyc = 69.442 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail_opt_o3 (10 runs)

sig stage: 11,693,586 cyc = 69.605 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 541 | 0.003 | 0.0 | 541 | 0.0 |
| ecdsa.sig_decode | 1 | 284 | 0.002 | 0.0 | 284 | 0.0 |
| ecdsa.verify | 1 | 11,692,453 | 69.598 | 100.0 | 11,692,453 | 0.0 |
| ecdsa.verify.load | 1 | 2,986 | 0.018 | 0.0 | 2,986 | 0.0 |
| ecdsa.verify.inv_s | 1 | 165,586 | 0.986 | 1.4 | 165,586 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 277,237 | 1.650 | 2.4 | 277,237 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 194,298 | 1.157 | 1.7 | 194,298 | 0.0 |
| ecdsa.verify.loop | 1 | 10,875,868 | 64.737 | 93.0 | 10,875,868 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 5,416,810 | 32.243 | 46.3 | 21,242 | 0.0 |
| ecdsa.verify.loop.add | 195 | 5,436,216 | 32.358 | 46.5 | 27,878 | 0.0 |
| ecdsa.verify.final | 1 | 176,403 | 1.050 | 1.5 | 176,403 | 0.0 |
| (rest of sig) | | 308 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_sig_detail_sig_prims_opt_o3 (10 runs)

sig stage: 12,028,457 cyc = 71.598 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 559 | 0.003 | 0.0 | 559 | 0.0 |
| ecdsa.sig_decode | 1 | 288 | 0.002 | 0.0 | 288 | 0.0 |
| ecdsa.verify | 1 | 12,027,272 | 71.591 | 100.0 | 12,027,272 | 0.0 |
| ecdsa.verify.load | 1 | 3,010 | 0.018 | 0.0 | 3,010 | 0.0 |
| ecdsa.verify.inv_s | 1 | 166,638 | 0.992 | 1.4 | 166,638 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 269,690 | 1.605 | 2.2 | 269,690 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 196,322 | 1.169 | 1.6 | 196,322 | 0.0 |
| ecdsa.verify.loop | 1 | 11,213,610 | 66.748 | 93.2 | 11,213,610 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 5,575,152 | 33.185 | 46.3 | 21,863 | 0.0 |
| ecdsa.verify.loop.add | 195 | 5,612,371 | 33.407 | 46.7 | 28,781 | 0.0 |
| ecdsa.verify.final | 1 | 177,868 | 1.059 | 1.5 | 177,868 | 0.0 |
| tc.vli_mult | 4201 | 6,054,881 | 36.041 | 50.3 | 1,441 | 0.0 |
| tc.mmod_fast | 4199 | 3,556,837 | 21.172 | 29.6 | 847 | 0.0 |
| tc.mmod | 2 | 265,552 | 1.581 | 2.2 | 132,776 | 0.0 |
| tc.modinv | 3 | 504,229 | 3.001 | 4.2 | 168,076 | 0.0 |
| tc.double_jacobian | 255 | 5,526,600 | 32.896 | 45.9 | 21,673 | 0.0 |
| tc.xycz_add | 196 | 3,142,880 | 18.708 | 26.1 | 16,035 | 0.0 |
| tc.apply_z | 197 | 1,911,753 | 11.379 | 15.9 | 9,704 | 0.0 |
| (rest of sig) | | 338 | 0.002 | 0.0 | | |


### ecdsa_p256_measure_opt_lto (10 runs)

sig stage: 18,053,671 cyc = 107.462 ms (stdev 0.0 cyc)

(no MEASD lines)


### ecdsa_p256_measure_sig_detail_opt_lto (10 runs)

sig stage: 18,104,178 cyc = 107.763 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 753 | 0.004 | 0.0 | 753 | 0.0 |
| ecdsa.sig_decode | 1 | 467 | 0.003 | 0.0 | 467 | 0.0 |
| ecdsa.verify | 1 | 18,102,756 | 107.754 | 100.0 | 18,102,756 | 0.0 |
| ecdsa.verify.load | 1 | 3,356 | 0.020 | 0.0 | 3,356 | 0.0 |
| ecdsa.verify.inv_s | 1 | 225,745 | 1.344 | 1.2 | 225,745 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 331,570 | 1.974 | 1.8 | 331,570 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 268,345 | 1.597 | 1.5 | 268,345 | 0.0 |
| ecdsa.verify.loop | 1 | 17,032,718 | 101.385 | 94.1 | 17,032,718 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 8,473,145 | 50.435 | 46.8 | 33,228 | 0.0 |
| ecdsa.verify.loop.add | 195 | 8,518,143 | 50.703 | 47.1 | 43,683 | 0.0 |
| ecdsa.verify.final | 1 | 240,714 | 1.433 | 1.3 | 240,714 | 0.0 |
| (rest of sig) | | 202 | 0.001 | 0.0 | | |


### ecdsa_p256_measure_sig_detail_sig_prims_opt_lto (10 runs)

sig stage: 18,956,396 cyc = 112.836 ms (stdev 0.0 cyc)

| item | calls | cycles (mean) | ms | % of sig | cyc/call | stdev cyc |
|---|---|---|---|---|---|---|
| ecdsa.key_parse | 1 | 758 | 0.005 | 0.0 | 758 | 0.0 |
| ecdsa.sig_decode | 1 | 469 | 0.003 | 0.0 | 469 | 0.0 |
| ecdsa.verify | 1 | 18,954,971 | 112.827 | 100.0 | 18,954,971 | 0.0 |
| ecdsa.verify.load | 1 | 3,352 | 0.020 | 0.0 | 3,352 | 0.0 |
| ecdsa.verify.inv_s | 1 | 225,879 | 1.345 | 1.2 | 225,879 | 0.0 |
| ecdsa.verify.u1u2 | 1 | 336,835 | 2.005 | 1.8 | 336,835 | 0.0 |
| ecdsa.verify.g_plus_q | 1 | 270,255 | 1.609 | 1.4 | 270,255 | 0.0 |
| ecdsa.verify.loop | 1 | 17,876,824 | 106.410 | 94.3 | 17,876,824 | 0.0 |
| ecdsa.verify.loop.dbl | 255 | 8,880,135 | 52.858 | 46.8 | 34,824 | 0.0 |
| ecdsa.verify.loop.add | 195 | 8,959,529 | 53.331 | 47.3 | 45,946 | 0.0 |
| ecdsa.verify.final | 1 | 241,528 | 1.438 | 1.3 | 241,528 | 0.0 |
| tc.vli_mult | 4201 | 6,520,358 | 38.812 | 34.4 | 1,552 | 0.0 |
| tc.mmod_fast | 4199 | 9,326,062 | 55.512 | 49.2 | 2,221 | 0.0 |
| tc.mmod | 2 | 332,573 | 1.980 | 1.8 | 166,286 | 0.0 |
| tc.modinv | 3 | 679,689 | 4.046 | 3.6 | 226,563 | 0.0 |
| tc.double_jacobian | 255 | 8,818,776 | 52.493 | 46.5 | 34,583 | 0.0 |
| tc.xycz_add | 196 | 5,032,567 | 29.956 | 26.5 | 25,676 | 0.0 |
| tc.apply_z | 197 | 3,074,889 | 18.303 | 16.2 | 15,609 | 0.0 |
| (rest of sig) | | 198 | 0.001 | 0.0 | | |


## sig stage per build (instrumentation cost)

| build | runs | sig cycles | sig ms | stdev cyc |
|---|---|---|---|---|
| ecdsa_p256_measure | 10 | 18,150,957 | 108.041 | 0.0 |
| ecdsa_p256_measure_sig_detail | 10 | 18,114,764 | 107.826 | 0.0 |
| ecdsa_p256_measure_sig_detail_sig_prims | 10 | 18,972,271 | 112.930 | 0.0 |
| ecdsa_p256_measure_opt_o2 | 10 | 14,356,092 | 85.453 | 0.0 |
| ecdsa_p256_measure_sig_detail_opt_o2 | 10 | 14,407,159 | 85.757 | 0.0 |
| ecdsa_p256_measure_sig_detail_sig_prims_opt_o2 | 10 | 14,738,178 | 87.727 | 0.0 |
| ecdsa_p256_measure_opt_o3 | 10 | 11,666,220 | 69.442 | 0.0 |
| ecdsa_p256_measure_sig_detail_opt_o3 | 10 | 11,693,586 | 69.605 | 0.0 |
| ecdsa_p256_measure_sig_detail_sig_prims_opt_o3 | 10 | 12,028,457 | 71.598 | 0.0 |
| ecdsa_p256_measure_opt_lto | 10 | 18,053,671 | 107.462 | 0.0 |
| ecdsa_p256_measure_sig_detail_opt_lto | 10 | 18,104,178 | 107.763 | 0.0 |
| ecdsa_p256_measure_sig_detail_sig_prims_opt_lto | 10 | 18,956,396 | 112.836 | 0.0 |
