# Notes: 2026-10-22_stage8_ecdsa_detail

## Setup

- MCUboot `sign-replace` @ e0e92c72 + uncommitted TinyCrypt instrumentation (committed
  later as 6a809c68 together with the hooks for the other algorithms and the nesting
  depth counter); exp `dev` @ a6fca6b +
  uncommitted `boot_conf/{sig_detail,sig_prims,opt_o2,opt_o3,opt_lto}.conf`,
  `scripts/detail_report.py`, `SKIP_REJECT` in `measure_boot.sh`. meta.json therefore
  records a dirty tree for this stage.
- Laptop PC, image and keys from stage 7 (2026-10-19), not re-signed: the ECDSA
  signature is the same, so stage 7 and 8 sig cycles are directly comparable
  (-Os baseline 18,150,957 cycles in both).
- Builds (`scripts/build_boot.sh ecdsa_p256 measure [sig_detail [sig_prims]] [opt_*]`):
  12 = {-Os, -O2, -O3, LTO} x {measure, +sig_detail, +sig_detail+sig_prims}.
  Rejection cases only on the plain `measure` builds (`SKIP_REJECT=1` on the others).

## How the counters work

- `MEAS` lines: unchanged stage counters (total / validate / hash / sig).
- `MEASD` lines: new. Cleared when the `sig` stage starts, so they describe the last
  signature check. `sum_cyc` = total cycles over all `n` calls.
  - `CONFIG_BOOT_MEASURE_SIG_DETAIL`: steps (`ecdsa.verify.*`), one start/stop pair per
    step, plus one per loop iteration (dbl/add). Inline DWT reads.
  - `CONFIG_BOOT_MEASURE_SIG_PRIMS`: primitives (`tc.*`), counted on every call.
- Steps nest: `ecdsa.verify.loop` contains `.loop.dbl` and `.loop.add`.
  Primitives nest too: `tc.xycz_add` / `tc.apply_z` / `tc.double_jacobian` contain
  `tc.vli_mult` + `tc.mmod_fast`. Do not add rows across nesting levels.
- "(rest of sig)" in detail.md = sig stage minus the top-level steps (key parse, sig
  decode, verify): ~300 cycles of glue.

## Instrumentation cost

- detail builds: -Os 18,114,764 vs 18,150,957 cycles (-0.2 %, i.e. faster: code layout);
  -O2 +0.4 %, -O3 +0.2 %, LTO +0.3 %. Negligible; step numbers can be used as they are.
- prims builds: +4.5 % (-Os), +2.7 % (-O2), +3.1 % (-O3), +5.0 % (LTO). Use these only
  for shares and per-call costs, not for absolute time.
- After this stage the accumulator gained a nesting depth (so recursive / shared ids are
  timed once). Stage 8 ran before that change; it does not affect stage 8 because no
  TinyCrypt id is entered twice.

## Observations

- Loop counts: 255 doublings (num_bits - 1 of max(u1, u2) bit length = 256) and 195
  additions (bits where u1 or u2 is set: ~3/4 of 256 for random scalars). These depend
  on the signature (u1, u2), so another signature gives slightly different numbers
  (stage 5 vs 7: 107.89 vs 108.04 ms).
- One addition costs more than one doubling (43.7k vs 33.3k cycles at -Os) because each
  addition first converts the stored affine point to the current Z (`apply_z`, 4 field
  multiplications) before the co-Z addition (`XYcZ_add`, 6) and the Z update (1).
- `vli_mmod_fast_secp256r1` is more expensive than the multiplication at -Os
  (2,246 vs 1,571 cycles): it calls `uECC_vli_add`/`uECC_vli_sub` (8-word loops) as
  out-of-line functions ~8 times per reduction. At -O3 they are inlined: 847 cycles.
  This is where most of the -O2/-O3 gain comes from.
- The 32x32->64 multiply-accumulate loop (`muladd`) is ~1,450 cycles at every level.
  A Cortex-M4 UMAAL assembly multiply would be the next step, but that is a code change,
  not a build option (TinyCrypt dropped micro-ecc's assembly).
- LTO alone does nothing for ECDSA (-0.5 %): TinyCrypt's hot code is already in one file
  (ecc.c); it only shrinks FLASH (-3.8 KB).
- hash ms moves with the build (-Os 9.83, -O2 8.81, -O3 9.42, LTO 10.13 ms) although the
  SHA-256 code is the same source; consistent with the stage 7 note that hash time
  depends on code placement per build. Not investigated further.

## Caveats

- -O3 build: GCC warns `'t5' may be used uninitialized` in `ecc.c:382`
  (`uECC_vli_modSquare_fast`, inlined into `XYcZ_add`). Not seen at -Os/-O2. The value
  is written by `uECC_vli_modSub` before use; looks like a -O3 inlining false positive
  (not proven). The valid image verifies and all three bad images are rejected.
- Compiler options apply to the whole bootloader, so they speed up RSA, Ed25519 and
  ML-DSA as well. Comparing algorithms needs the same option for all of them.
- FLASH in the table is for the measure builds (instrumentation included, +~0.7 KB).
