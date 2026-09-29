#!/usr/bin/env python3
"""Flip one bit in a signed image to check that MCUboot rejects it.

usage: scripts/tamper.py <in.bin> <out.bin> [offset]
  offset defaults to 0x400 (inside the payload, past the 0x200 header)
"""
import sys

src, dst = sys.argv[1], sys.argv[2]
off = int(sys.argv[3], 0) if len(sys.argv) > 3 else 0x400

data = bytearray(open(src, "rb").read())
before = data[off]
data[off] ^= 0x01
open(dst, "wb").write(data)
print(f"offset {off:#x}: {before:#04x} -> {data[off]:#04x}  ({dst})")
