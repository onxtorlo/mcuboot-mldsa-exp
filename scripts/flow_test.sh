#!/usr/bin/env bash
# End-to-end secure boot flow for one configuration: boot, upgrade, rejected upgrades.
# usage: scripts/flow_test.sh <conf> <boot name> <outdir>
#   e.g. scripts/flow_test.sh mldsa65 mldsa65_measure results/<date>_flow/mldsa65
#   needs build/hello_v1 and build/hello_v2 (scripts/build_app.sh v1|v2); serial port free
#
# Cases (each one starts from an erased board with MCUboot and v1 in slot0):
#   boot_v1         v1 in slot0                         -> boots [v1]
#   upgrade_v2      + signed v2 in slot1 (confirmed)    -> slot1 verified, swapped, boots [v2]
#   after_upgrade   reset once more                     -> boots [v2], no swap
#   upgrade_bad_payload  v2 in slot1, 1 bit flipped in code  -> slot1 rejected, boots [v1]
#   upgrade_bad_key      v2 in slot1 signed with another key -> slot1 rejected, boots [v1]
# <outdir>/flow.csv: case, expected, booted tag, verdict; logs/<case>.log
set -uo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> <boot name> <outdir>}
BOOT=${2:?}
OUT=${3:?}
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
KEY=$(conf_get "$CONF" KEY)
read -r -a SIGN_ARGS <<<"$(conf_get "$CONF" SIGN)"
V1="$BUILD/hello_v1/hello_v1_$CONF.bin"
V2="$BUILD/hello_v2/hello_v2_${CONF}_upgrade.bin"
V2_BAD_PAYLOAD="$BUILD/hello_v2/hello_v2_${CONF}_upgrade_bad_payload.bin"
V2_BAD_KEY="$BUILD/hello_v2/hello_v2_${CONF}_upgrade_bad_key.bin"

if [ -e "$OUT" ]; then
	echo "$OUT already exists; pick a new directory" >&2
	exit 1
fi
mkdir -p "$OUT/logs"

"$EXP/scripts/sign_app.sh" "$CONF" v1 1.0.0 >/dev/null
"$EXP/scripts/sign_app.sh" "$CONF" v2 2.0.0 upgrade >/dev/null
python "$EXP/scripts/tamper.py" "$V2" "$V2_BAD_PAYLOAD" 0x400 >/dev/null
OTHER_KEY="$(mktemp --suffix=.pem)"
case "$KEY" in
mldsa44) KEY_TYPE=ml-dsa-44 ;; mldsa65) KEY_TYPE=ml-dsa-65 ;; mldsa87) KEY_TYPE=ml-dsa-87 ;;
rsa2048) KEY_TYPE=rsa-2048 ;; rsa3072) KEY_TYPE=rsa-3072 ;;
ecdsa_p256) KEY_TYPE=ecdsa-p256 ;; ed25519) KEY_TYPE=ed25519 ;;
*) echo "unknown key type for $KEY" >&2; exit 1 ;;
esac
python "$IMGTOOL" keygen -k "$OTHER_KEY" -t "$KEY_TYPE"
python "$IMGTOOL" sign -k "$OTHER_KEY" "${SIGN_ARGS[@]}" --header-size "$HDR_SIZE" --align 1 \
	--slot-size "$SLOT_SIZE" --version 2.0.0 --pad --confirm \
	"$BUILD/hello_v2/zephyr/zephyr.bin" "$V2_BAD_KEY" >/dev/null
rm -f "$OTHER_KEY"

echo "case,expected,booted,verdict" >"$OUT/flow.csv"
fail=0

fresh() {
	"$EXP/scripts/flash.sh" erase >/dev/null 2>&1
	"$EXP/scripts/flash.sh" boot "$BOOT" >/dev/null 2>&1
	"$EXP/scripts/flash.sh" slot0 "$V1" >/dev/null 2>&1
}

# check <case> <expected tag>: reset, capture, compare the booted application tag
check() {
	local log="$OUT/logs/$1.log" got
	python "$EXP/scripts/capture_boot.py" --seconds 20 --label "$1" --log "$log" \
		--csv "$OUT/boot.csv" >/dev/null
	got=$(grep -o "\[v[0-9]\] Hello World" "$log" | head -1 | cut -c2-3)
	[ -n "$got" ] || got=none
	if [ "$got" = "$2" ]; then v=PASS; else v=FAIL; fail=1; fi
	echo "$1,$2,$got,$v" >>"$OUT/flow.csv"
	printf "%-22s expect %-4s got %-4s %s\n" "$1" "$2" "$got" "$v"
}

fresh
check boot_v1 v1
"$EXP/scripts/flash.sh" slot1 "$V2" >/dev/null 2>&1
check upgrade_v2 v2
check after_upgrade v2

fresh
"$EXP/scripts/flash.sh" slot1 "$V2_BAD_PAYLOAD" >/dev/null 2>&1
check upgrade_bad_payload v1

fresh
"$EXP/scripts/flash.sh" slot1 "$V2_BAD_KEY" >/dev/null 2>&1
check upgrade_bad_key v1

exit $fail
