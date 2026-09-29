#!/usr/bin/env bash
# Sign, make bad images and measure every configuration that built (build_matrix.sh),
# then write the comparison table.
# usage: scripts/measure_matrix.sh <stage dir> <runs> [<conf>...]
#   <stage dir>/build_status.csv from build_matrix.sh; confs default to all that built
#   results go to <stage dir>/<conf>/ (see measure_boot.sh), then compare.py
set -uo pipefail
source "$(dirname "$0")/env.sh"

STAGE=${1:?usage: $0 <stage dir> <runs> [<conf>...]}
RUNS=${2:?}
shift 2
[[ "$STAGE" = /* ]] || STAGE="$WS/$STAGE"

# Configurations whose plain and measure builds both succeeded
mapfile -t BUILT < <(awk -F, 'NR > 1 && $3 == "ok" {n[$1]++} END {for (c in n) if (n[c] == 2) print c}' \
	"$STAGE/build_status.csv" | sort)
CONFS=("$@")
[ ${#CONFS[@]} -eq 0 ] && CONFS=("${BUILT[@]}")

"$EXP/scripts/build_app.sh" v1 >/dev/null 2>&1 || { echo "app build failed" >&2; exit 1; }

for conf in "${CONFS[@]}"; do
	if [[ ! " ${BUILT[*]} " =~ " $conf " ]]; then
		echo "skip $conf (did not build)"
		continue
	fi
	if [ -e "$STAGE/$conf" ]; then
		echo "skip $conf (already measured)"
		continue
	fi
	echo "######## $conf"
	"$EXP/scripts/sign_app.sh" "$conf" v1 1.0.0 >/dev/null &&
		"$EXP/scripts/make_bad_images.sh" "$conf" v1 >/dev/null &&
		"$EXP/scripts/measure_boot.sh" "$conf" "${conf}_measure" "$RUNS" "$STAGE/$conf" "$conf" |
		grep -E "^==|MEAS result" | uniq -c ||
		echo "measure failed: $conf"
done

python "$EXP/scripts/compare.py" "$STAGE" >/dev/null && echo "comparison: $STAGE/comparison.md"
