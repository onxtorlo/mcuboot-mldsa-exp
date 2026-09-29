#!/usr/bin/env bash
# Measure one bootloader build on the board and save every artifact in <outdir>.
# usage: scripts/measure_boot.sh <sig> <boot name> <runs> <outdir> [<boot name> ...]
#   e.g. scripts/measure_boot.sh rsa2048 rsa2048_measure 10 results/2026-09-30_stage2_rsa2048 rsa2048
#   <boot name>       build/boot_<name> to flash (must have CONFIG_BOOT_MEASURE_TIMING)
#   extra boot names  only recorded in build_size.csv for comparison
# needs: build/hello_v1/hello_v1_<sig>.bin and _bad_{payload,sig,key}.bin
#        (scripts/sign_app.sh, scripts/make_bad_images.sh); serial port free
#
# <outdir>/
#   meta.json            versions, commits, signed image layout
#   build_size.csv       bootloader text/data/bss, FLASH/RAM
#   boot_ok.csv          one row per valid boot (cycles per stage)
#   reject.csv           one row per rejection case
#   summary.md           tables built from the above
#   logs/                raw serial logs, one per boot
#   build_logs/          west build output of each bootloader
set -euo pipefail
source "$(dirname "$0")/env.sh"

SIG=${1:?usage: $0 <sig> <boot name> <runs> <outdir> [<boot name> ...]}
BOOT=${2:?}
RUNS=${3:?}
OUT=${4:?}
shift 4
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
IMG="$BUILD/hello_v1/hello_v1_$SIG.bin"
CAP=(python "$EXP/scripts/capture_boot.py" --seconds 10)

if [ -e "$OUT" ]; then
	echo "$OUT already exists; pick a new directory" >&2
	exit 1
fi
mkdir -p "$OUT/logs" "$OUT/build_logs"
for b in "$BOOT" "$@"; do
	cp "$BUILD/boot_$b.build.log" "$OUT/build_logs/" 2>/dev/null ||
		echo "warning: no build log for boot_$b (rebuild with scripts/build_boot.sh)" >&2
done

flash_fresh() {
	"$EXP/scripts/flash.sh" erase >/dev/null 2>&1
	"$EXP/scripts/flash.sh" boot "$BOOT" >/dev/null 2>&1
	"$EXP/scripts/flash.sh" slot0 "$1" >/dev/null 2>&1
}

echo "== valid image, $RUNS runs"
flash_fresh "$IMG"
for i in $(seq -w 1 "$RUNS"); do
	"${CAP[@]}" --label boot_ok --run "$i" --log "$OUT/logs/boot_ok_run$i.log" \
		--csv "$OUT/boot_ok.csv" | grep -E "MEAS (sig|result)" || true
done

for c in payload sig key; do
	echo "== reject: bad_$c"
	flash_fresh "$BUILD/hello_v1/hello_v1_${SIG}_bad_$c.bin"
	"${CAP[@]}" --label "bad_$c" --run 1 --log "$OUT/logs/reject_bad_$c.log" \
		--csv "$OUT/reject.csv" | grep -E "MEAS result" || true
done

echo "== restore valid image"
flash_fresh "$IMG"

BOOTS=(--boot "$BOOT")
for b in "$@"; do BOOTS+=(--boot "$b"); done
python "$EXP/scripts/report.py" meta "$OUT" --image "$IMG" "${BOOTS[@]}" >/dev/null
python "$EXP/scripts/report.py" summary "$OUT"
