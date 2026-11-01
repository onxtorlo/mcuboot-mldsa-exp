#!/usr/bin/env bash
# Re-run step 4 (board PoCs) of an existing chkup.sh run with the current validator, reusing
# its static verdicts and the flashable bootloader builds; then rewrite report.md.
# usage: scripts/chkup_revalidate.sh <outdir> <conf> <build>...   (build = name under static/)
#   old poc/<build> is replaced (the previous run is kept in poc/<build>.old until success)
set -uo pipefail
source "$(dirname "$0")/env.sh"

OUT=${1:?usage: $0 <outdir> <conf> <build>...}
CONF=${2:?}
shift 2
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
exec > >(tee -a "$OUT/run.log") 2>&1
echo "chkup_revalidate.sh $CONF $* ($(date -Is))"
for n in "$@"; do
	echo "== revalidate $n"
	[ -d "$BUILD/boot_$n" ] || { echo "   no flashable build boot_$n"; continue; }
	[ -d "$OUT/poc/$n" ] && mv "$OUT/poc/$n" "$OUT/poc/$n.old"
	if python3 "$EXP/scripts/chkup_validate.py" "$CONF" "$n" "$OUT/static/$n/verdict.json" \
		"$OUT/poc/$n" --negative; then
		rm -rf "$OUT/poc/$n.old"
	else
		echo "   board validation incomplete (previous result in poc/$n.old)"
	fi
done
python3 "$EXP/scripts/chkup_report.py" "$OUT"
