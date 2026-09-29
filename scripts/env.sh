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

# shellcheck disable=SC1091
source "$WS/.venv/bin/activate"
cd "$WS"
