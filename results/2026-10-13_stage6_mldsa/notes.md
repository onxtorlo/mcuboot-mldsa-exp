# Notes: 2026-10-13_stage6_mldsa (ML-DSA as the MCUboot image signature)

MCUboot fork `sign-replace` @ e0e92c72 (v2.4.0 + timing + ML-DSA): the image hash
(SHA-256 TLV) is signed with ML-DSA-44/65/87 (empty context) by imgtool and verified
in MCUboot with mldsa-native (portable C, -Os). Public key embedded raw (FIPS 204).
Signature TLVs 0x26/0x27/0x28 (experimental ids, not assigned upstream).
Each configuration: 10 boots + bad payload / bad signature / wrong key, then
`flow/<conf>/`: boot v1, upgrade to v2 through slot1 (swap-using-scratch), reboot,
and two upgrades that must be refused (bad payload, wrong key). RSA-2048 runs the
same flow as a baseline.

## Results

| Configuration | sig ms | stack peak (B) | MCUboot RAM (B) | FLASH (B) |
|---|---|---|---|---|
| mldsa44 | 17.26 | 47,144 | 65,344 | 37,288 |
| mldsa44_lowram | 17.04 | 27,304 | 44,864 | 36,824 |
| mldsa65 | 29.48 | 71,680 | 89,920 | 38,032 |
| mldsa65_lowram | 28.29 | 36,480 | 53,056 | 37,264 |
| mldsa87 | 50.15 | 110,112 | 126,784 | 38,424 |
| mldsa87_lowram | 47.65 | 48,288 | 65,344 | 37,944 |

For comparison (stage 5, same board/image): Ed25519 24.05 ms, RSA-2048 52.49 ms,
RSA-3072 103.99 ms, ECDSA P-256 TinyCrypt 107.89 ms.

- Inside MCUboot the verify times match the standalone benchmark (stage 4: 17.76 /
  29.31 / 49.57 ms), so MCUboot adds no overhead beyond hashing.
- ML-DSA-44 verifies faster than Ed25519, ML-DSA-87 about as fast as RSA-2048.
- `MLD_CONFIG_REDUCE_RAM` cuts the stack peak by 42-56 % and is not slower here
  (slightly faster). It is marked experimental in mldsa-native (not covered by its
  CBMC proofs). Recommended setting on RAM-limited parts.
- Stack: measured peak = mldsa-native MLD_TOTAL_ALLOC_*_VERIFY + signature buffer
  (in bootutil_img_validate) + ~6 KB MCUboot. The build checks MAIN_STACK_SIZE
  against that sum + 8 KB. The first run used +4 KB and left only 2 KB headroom for
  ML-DSA-44, so the configs were raised (56/80/116 KB, lowram 36/44/56 KB).
- FLASH: MCUboot with ML-DSA is ~37-38 KB, smaller than Ed25519 (42 KB), similar to RSA (37 KB).
- Image overhead: TLV area 2.5 / 3.4 / 4.7 KB (vs 144 B Ed25519, 336 B RSA-2048).

## Issues found on the way

- First run: every image rejected (`result=other`, log "TLV 38 not permitted"): the
  unprotected-TLV allow list in image_validate.c (`allowed_unprot_tlvs`) did not include
  the new signature TLVs. Fixed in the fork before this run.

## Not covered

- Image encryption (key exchange is still RSA/ECIES; ML-KEM is not integrated).
- Hardware keys / builtin keys, ML-DSA pure (signature over the whole image),
  serial recovery. Side-channel / fault-injection hardening of mldsa-native.
