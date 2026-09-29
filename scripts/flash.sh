#!/usr/bin/env bash
# Flash MCUboot and/or a signed image with OpenOCD.
# usage: scripts/flash.sh boot <name>         -> MCUboot build/boot_<name> at 0x08000000
#        scripts/flash.sh slot0 <file.bin>    -> image at slot0
#        scripts/flash.sh slot1 <file.bin>    -> image at slot1 (upgrade candidate)
#        scripts/flash.sh erase               -> mass erase both banks
set -euo pipefail
source "$(dirname "$0")/env.sh"

OCD=(openocd -f interface/stlink.cfg -f target/stm32f4x.cfg)

case "${1:-}" in
boot)
	NAME=${2:?usage: $0 boot <name>}
	west flash -d "$BUILD/boot_$NAME" --runner openocd
	;;
slot0 | slot1)
	FILE=${2:?usage: $0 $1 <file.bin>}
	[ "$1" = slot0 ] && ADDR=$SLOT0_ADDR || ADDR=$SLOT1_ADDR
	"${OCD[@]}" -c "program $FILE $ADDR verify reset exit"
	;;
erase)
	"${OCD[@]}" -c "init; reset halt; stm32f2x mass_erase 0; stm32f2x mass_erase 1; shutdown"
	;;
*)
	sed -n '2,6p' "$0"
	exit 1
	;;
esac
