#!/usr/bin/env bash
# Stage 5: re-measure every signature configuration that is possible on this platform
# (Zephyr 4.4 / Mbed TLS 4.x / TF-PSA-Crypto, STM32F429), including the three that
# failed in stage 3 and were fixed by configuration only.
# usage: scripts/run_stage5.sh <stage dir> <runs>
#   run inside tmux (takes about 30 minutes); progress goes to stdout
set -uo pipefail
source "$(dirname "$0")/env.sh"

STAGE=${1:?usage: $0 <stage dir> <runs>}
RUNS=${2:?}
[[ "$STAGE" = /* ]] || STAGE="$WS/$STAGE"
mkdir -p "$STAGE"

CONFS=(none
	rsa2048 rsa2048_psa
	rsa3072 rsa3072_psa_heap16k
	ecdsa_p256 ecdsa_p256_psa_heap ecdsa_p256_psa_heap_nistopt
	ed25519 ed25519_sha512 ed25519_pure_sha512)

echo "start $(date +%T)"
"$EXP/scripts/build_matrix.sh" "$STAGE/build_status.csv" "${CONFS[@]}"
echo "builds done $(date +%T)"
"$EXP/scripts/measure_matrix.sh" "$STAGE" "$RUNS"
echo "all done $(date +%T)"
