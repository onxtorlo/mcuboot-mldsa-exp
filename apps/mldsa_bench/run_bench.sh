#!/usr/bin/env bash
# Generate a vector, build, flash and measure the ML-DSA verify benchmark for one level.
# usage: apps/mldsa_bench/run_bench.sh <44|65|87> <outdir> [main stack bytes]
#   outdir gets logs/, bench.csv, summary.md, bench_vectors.h, the build log
set -euo pipefail
source "$(dirname "$0")/../../scripts/env.sh"

LEVEL=${1:?usage: $0 <44|65|87> <outdir> [main stack bytes]}
OUT=${2:?}
STACK=${3:-65536}
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
APP="$EXP/apps/mldsa_bench"
BDIR="$BUILD/mldsa_bench_$LEVEL"

if [ -e "$OUT" ]; then
	echo "$OUT already exists; pick a new directory" >&2
	exit 1
fi
mkdir -p "$OUT/logs" "$BDIR"

python "$APP/gen_vectors.py" "$BUILD/hello_v1/zephyr/zephyr.bin" "$BDIR/bench_vectors.h" "$LEVEL"
cp "$BDIR/bench_vectors.h" "$OUT/"
west build -p -b "$BOARD" "$APP" -d "$BDIR/build" -- -DMLDSA_LEVEL="$LEVEL" \
	-DBENCH_VECTORS="$BDIR/bench_vectors.h" -DCONFIG_MAIN_STACK_SIZE="$STACK" \
	>"$OUT/mldsa_bench.build.log" 2>&1
grep -E "^\s+(FLASH|RAM):" "$OUT/mldsa_bench.build.log"
west flash -d "$BDIR/build" --runner openocd >/dev/null 2>&1

for i in 1 2 3; do
	python "$EXP/scripts/capture_boot.py" --seconds 30 --label "mldsa${LEVEL}_bench" \
		--run "$i" --log "$OUT/logs/bench_boot$i.log" >/dev/null
done
python "$APP/parse_bench.py" "$OUT"
