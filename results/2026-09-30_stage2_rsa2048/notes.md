# Notes: 2026-09-30_stage2_rsa2048

Purpose: check the boot timing instrumentation (CONFIG_BOOT_MEASURE_TIMING)
with RSA-2048 before measuring other algorithms. Re-run of the first
check done earlier the same day, this time with every artifact saved.

## Reading the numbers

- Cycles come from the Cortex-M4 DWT counter at 168 MHz; ms = cycles / 168,000.
- `total` = bootloader `main()` entry until `boot_go()` returns. It includes
  UART log output at 115200 baud and excludes Zephyr kernel init before
  `main()`. Use `sig` and `validate` to compare algorithms.
- `hash` scales with image size; the test image payload is 17,456 B.
- Within one bootloader build every run gives the same cycle count (stdev 0).
- Between builds the count can shift slightly even when the measured code is
  the same. The first check (MCUboot banner `v2.4.0`) gave sig = 8,817,413 and
  hash = 1,816,559 cycles; this run (banner `v2.4.0-1-g155e48c2a3d5`, 16 B
  longer, nothing else changed) gives 8,815,930 and 1,818,252 (~0.02-0.1 %).
  Likely flash/cache alignment. Compare algorithms using numbers from builds
  made the same way, and treat differences of this size as noise.

## Known issues

- `time` in the CSVs and the `# captured` line in the logs use the WSL clock,
  which was being corrected during the run (jumps of ~10 s). Order runs by
  `run`, not by `time`. The cycle counts are unaffected.
- `meta.json` field `zephyr.version` was added after the run (the shallow
  west checkout has no git tags); everything else in it was written at the
  end of the run.
