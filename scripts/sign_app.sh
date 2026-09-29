#!/usr/bin/env bash
# Sign a built application image with imgtool from our MCUboot fork.
# usage: scripts/sign_app.sh <conf> <tag> <version> [upgrade]
#   e.g. rsa2048 v1 1.0.0          -> for slot0
#        rsa2048 v2 2.0.0 upgrade  -> for slot1, padded + confirmed (permanent swap)
#   key and extra imgtool arguments come from boot_conf/<conf>.conf ("# KEY=", "# SIGN=")
# output: build/hello_<tag>/hello_<tag>_<conf>[_upgrade].bin
set -euo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> <tag> <version> [upgrade]}
TAG=${2:?usage: $0 <conf> <tag> <version> [upgrade]}
VER=${3:?usage: $0 <conf> <tag> <version> [upgrade]}
KEY=$(conf_get "$CONF" KEY)
read -r -a SIGN_ARGS <<<"$(conf_get "$CONF" SIGN)"
IN="$BUILD/hello_$TAG/zephyr/zephyr.bin"
OUT="$BUILD/hello_$TAG/hello_${TAG}_$CONF.bin"
KEY_ARG=()
[ "$KEY" != none ] && KEY_ARG=(-k "$EXP/keys/$KEY.pem")
EXTRA=()
if [ "${4:-}" = upgrade ]; then
	EXTRA=(--pad --confirm)
	OUT="${OUT%.bin}_upgrade.bin"
fi

python "$IMGTOOL" sign "${KEY_ARG[@]}" "${SIGN_ARGS[@]}" --header-size "$HDR_SIZE" --align 1 \
	--slot-size "$SLOT_SIZE" --version "$VER" "${EXTRA[@]}" "$IN" "$OUT"
python "$IMGTOOL" verify "${KEY_ARG[@]}" "$OUT"
echo "signed: $OUT"
