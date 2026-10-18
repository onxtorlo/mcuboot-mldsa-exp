# Notes: 2026-10-19_stage7_compare (ML-DSA vs existing signatures, one session)

Representative configurations only: the MCUboot default backend of each existing
algorithm (RSA-2048 legacy, ECDSA P-256 TinyCrypt, Ed25519 over SHA-256) and the three
ML-DSA parameter sets (default RAM mode). Same session, same app image, same build tree:
exp 58f0823, MCUboot sign-replace e0e92c72, laptop (keys generated on this PC; ML-DSA
keys created 2026-10-19). 10 boots + bad payload / bad signature / wrong key each.

## Agreement with stage 5/6 (2026-10-13, lab PC)

- sig ms identical within 0.01 ms for RSA-2048, Ed25519, ML-DSA-44/65/87
  (verification is deterministic; the keys differ but the work does not).
- ECDSA P-256 108.04 ms vs 107.89 ms: the image was re-signed with a different key and
  a new random nonce, so the scalar bit patterns differ.
- MCUboot FLASH +16 B for every configuration (version/banner strings), RAM identical.

## Observed, not explained

- hash ms is ~10.8 ms for rsa2048 and mldsa87 but ~9.8-9.9 ms for the others, with the
  same image. Same pattern on 10/13. Likely code placement (flash/ART cache alignment of
  the SHA-256 routine) in each build; not verified.
