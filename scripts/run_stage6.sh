#!/usr/bin/env bash
# Stage 6: ML-DSA as the MCUboot image signature (all three parameter sets, default and
# reduced-RAM builds): build, measure boot timing + rejections, then the full boot /
# upgrade / rejected-upgrade flow. RSA-2048 runs the same flow as a baseline.
# usage: scripts/run_stage6.sh <stage dir> <runs>
#   run inside tmux; progress goes to stdout
set -uo pipefail
source "$(dirname "$0")/env.sh"

STAGE=${1:?usage: $0 <stage dir> <runs>}
RUNS=${2:?}
[[ "$STAGE" = /* ]] || STAGE="$WS/$STAGE"
mkdir -p "$STAGE"

CONFS=(mldsa44 mldsa65 mldsa87 mldsa44_lowram mldsa65_lowram mldsa87_lowram)

echo "start $(date +%T)"
"$EXP/scripts/build_matrix.sh" "$STAGE/build_status.csv" "${CONFS[@]}" rsa2048
echo "builds done $(date +%T)"
"$EXP/scripts/build_app.sh" v2 >/dev/null 2>&1 || { echo "app v2 build failed" >&2; exit 1; }
"$EXP/scripts/measure_matrix.sh" "$STAGE" "$RUNS" "${CONFS[@]}"
for conf in "${CONFS[@]}" rsa2048; do
	echo "######## flow $conf"
	"$EXP/scripts/flow_test.sh" "$conf" "${conf}_measure" "$STAGE/flow/$conf"
done
echo "all done $(date +%T)"
