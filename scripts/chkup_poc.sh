#!/usr/bin/env bash
# ChkUp step 4 (vulnerability validation) on the board: feed PoC images to MCUboot and record
# what it boots. ChkUp's rule: if the update still goes through, the alert is a true positive.
# usage: scripts/chkup_poc.sh <conf> <outdir> [case...]
#   e.g. mldsa65 mcuboot-mldsa-exp/results/<date>_chkup/poc   (relative to the west workspace)
#   needs build/boot_<conf>[_<variant>] (scripts/build_boot.sh <conf> [variant...]),
#   build/hello_v1, build/hello_v2 (scripts/build_app.sh), build/hello_nucleo (see notes);
#   serial port free, ST-Link attached to WSL
# outputs: <outdir>/poc.csv (case, boot, property, poc, expected, observed, verdict, markers),
#          logs/<case>.log, images/ (every PoC image, with chkup_images.py info)
set -uo pipefail
source "$(dirname "$0")/env.sh"

CONF=${1:?usage: $0 <conf> <outdir> [case...]}
OUT=${2:?}
shift 2
ONLY=("$@")
[[ "$OUT" = /* ]] || OUT="$WS/$OUT"
if [ -e "$OUT" ]; then
	echo "$OUT already exists; pick a new directory" >&2
	exit 1
fi
mkdir -p "$OUT/logs" "$OUT/images"
KEY=$(conf_get "$CONF" KEY)
read -r -a SIGN_ARGS <<<"$(conf_get "$CONF" SIGN)"
IMG="$OUT/images"
TOOL="$EXP/scripts/chkup_images.py"

sign() { # sign <app dir> <out> <version> [extra imgtool args...]
	local app=$1 out=$2 ver=$3
	shift 3
	python "$IMGTOOL" sign "${SIGN_ARGS[@]}" --header-size "$HDR_SIZE" --align 1 \
		--slot-size "$SLOT_SIZE" --version "$ver" "$@" "$BUILD/$app/zephyr/zephyr.bin" "$IMG/$out" >/dev/null
}
K=(-k "$EXP/keys/$KEY.pem")
UP=(--pad --confirm)

# ---- PoC images (ChkUp Table 2, adapted)
sign hello_v1 v1_10.bin 1.0.0 "${K[@]}"
sign hello_v2 v2_20.bin 2.0.0 "${K[@]}"
sign hello_v2 up_v2_20.bin 2.0.0 "${K[@]}" "${UP[@]}"
sign hello_v1 up_v1_10.bin 1.0.0 "${K[@]}" "${UP[@]}"
sign hello_v2 up_v2_unsigned.bin 2.0.0 "${UP[@]}"
python "$EXP/scripts/tamper.py" "$IMG/up_v2_20.bin" "$IMG/up_v2_flip.bin" 0x400 >/dev/null
OTHER_KEY="$(mktemp --suffix=.pem)"
python "$IMGTOOL" keygen -k "$OTHER_KEY" -t "ml-dsa-${KEY#mldsa}"
sign hello_v2 up_v2_wrongkey.bin 2.0.0 -k "$OTHER_KEY" "${UP[@]}"
rm -f "$OTHER_KEY"
python "$TOOL" rehash "$IMG/up_v2_20.bin" "$IMG/up_v2_rehash.bin" 0x400 >/dev/null
python "$TOOL" setver "$IMG/up_v1_10.bin" "$IMG/up_v1_setver3.bin" 3.0.0 >/dev/null
python "$TOOL" inject "$IMG/up_v2_20.bin" "$IMG/up_v2_inject.bin" 0x50 0a000000 >/dev/null
sign hello_nucleo up_other.bin 2.0.0 "${K[@]}" "${UP[@]}"
python "$TOOL" replace "$IMG/v1_10.bin" "$IMG/v1_tampered.bin" "Hello World" "Hello Wor1d" >/dev/null
sign hello_v1 v1_10_sc1.bin 1.0.0 "${K[@]}" -s 1
sign hello_v2 v2_20_sc5.bin 2.0.0 "${K[@]}" -s 5
sign hello_v2 up_v2_20_sc5.bin 2.0.0 "${K[@]}" -s 5 "${UP[@]}"
sign hello_v1 up_v1_10_sc1.bin 1.0.0 "${K[@]}" -s 1 "${UP[@]}"
sign hello_v1 up_v1_10_sc5.bin 1.0.0 "${K[@]}" -s 5 "${UP[@]}"
python "$TOOL" inject "$IMG/up_v1_10_sc1.bin" "$IMG/up_v1_10_sc1_inject.bin" 0x50 0a000000 >/dev/null
for f in "$IMG"/*.bin; do
	echo "== $(basename "$f")"
	python "$TOOL" info "$f"
done >"$IMG/info.txt"

# ---- cases: name | boot build | property | PoC | slot0 | slot1 | expected
# expected: tag of the application that must run (v1, v2), v1-tampered (modified slot0 runs),
#           swap (slot1 accepted, other-board image runs without console), none (nothing boots)
CASES=(
"B0|$CONF|sanity|legit upgrade v1->v2|v1_10|up_v2_20|v2"
"B1|$CONF|authenticity-missing|unsigned image|v1_10|up_v2_unsigned|v1"
"B2|$CONF|integrity-missing|1 bit flipped in code|v1_10|up_v2_flip|v1"
"B3|$CONF|freshness-missing|older valid image (2.0.0 -> 1.0.0)|v2_20|up_v1_10|v1"
"B4|$CONF|compatibility-missing|image for another board, same key|v1_10|up_other|swap"
"B5|$CONF|authenticity-improper|signed with another ML-DSA key|v1_10|up_v2_wrongkey|v1"
"B6|$CONF|integrity-improper|bit flip + SHA256 TLV replaced|v1_10|up_v2_rehash|v1"
"B7|$CONF|freshness-improper|older image, header version set to 3.0.0|v2_20|up_v1_setver3|v2"
"B8|$CONF|P5 unsigned-field|SEC_CNT TLV injected in unprotected area|v1_10|up_v2_inject|v1"
"B9|$CONF|integrity (slot0)|slot0 payload modified, no upgrade|v1_tampered|-|none"
"D0|${CONF}_chkup_dgp|sanity|legit upgrade v1->v2|v1_10|up_v2_20|v2"
"D3|${CONF}_chkup_dgp|freshness|older valid image (2.0.0 -> 1.0.0)|v2_20|up_v1_10|v2"
"D7|${CONF}_chkup_dgp|freshness-improper|older image, header version set to 3.0.0|v2_20|up_v1_setver3|v2"
"S0|${CONF}_chkup_dgp_seccnt|sanity|legit upgrade, counter 1->5|v1_10_sc1|up_v2_20_sc5|v2"
"S3|${CONF}_chkup_dgp_seccnt|freshness|counter 5 -> 1|v2_20_sc5|up_v1_10_sc1|v2"
"S4|${CONF}_chkup_dgp_seccnt|P6 rollback value|older version, equal counter 5 -> 5|v2_20_sc5|up_v1_10_sc5|v1"
"SN|${CONF}_chkup_dgp_seccnt_chkup_noallow|P6 rollback value|counter 5 -> 1 + unprotected SEC_CNT=10|v2_20_sc5|up_v1_10_sc1_inject|v2"
"N8|${CONF}_chkup_noallow|P5 unsigned-field|SEC_CNT TLV injected in unprotected area|v1_10|up_v2_inject|v2"
"V9|${CONF}_chkup_noval0|integrity (slot0)|slot0 payload modified, no upgrade|v1_tampered|-|v1-tampered"
)

echo "case,boot,property,poc,expected,observed,verdict,markers" >"$OUT/poc.csv"
fail=0
for c in "${CASES[@]}"; do
	IFS='|' read -r name boot prop poc s0 s1 exp <<<"$c"
	if [ ${#ONLY[@]} -gt 0 ] && [[ ! " ${ONLY[*]} " =~ " $name " ]]; then
		continue
	fi
	log="$OUT/logs/$name.log"
	{
		"$EXP/scripts/flash.sh" erase
		"$EXP/scripts/flash.sh" boot "$boot"
		"$EXP/scripts/flash.sh" slot0 "$IMG/$s0.bin"
		# slot1 is written with the core left halted: flash.sh would reset and let MCUboot
		# process the image before the capture starts, losing the swap/reject messages
		[ "$s1" = - ] || openocd -f interface/stlink.cfg -f target/stm32f4x.cfg \
			-c "init; reset halt; program $IMG/$s1.bin $SLOT1_ADDR verify; shutdown"
	} >"$OUT/logs/$name.flash.log" 2>&1 || { echo "$name: flashing failed" >&2; fail=1; continue; }
	python "$EXP/scripts/capture_boot.py" --seconds 25 --log "$log" >/dev/null
	tag=$(grep -oE "\[(v[0-9]|other)\] Hello Wor[l1]d" "$log" | head -1)
	case "$tag" in
	*"Wor1d") got="${tag:1:2}-tampered" ;;
	"") got=none ;;
	*) got="${tag:1:2}" ;;
	esac
	marks=""
	grep -q "Starting swap" "$log" && marks+="swap;"
	grep -q "slot is not valid" "$log" && marks+="rejected;"
	grep -q "downgrade prevention" "$log" && marks+="downgrade-erased;"
	grep -q "Unable to find bootable image" "$log" && marks+="no-bootable;"
	grep -q "Jumping to" "$log" && marks+="jump;"
	[ "$got" = none ] && [[ "$marks" == *swap* && "$marks" == *jump* ]] && got=swap
	if [ "$got" = "$exp" ]; then v=PASS; else v=FAIL; fail=1; fi
	echo "$name,$boot,$prop,\"$poc\",$exp,$got,$v,$marks" >>"$OUT/poc.csv"
	printf "%-3s %-22s expect %-12s got %-12s %s  %s\n" "$name" "$prop" "$exp" "$got" "$v" "$marks"
done
exit $fail
