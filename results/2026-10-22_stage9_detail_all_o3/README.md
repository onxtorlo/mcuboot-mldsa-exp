# 2026-10-22_stage9_detail_all_o3

**Final comparison basis (decided 2026-10-22): these -O3 builds** (the fastest of the
measured options). Quote sig/total ms from `<conf>_measure_opt_o3`. The -Os run in
../2026-10-22_stage9_detail_all stays for the primitive-level breakdown (no -O3 prims
builds) and continuity with stages 1-8.

Supplement to ../2026-10-22_stage9_detail_all: the same 9 configurations with the whole
bootloader built at -O3 (boot_conf/opt_o3.conf), stages + steps only. Tables and
comparison with -Os: ../2026-10-22_stage9_detail_all/summary.md section 9; notes:
../2026-10-22_stage9_detail_all/notes.md ("-O3 supplement"). Per-build tables: detail.md.

## Commit hashes in the records (rebased before push)

meta.json / per-build summary.md name exp commits as they were when measured. Before
pushing, these commits were rebased onto 3b565d2 (stage 5/6 logs, other PC; no file in
common), so they have new ids with the same changes:
b4fb053 -> d910341, 00476a4 -> fcb6daa, 2ba3097 -> ced8a8a.
