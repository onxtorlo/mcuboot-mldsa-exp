# Common settings, sourced by the other scripts.
EXP="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WS="$(cd "$EXP/.." && pwd)"                 # west workspace (~/secureboot)
BOARD=stm32f429i_disc1
BUILD="$WS/build"
IMGTOOL="$WS/bootloader/mcuboot/scripts/imgtool.py"
PART_OVERLAY="$EXP/boot_conf/$BOARD.overlay"

# Must match boot_conf/<board>.overlay
HDR_SIZE=0x200
SLOT_SIZE=0xc0000
SLOT0_ADDR=0x08020000
SLOT1_ADDR=0x08120000

# Header fields of boot_conf/<conf>.conf, e.g. "# KEY=rsa2048", "# SIGN=--pure"
#   KEY   keys/<KEY>.pem signs the image and is built into MCUboot ("none": unsigned)
#   SIGN  extra imgtool sign arguments
conf_get() {
	sed -n "s/^# $2=//p" "$EXP/boot_conf/$1.conf" | head -1
}

# shellcheck disable=SC1091
source "$WS/.venv/bin/activate"
cd "$WS"
