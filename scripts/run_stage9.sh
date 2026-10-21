#!/usr/bin/env bash
# Stage 9: where the verification time goes, for every working signature backend.
# Each configuration is measured as three bootloader builds:
#   <conf>_measure                      stages only (+ bad image rejections)
#   <conf>_measure_sig_detail           + steps inside the signature check
#   <conf>_measure_sig_detail_sig_prims + arithmetic primitives (slower; for shares)
# Images: build/hello_v1/hello_v1_<KEY>.bin (the "# KEY=" of the conf), so backends
# of the same algorithm verify the very same signed image.
# usage: [VARIANTS="..."] scripts/run_stage9.sh <stage dir> <runs> [<conf>...]
#   VARIANTS: build name suffixes, e.g. "measure_opt_o3 measure_sig_detail_opt_o3"
#   builds must exist (scripts/build_boot.sh <conf> measure [sig_detail [sig_prims]])
#   run inside tmux; progress goes to stdout
set -uo pipefail
source "$(dirname "$0")/env.sh"

STAGE=${1:?usage: $0 <stage dir> <runs> [<conf>...]}
RUNS=${2:?}
shift 2
[[ "$STAGE" = /* ]] || STAGE="$WS/$STAGE"
CONFS=("$@")
[ ${#CONFS[@]} -eq 0 ] && CONFS=(ecdsa_p256 ecdsa_p256_psa_heap ecdsa_p256_psa_heap_nistopt
	rsa2048 rsa2048_psa ed25519 mldsa44 mldsa65 mldsa87)
mkdir -p "$STAGE"
VARIANTS=${VARIANTS:-measure measure_sig_detail measure_sig_detail_sig_prims}

echo "start $(date +%T)"
DIRS=()
for conf in "${CONFS[@]}"; do
	key=$(conf_get "$conf" KEY)
	for v in $VARIANTS; do
		b="${conf}_$v"
		DIRS+=("$STAGE/$b")
		if [ -e "$STAGE/$b" ]; then
			echo "skip $b (already measured)"
			continue
		fi
		echo "######## $b ($(date +%T))"
		skip=1
		[[ "$v" != *sig_* ]] && skip=   # rejections on the build without MEASD counters
		SKIP_REJECT=$skip "$EXP/scripts/measure_boot.sh" "$key" "$b" "$RUNS" "$STAGE/$b" |
			grep -E "^==|MEAS result" | uniq -c || echo "measure failed: $b"
	done
done
python "$EXP/scripts/detail_report.py" "$STAGE" "${DIRS[@]}" >/dev/null &&
	echo "detail: $STAGE/detail.md"
echo "all done $(date +%T)"
