#!/usr/bin/env bash
# Sign a built application image with imgtool from our MCUboot fork.
# usage: scripts/sign_app.sh <sig> <tag> <version> [upgrade]
#   e.g. rsa2048 v1 1.0.0          -> for slot0
#        rsa2048 v2 2.0.0 upgrade  -> for slot1, padded + confirmed (permanent swap)
# output: build/hello_<tag>/hello_<tag>_<sig>[_upgrade].bin
set -euo pipefail
source "$(dirname "$0")/env.sh"

SIG=${1:?usage: $0 <sig> <tag> <version> [upgrade]}
TAG=${2:?usage: $0 <sig> <tag> <version> [upgrade]}
VER=${3:?usage: $0 <sig> <tag> <version> [upgrade]}
KEY="$EXP/keys/$SIG.pem"
IN="$BUILD/hello_$TAG/zephyr/zephyr.bin"
OUT="$BUILD/hello_$TAG/hello_${TAG}_$SIG.bin"
EXTRA=()
if [ "${4:-}" = upgrade ]; then
	EXTRA=(--pad --confirm)
	OUT="${OUT%.bin}_upgrade.bin"
fi

python "$IMGTOOL" sign -k "$KEY" --header-size "$HDR_SIZE" --align 1 \
	--slot-size "$SLOT_SIZE" --version "$VER" "${EXTRA[@]}" "$IN" "$OUT"
python "$IMGTOOL" verify -k "$KEY" "$OUT"
echo "signed: $OUT"
