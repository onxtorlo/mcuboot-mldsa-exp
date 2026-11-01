# ChkUp step 4 — boot_mldsa65_chkup_overwrite_chkup_dgp

alerts: 1 -> TP 1, FP 0; negative checks -> TN 10, FN 0

| case | property | alert | PoC | attack succeeds if | observed | result | MCUboot log |
|---|---|---|---|---|---|---|---|
| baseline | baseline | - | legitimate upgrade v1/cnt1 -> v2/cnt5 | v2 | v2 | ok | jump |
| comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | accepted | TP | jump |
| auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v2 | v1 | TN | rejected;jump |
| auth_wrongkey | authenticity | - | signed with another key of the same type | v2 | v1 | TN | rejected;jump |
| slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | v1-tampered | none | TN | rejected;no-bootable |
| integ_modified | integrity | - | payload modified, nothing else | v2-tampered | v1 | TN | rejected;jump |
| integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v2-tampered | v1 | TN | rejected;jump |
| fresh_older | freshness | - | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | v2 | TN | jump |
| fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v1 | v2 | TN | rejected;jump |
| p5_inject | P5 | - | TLV injected in the unprotected area | v2 | v1 | TN | rejected;jump |
| p6_equal_counter | P6 | - | older image with the same security counter (5 -> 5) | v1 | v2 | TN | jump |
| p6_unprot_counter | P6 | - | older image cnt1 + SEC_CNT=10 in the unprotected area | v1 | v2 | TN | jump |
