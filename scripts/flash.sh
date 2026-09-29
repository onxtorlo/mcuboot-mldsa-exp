#!/usr/bin/env bash
# Flash MCUboot and/or a signed image with OpenOCD.
# usage: scripts/flash.sh boot <sig>          -> MCUboot at 0x08000000
#        scripts/flash.sh slot0 <file.bin>    -> image at slot0
#        scripts/flash.sh slot1 <file.bin>    -> image at slot1 (upgrade candidate)
#        scripts/flash.sh erase               -> mass erase both banks
set -euo pipefail
source "$(dirname "$0")/env.sh"

OCD=(openocd -f interface/stlink.cfg -f target/stm32f4x.cfg)

case "${1:-}" in
boot)
	SIG=${2:?usage: $0 boot <sig>}
	west flash -d "$BUILD/boot_$SIG" --runner openocd
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
