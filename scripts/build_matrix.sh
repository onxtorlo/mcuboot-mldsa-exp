#!/usr/bin/env bash
# Build MCUboot for several configurations, with and without measurement,
# and record which ones build.
# usage: scripts/build_matrix.sh <status.csv> <conf>...
# status.csv columns: conf, variant (plain|measure), status (ok|fail), flash_used, ram_used, error
set -uo pipefail
source "$(dirname "$0")/env.sh"

STATUS=${1:?usage: $0 <status.csv> <conf>...}
shift
[[ "$STATUS" = /* ]] || STATUS="$WS/$STATUS"
[ -e "$STATUS" ] || echo "conf,variant,status,flash_used,ram_used,error" >"$STATUS"

for conf in "$@"; do
	for variant in plain measure; do
		extra=()
		name=$conf
		if [ $variant = measure ]; then
			extra=(measure)
			name=${conf}_measure
		fi
		log="$BUILD/boot_$name.build.log"
		if "$EXP/scripts/build_boot.sh" "$conf" "${extra[@]}" >/dev/null 2>&1; then
			flash=$(sed -n 's/^\s*FLASH:\s*\([0-9]*\) B.*/\1/p' "$log")
			ram=$(sed -n 's/^\s*RAM:\s*\([0-9]*\) B.*/\1/p' "$log")
			echo "$conf,$variant,ok,$flash,$ram," >>"$STATUS"
			echo "ok    $name  FLASH=$flash RAM=$ram"
		else
			# First compiler/linker/Kconfig error line, commas stripped for CSV
			err=$(grep -m1 -E "error:|Error:|overflowed|warning: .*(unmet|assigned)" "$log" | tr -d ',' | cut -c1-200)
			echo "$conf,$variant,fail,,,$err" >>"$STATUS"
			echo "FAIL  $name  $err"
		fi
	done
done
