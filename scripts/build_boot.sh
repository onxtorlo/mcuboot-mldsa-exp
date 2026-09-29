#!/usr/bin/env bash
# Build MCUboot for one signature configuration, optionally with extra config fragments.
# usage: scripts/build_boot.sh <conf> [extra...]   e.g. rsa2048, ecdsa_p256_psa measure
#   needs boot_conf/<conf>.conf (its "# KEY=" line names keys/<key>.pem)
#   and boot_conf/<extra>.conf
# output: build/boot_<conf>[_<extra>...]   (flash with: scripts/flash.sh boot <conf>[_<extra>...])
#         build/boot_<conf>[_<extra>...].build.log
set -euo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> [extra...]}
shift
KEY=$(conf_get "$CONF" KEY)
CONFS="$EXP/boot_conf/$CONF.conf"
NAME="$CONF"
for extra in "$@"; do
	CONFS="$CONFS;$EXP/boot_conf/$extra.conf"
	NAME="${NAME}_$extra"
done
KEY_ARG=()
if [ "$KEY" != none ]; then
	KEY_ARG=(-DCONFIG_BOOT_SIGNATURE_KEY_FILE="\"$EXP/keys/$KEY.pem\"")
fi

mkdir -p "$BUILD"
west build -p -b "$BOARD" bootloader/mcuboot/boot/zephyr -d "$BUILD/boot_$NAME" -- \
	-DEXTRA_DTC_OVERLAY_FILE="$PART_OVERLAY" \
	-DEXTRA_CONF_FILE="$CONFS" \
	"${KEY_ARG[@]}" \
	2>&1 | tee "$BUILD/boot_$NAME.build.log"
