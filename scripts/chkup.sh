#!/usr/bin/env bash
# ChkUp for MCUboot, end to end: for each Kconfig variant build -> steps 1-3 (static) ->
# step 4 (board PoCs chosen from the alerts) -> one report.
# usage: scripts/chkup.sh <conf> <outdir> [--board] [--negative] [variant...]
#   conf     boot_conf/<conf>.conf (signature), e.g. mldsa65
#   outdir   relative to the west workspace, e.g. mcuboot-mldsa-exp/results/<date>_chkup
#   variant  base (no extra fragment), <v> = boot_conf/chkup_<v>.conf, or a+b for several;
#            default: base dgp dgp_seccnt hwdgp noval0 noallow
#   --board     run step 4 on the board (serial port free, ST-Link attached to WSL)
#   --negative  step 4 also runs PoCs for properties without an alert (finds false negatives)
# output: <outdir>/static/<build>/ (verdict.*), poc/<build>/ (validation.*), report.md, run.log
set -uo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> <outdir> [--board] [--negative] [variant...]}
OUT=${2:?}
shift 2
BOARD_RUN=0
NEG=()
VARIANTS=()
for x in "$@"; do
	case "$x" in
	--board) BOARD_RUN=1 ;;
	--negative) NEG=(--negative) ;;
	*) VARIANTS+=("$x") ;;
	esac
done
[ ${#VARIANTS[@]} -gt 0 ] || VARIANTS=(base dgp dgp_seccnt hwdgp noval0 noallow)
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
if [ -e "$OUT" ]; then
	echo "$OUT already exists; pick a new directory" >&2
	exit 1
fi
mkdir -p "$OUT/static" "$OUT/poc"
exec > >(tee -a "$OUT/run.log") 2>&1
echo "chkup.sh $CONF $* ($(date -Is))"

if [ $BOARD_RUN = 1 ]; then  # applications used by the PoCs
	[ -f "$BUILD/hello_v1/zephyr/zephyr.bin" ] || "$EXP/scripts/build_app.sh" v1 >/dev/null
	[ -f "$BUILD/hello_v2/zephyr/zephyr.bin" ] || "$EXP/scripts/build_app.sh" v2 >/dev/null
	[ -f "$BUILD/hello_nucleo/zephyr/zephyr.bin" ] ||
		west build -p -b nucleo_f429zi "$EXP/apps/hello" -d "$BUILD/hello_nucleo" -- -DAPP_TAG=other \
			-DEXTRA_DTC_OVERLAY_FILE="$EXP/apps/hello/drop_partitions.overlay;$PART_OVERLAY;$EXP/apps/hello/slot0.overlay" >/dev/null
fi

for v in "${VARIANTS[@]}"; do
	FRAGS=()
	if [ "$v" != base ]; then
		IFS=+ read -r -a parts <<<"$v"
		for p in "${parts[@]}"; do FRAGS+=("chkup_$p"); done
	fi
	NAME="$CONF"
	for f in "${FRAGS[@]}"; do NAME+="_$f"; done
	echo "== $v ($NAME)"

	# steps 1-3 on the analysis build (a link failure still leaves every compiled object)
	"$EXP/scripts/build_boot.sh" "$CONF" "${FRAGS[@]}" callgraph >/dev/null 2>&1 ||
		echo "   analysis build did not link (see build/boot_${NAME}_callgraph.build.log)"
	if ! python3 "$EXP/scripts/chkup_analyze.py" "$BUILD/boot_${NAME}_callgraph" \
		--out "$OUT/static/$NAME" | sed -n '/^| property/,$p'; then
		echo "   static analysis failed"
		continue
	fi
	[ $BOARD_RUN = 1 ] || continue

	# step 4 on a normal (flashable) build
	if ! "$EXP/scripts/build_boot.sh" "$CONF" "${FRAGS[@]}" >/dev/null 2>&1; then
		echo "   not flashable (build failed) -> no board validation"
		echo "build failed" >"$OUT/static/$NAME/not_flashable"
		continue
	fi
	python3 "$EXP/scripts/chkup_validate.py" "$CONF" "$NAME" "$OUT/static/$NAME/verdict.json" \
		"$OUT/poc/$NAME" "${NEG[@]}" || echo "   board validation incomplete"
done

python3 "$EXP/scripts/chkup_report.py" "$OUT"
echo "report: $OUT/report.md"
