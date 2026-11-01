#!/usr/bin/env python3
"""Build ChkUp PoC images (Table 2, adapted to MCUboot) from a signed image.

usage: scripts/chkup_images.py info    <in.bin>
       scripts/chkup_images.py rehash  <in.bin> <out.bin> [offset]   flip a payload bit, then
                                       replace the SHA256 TLV with the new digest
       scripts/chkup_images.py setver  <in.bin> <out.bin> <maj.min.rev>   edit the header
                                       version without re-signing
       scripts/chkup_images.py inject  <in.bin> <out.bin> <type> <hexvalue>   append a TLV to
                                       the unprotected TLV area (outside the signed region)
       scripts/chkup_images.py replace <in.bin> <out.bin> <old> <new>   replace a byte string
                                       in the payload (same length), e.g. a printed message

Image layout: header (hdr_size) | payload (img_size) | protected TLVs (protect_tlv_size)
| unprotected TLVs. The image hash covers everything up to the end of the protected TLVs;
the signature signs that hash.
"""
import hashlib
import struct
import sys

IMAGE_MAGIC = 0x96F3B83D
TLV_INFO_MAGIC, TLV_PROT_INFO_MAGIC = 0x6907, 0x6908
TLV_SHA256 = 0x10
HDR = struct.Struct("<IIHHIIBBHI")  # magic load hdr_size prot_size img_size flags ver(B B H I)


def parse(data):
    magic, load, hdr_size, prot_size, img_size, flags, vmaj, vmin, vrev, vbuild = HDR.unpack_from(data)
    if magic != IMAGE_MAGIC:
        sys.exit("not an MCUboot image")
    tlv = hdr_size + img_size
    info = {"load": load, "hdr_size": hdr_size, "prot_size": prot_size, "img_size": img_size,
            "flags": flags, "version": f"{vmaj}.{vmin}.{vrev}+{vbuild}", "tlv_off": tlv, "tlvs": []}
    off = tlv
    for area, magic_expect, size in (("protected", TLV_PROT_INFO_MAGIC, prot_size),
                                     ("unprotected", TLV_INFO_MAGIC, None)):
        if area == "protected" and not size:
            continue
        m, tot = struct.unpack_from("<HH", data, off)
        if m != magic_expect:
            sys.exit(f"bad {area} TLV info magic {m:#x} at {off:#x}")
        info[f"{area}_info_off"], info[f"{area}_tot"] = off, tot
        p = off + 4
        while p < off + tot:
            t, ln = struct.unpack_from("<HH", data, p)
            info["tlvs"].append({"area": area, "type": t, "len": ln, "off": p + 4})
            p += 4 + ln
        off += tot
    info["hashed_end"] = tlv + prot_size
    return info


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in ("info", "rehash", "setver", "inject", "replace"):
        sys.exit(__doc__)
    data = bytearray(open(sys.argv[2], "rb").read())
    info = parse(data)

    if cmd == "info":
        print({k: v for k, v in info.items() if k != "tlvs"})
        for t in info["tlvs"]:
            print(f"  {t['area']:11s} type {t['type']:#06x} len {t['len']:4d} at {t['off']:#x}")
        return

    out = sys.argv[3]
    if cmd == "rehash":
        off = int(sys.argv[4], 0) if len(sys.argv) > 4 else 0x400
        data[off] ^= 0x01
        sha = [t for t in info["tlvs"] if t["type"] == TLV_SHA256]
        if not sha:
            sys.exit("no SHA256 TLV")
        digest = hashlib.sha256(data[:info["hashed_end"]]).digest()
        data[sha[0]["off"]:sha[0]["off"] + 32] = digest
        print(f"flipped bit at {off:#x}, SHA256 TLV replaced with {digest.hex()[:16]}...")
    elif cmd == "setver":
        maj, mnr, rev = (int(x) for x in sys.argv[4].split("."))
        struct.pack_into("<BBH", data, 20, maj, mnr, rev)
        print(f"header version {info['version']} -> {sys.argv[4]} (signature not updated)")
    elif cmd == "inject":
        t, val = int(sys.argv[4], 0), bytes.fromhex(sys.argv[5])
        end = info["unprotected_info_off"] + info["unprotected_tot"]
        new = struct.pack("<HH", t, len(val)) + val
        if end + len(new) > len(data):
            data.extend(b"\xff" * (end + len(new) - len(data)))
        elif any(b != 0xFF for b in data[end:end + len(new)]):
            sys.exit("no free (erased) space after the unprotected TLVs")
        data[end:end + len(new)] = new
        struct.pack_into("<H", data, info["unprotected_info_off"] + 2, info["unprotected_tot"] + len(new))
        print(f"TLV {t:#x} ({len(val)} B) appended to the unprotected area at {end:#x}")
    elif cmd == "replace":
        old, new = sys.argv[4].encode(), sys.argv[5].encode()
        if len(old) != len(new):
            sys.exit("old and new must have the same length")
        i = data.find(old, info["hdr_size"], info["tlv_off"])
        if i < 0:
            sys.exit(f"{sys.argv[4]!r} not found in the payload")
        data[i:i + len(old)] = new
        print(f"payload {sys.argv[4]!r} -> {sys.argv[5]!r} at {i:#x}")
    open(out, "wb").write(data)


if __name__ == "__main__":
    main()
