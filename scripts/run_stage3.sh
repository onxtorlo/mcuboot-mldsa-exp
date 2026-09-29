#!/usr/bin/env bash
# Stage 3: build every MCUboot v2.4.0 signature configuration and measure the ones that build.
# usage: scripts/run_stage3.sh <stage dir> <runs>
#   run inside tmux (takes about an hour); progress goes to stdout
set -uo pipefail
source "$(dirname "$0")/env.sh"

STAGE=${1:?usage: $0 <stage dir> <runs>}
RUNS=${2:?}
[[ "$STAGE" = /* ]] || STAGE="$WS/$STAGE"
mkdir -p "$STAGE"

CONFS=(none
	rsa2048 rsa2048_mbedtls rsa2048_psa
	rsa3072 rsa3072_mbedtls rsa3072_psa
	ecdsa_p256 ecdsa_p256_mbedtls ecdsa_p256_psa ecdsa_p256_psa_sha512
	ed25519 ed25519_mbedtls ed25519_psa ed25519_sha512
	ed25519_pure ed25519_pure_mbedtls ed25519_pure_psa
	ecdsa_p256_psa_fix ecdsa_p256_psa_sha512_fix ed25519_psa_fix ed25519_pure_psa_fix
	ecdsa_p256_mbedtls_fix ed25519_mbedtls_fix)

echo "start $(date +%T)"
"$EXP/scripts/build_matrix.sh" "$STAGE/build_status.csv" "${CONFS[@]}"
echo "builds done $(date +%T)"
"$EXP/scripts/measure_matrix.sh" "$STAGE" "$RUNS"
echo "all done $(date +%T)"
