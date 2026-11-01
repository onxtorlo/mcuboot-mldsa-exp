# ChkUp step 4 — boot_mldsa65

alerts: 2 -> TP 2, FP 0; negative checks -> TN 6, FN 0

| case | property | alert | PoC | attack succeeds if | observed | result | MCUboot log |
|---|---|---|---|---|---|---|---|
| baseline | baseline | - | legitimate upgrade v1/cnt1 -> v2/cnt5 | v2 | v2 | ok | swap;jump |
| fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | v1 | TP | swap;jump |
| comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | accepted | TP | swap;jump |
| auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v2 | v1 | TN | rejected;jump |
| auth_wrongkey | authenticity | - | signed with another key of the same type | v2 | v1 | TN | rejected;jump |
| slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | v1-tampered | none | TN | rejected;no-bootable |
| integ_modified | integrity | - | payload modified, nothing else | v2-tampered | v1 | TN | rejected;jump |
| integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v2-tampered | v1 | TN | rejected;jump |
| p5_inject | P5 | - | TLV injected in the unprotected area | v2 | v1 | TN | rejected;jump |
