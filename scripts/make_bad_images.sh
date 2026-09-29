#!/usr/bin/env bash
# Make images that MCUboot must reject, from a signed image.
# usage: scripts/make_bad_images.sh <conf> <tag>      e.g. rsa2048 v1
#   needs build/hello_<tag>/hello_<tag>_<conf>.bin (scripts/sign_app.sh)
# outputs in build/hello_<tag>/:
#   *_bad_payload.bin  1 bit flipped in code      -> fails at hash check (pure: at signature)
#   *_bad_sig.bin      1 bit flipped in signature -> fails at signature check
#   *_bad_key.bin      signed with another key    -> fails at key match
#   (only bad_payload for unsigned configurations, KEY=none)
set -euo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> <tag>}
TAG=${2:?usage: $0 <conf> <tag>}
KEY=$(conf_get "$CONF" KEY)
read -r -a SIGN_ARGS <<<"$(conf_get "$CONF" SIGN)"
DIR="$BUILD/hello_$TAG"
GOOD="$DIR/hello_${TAG}_$CONF.bin"
BAD="$DIR/hello_${TAG}_${CONF}_bad"

# Code area (past the 0x200 header)
python "$EXP/scripts/tamper.py" "$GOOD" "${BAD}_payload.bin" 0x400
[ "$KEY" = none ] && exit 0

# The signature TLV is the last TLV, so the last byte of an unpadded image is in it
python "$EXP/scripts/tamper.py" "$GOOD" "${BAD}_sig.bin" -1

# Throwaway key, never kept
case "$KEY" in
rsa2048) KEY_TYPE=rsa-2048 ;;
rsa3072) KEY_TYPE=rsa-3072 ;;
ecdsa_p256) KEY_TYPE=ecdsa-p256 ;;
ed25519) KEY_TYPE=ed25519 ;;
*) echo "unknown key type for $KEY" >&2; exit 1 ;;
esac
OTHER_KEY="$(mktemp --suffix=.pem)"
python "$IMGTOOL" keygen -k "$OTHER_KEY" -t "$KEY_TYPE"
python "$IMGTOOL" sign -k "$OTHER_KEY" "${SIGN_ARGS[@]}" --header-size "$HDR_SIZE" --align 1 \
	--slot-size "$SLOT_SIZE" --version 1.0.0 "$DIR/zephyr/zephyr.bin" "${BAD}_key.bin"
rm -f "$OTHER_KEY"
echo "wrong key: ${BAD}_key.bin"
