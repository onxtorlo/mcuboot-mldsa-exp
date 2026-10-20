#!/usr/bin/env bash
# usage: dbg_one.sh <conf> <buildname-suffix> <img.bin> [extra -D args...]
# builds MCUboot <conf>+measure (+ extra -D), flashes it + image, captures one boot log
set -uo pipefail
source ~/secureboot/mcuboot-mldsa-exp/scripts/env.sh
CONF=$1; SUF=$2; IMG=$3; shift 3
KEY=$(conf_get "$CONF" KEY)
D="$BUILD/boot_${CONF}_$SUF"
west build -p -b "$BOARD" "$MCUBOOT/boot/zephyr" -d "$D" -- \
  -DEXTRA_DTC_OVERLAY_FILE="$PART_OVERLAY" \
  -DEXTRA_CONF_FILE="$EXP/boot_conf/$CONF.conf;$EXP/boot_conf/measure.conf" \
  -DCONFIG_BOOT_SIGNATURE_KEY_FILE="\"$EXP/keys/$KEY.pem\"" "$@" > "$D.build.log" 2>&1 \
  || { grep -m5 -E "error|Error" "$D.build.log"; exit 1; }
grep -E "FLASH:|RAM:" "$D.build.log" | tail -2
"$EXP/scripts/flash.sh" erase >/dev/null 2>&1
west flash -d "$D" --runner openocd >/dev/null 2>&1 || { echo flash boot failed; exit 1; }
"$EXP/scripts/flash.sh" slot0 "$IMG" >/dev/null 2>&1 || { echo flash img failed; exit 1; }
python "$EXP/scripts/capture_boot.py" --seconds 8 | grep -vE "^\s*$" | grep -vE "MEAS (total|clock)" | head -40
