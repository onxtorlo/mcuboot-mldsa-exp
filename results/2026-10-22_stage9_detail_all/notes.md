# Notes: 2026-10-22_stage9_detail_all

## Setup

- MCUboot `sign-replace` @ 6a809c68 (measurement hooks for TinyCrypt ECDSA, RSA/PSA glue,
  Ed25519/fiat). exp `dev` @ b4fb053 for the main run, @ 00476a4 for the two
  remeasured PSA ECDSA detail builds and the -O3 set (`..._o3/`).
- tf-psa-crypto (dc575a2) and mldsa-native (3fc1998) carry local hooks:
  `patches/*.diff`. meta.json of every build records them (`tf_psa_crypto`,
  `mldsa_native`: commit, dirty, diff_sha1).
- Signed images: stage 7 images (2026-10-19, laptop keys), not re-signed. `run_stage9.sh`
  picks `hello_v1_<KEY>.bin`, so `ecdsa_p256`, `_psa_heap`, `_psa_heap_nistopt` verify
  the same ECDSA signature and `rsa2048` / `rsa2048_psa` the same RSA signature.
- 9 configurations: one per working backend/option. Left out to save board time
  (same code paths as a measured one): rsa3072, rsa3072_psa_heap16k (larger key),
  ed25519_sha512, ed25519_pure_sha512 (other image hash), ML-DSA `_lowram` (A sampled
  inside the matrix product instead of up front, so `expand_a` would read ~0), none.
- Per configuration 3 builds (`_measure`, `_measure_sig_detail`,
  `_measure_sig_detail_sig_prims`), 10 boots each; bad image rejections on `_measure`
  only (all 9: bad payload -> hash_mismatch, bad signature -> bad_sig, wrong key ->
  no_key).

## Reading the tables

- "% of sig" uses the sig stage of the same build.
- Steps nest (`x.verify` > `x.verify.loop` > `x.verify.loop.dbl`); primitives nest
  (`ecp.mul_mod` = `mpi.mul_mpi` + `ecp.modp` + call overhead). Do not add rows across
  levels. "(rest of sig)" = sig - top-level steps (one dot, e.g. `rsa.public`).
- An id entered again before it is left is timed once (depth counter) but every call is
  counted: e.g. `ecp.normalize` n=5 includes nested `normalize_jac_many` ->
  `normalize_jac` calls.
- `mld.poly_uniform` counts calls of `mld_poly_uniform_4x` (4 polynomials) and
  `mld_poly_uniform` (1) alike: 44 = 4 x 4x; 65 = 7 x 4x + 2 x 1; 87 = 14 x 4x.
- `mld.keccakf1600` counts single permutations (the x4 variant calls it 4 times).
- RSA PSA: MGF1 / H' are inside `psa_verify_hash`, not separately timed.

## Issues during the run (all handled, nothing silently dropped)

1. `mbecdsa.verify` (whole `mbedtls_ecdsa_verify_restartable`) was wrapped with the
   primitive macros, so in the first `_sig_detail` builds of both PSA ECDSA
   configurations it was missing (only that row; all step rows were right). Fixed in
   the patch (exp 00476a4), both detail builds rebuilt and remeasured; the first runs
   are kept as `*_sig_detail.pre_fix/` (the nistopt one had in fact already been rebuilt
   with the fix when it was flashed, see "Flashing rebuilds" below).
2. `ecdsa_p256_psa_heap_nistopt_measure_sig_detail_sig_prims` run 01: the serial capture
   stopped early (it saw the previous boot's "Hello World" right after flashing), so the
   log has no MEAS lines. 9 valid runs remain (deterministic, identical cycles);
   `detail_report.py` lists such logs as incomplete instead of averaging them as 0
   (fixed in 00476a4; the first stage-9 detail.md before the fix was regenerated).
3. Counting cost of the primitives level rose after the nesting-depth counter was added:
   TinyCrypt ECDSA prims build +6.5 % here vs +4.5 % in stage 8. Step-level numbers are
   unaffected (both within 0.2 % of the plain build).

## Observations that need care when quoting

- ECDSA over PSA without NIST reduction: 2,207.5 ms here vs 2,139.3 ms in stage 5, with
  NIST: 351.0 vs 360.5 ms. Stage 5 used a separately signed image (other r, s), here
  the TinyCrypt image; scalar bit patterns change the comb work.
- RSA verify spends 38 % recomputing R² mod N because MCUboot builds a fresh
  `mbedtls_rsa_context` per verification. Caching R² with the key (or embedding it)
  would remove ~20 ms; this is a property of the glue code, not of RSA.
- The PSA ECDSA backend builds the comb table for Q on every verify (39 %) and uses
  binary-GCD inversions (35 % with NIST reduction). Both are generic-library choices.
- ML-DSA is dominated by Keccak; a faster Keccak-f1600 (Cortex-M4 assembly versions
  exist, e.g. in XKCP / pqm4; not tried here) would move all three parameter sets the most.
- hash ms differs per build (9.8-11.6 ms) for the same image and code (see stage 7/8).

## Flashing rebuilds from the current sources (found during this stage)

- `scripts/flash.sh boot` calls `west flash -d build/boot_<name>`, which first runs ninja:
  if a source changed after the build, the binary is rebuilt at flash time.
- Here: the counter fix in tf-psa-crypto `ecdsa.c` was saved at 02:50:30 while the run
  was going. `ecdsa_p256_psa_heap_nistopt_measure_sig_detail` was flashed at 02:51:57 and
  so was rebuilt with the fix (its results show 52,908 B FLASH vs 52,876 B when built,
  and its `.pre_fix` logs equal the remeasured logs line for line). The generic PSA
  detail build was flashed at 02:44 (before the fix) and really lacked the counter.
  The nistopt `_measure` (02:51) and `_sig_detail_sig_prims` (02:54) builds were also
  rebuilt, but for them the fix compiles to the same code (both macro kinds are empty in
  `_measure` and both active in `_prims`). No other stage 9 build compiles `ecdsa.c`
  after the fix (checked the object file times of all builds).
- Proposal (not applied): `west flash --skip-rebuild` in flash.sh, or never edit
  sources while a run is in progress (what I will do from now on).

## Code placement effect (measured)

- Generic PSA ECDSA detail build before/after the fix differ only by one counter pair
  (+32 B): 2,208.606 -> 2,135.929 ms (-3.3 %). The same bignum routine (1/s mod n) is
  3,590,882 vs 3,463,502 cycles in these two builds. So for the large Mbed TLS builds,
  absolute times move by about +-3 % with unrelated code changes. Small builds
  (TinyCrypt, RSA, ML-DSA, Ed25519) moved by <= 0.9 % between `_measure` and
  `_sig_detail`.
- Consequence: quote absolute ms from `_measure` builds; take shares from detail builds;
  differences under ~3 % between PSA builds are not meaningful.

## -O3 supplement (`2026-10-22_stage9_detail_all_o3/`)

- Builds `<conf>_measure_opt_o3` (+ rejections) and `<conf>_measure_sig_detail_opt_o3`,
  10 boots each, exp 00476a4. `VARIANTS="measure_opt_o3 measure_sig_detail_opt_o3"
  scripts/run_stage9.sh ...`.
- Only TinyCrypt `ecc.c` warns at -O3 (`'t5' may be used uninitialized`, see stage 8);
  all other -O3 builds have no warnings.
- No primitives builds at -O3 (board time); the ML-DSA Keccak slowdown at -O3 is seen
  in the steps (expand A, mu, c hash all slower) but its per-call cost was not measured.
