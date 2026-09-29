#!/usr/bin/env bash
# Build MCUboot for one signature type, optionally with extra config fragments.
# usage: scripts/build_boot.sh <sig> [extra...]   e.g. rsa2048, rsa2048 measure
#   needs boot_conf/<sig>.conf, keys/<sig>.pem and boot_conf/<extra>.conf
# output: build/boot_<sig>[_<extra>...]   (flash with: scripts/flash.sh boot <sig>[_<extra>...])
set -euo pipefail
source "$(dirname "$0")/env.sh"

SIG=${1:?usage: $0 <sig> [extra...]}
shift
CONFS="$EXP/boot_conf/$SIG.conf"
NAME="$SIG"
for extra in "$@"; do
	CONFS="$CONFS;$EXP/boot_conf/$extra.conf"
	NAME="${NAME}_$extra"
done

west build -p -b "$BOARD" bootloader/mcuboot/boot/zephyr -d "$BUILD/boot_$NAME" -- \
	-DEXTRA_DTC_OVERLAY_FILE="$PART_OVERLAY" \
	-DEXTRA_CONF_FILE="$CONFS" \
	-DCONFIG_BOOT_SIGNATURE_KEY_FILE="\"$EXP/keys/$SIG.pem\""
