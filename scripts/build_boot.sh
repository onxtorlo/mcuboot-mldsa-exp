#!/usr/bin/env bash
# Build MCUboot for one signature type.
# usage: scripts/build_boot.sh <sig>     e.g. rsa2048
#   needs boot_conf/<sig>.conf and keys/<sig>.pem
set -euo pipefail
source "$(dirname "$0")/env.sh"

SIG=${1:?usage: $0 <sig>}
west build -p -b "$BOARD" bootloader/mcuboot/boot/zephyr -d "$BUILD/boot_$SIG" -- \
	-DEXTRA_DTC_OVERLAY_FILE="$PART_OVERLAY" \
	-DEXTRA_CONF_FILE="$EXP/boot_conf/$SIG.conf" \
	-DCONFIG_BOOT_SIGNATURE_KEY_FILE="\"$EXP/keys/$SIG.pem\""
