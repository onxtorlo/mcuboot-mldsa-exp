# ChkUp step 4 — boot_mldsa65_chkup_noval0

alerts: 4 -> TP 4, FP 0; negative checks -> TN 1, FN 0

| case | property | alert | PoC | attack succeeds if | observed | result | MCUboot log |
|---|---|---|---|---|---|---|---|
| baseline | baseline | - | legitimate upgrade v1/cnt1 -> v2/cnt5 | v2 | v2 | ok | swap;jump |
| slot0_tamper | authenticity | partial | running image (slot0) modified, no upgrade | v1-tampered | v1-tampered | TP | jump |
| slot0_tamper_integrity | integrity | partial | running image (slot0) modified, no upgrade | v1-tampered | v1-tampered | TP | jump |
| fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | v1 | TP | swap;jump |
| comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | accepted | TP | swap;jump |
| p5_inject | P5 | - | TLV injected in the unprotected area | v2 | v1 | TN | rejected;jump |
