#!/usr/bin/env python3
"""Reset the board, capture the boot log from the serial port, and pull out
the "MEAS" lines printed by MCUboot (CONFIG_BOOT_MEASURE_TIMING).

usage: scripts/capture_boot.py [--port /dev/ttyACM0] [--seconds 10] [--no-reset]
                               [--csv results/x.csv --label rsa2048]

Nothing else may have the serial port open (e.g. minicom).
"""
import argparse
import csv
import os
import re
import subprocess
import time

import serial

OPENOCD = ["openocd", "-f", "interface/stlink.cfg", "-f", "target/stm32f4x.cfg",
           "-c", "init; reset run; shutdown"]
# Stop reading once the boot has clearly finished
DONE = re.compile(r"Hello World|Unable to find bootable image")
STAGE = re.compile(r"MEAS (\w+) n=(\d+) last_cyc=(\d+) sum_cyc=(\d+) last_us=(\d+)")
STAGES = ["total", "validate", "hash", "sig"]
FIELDS = (["label", "clock_hz"]
          + [f"{s}_{k}" for s in STAGES for k in ("n", "cyc", "sum_cyc", "us")]
          + ["result", "booted"])


def capture(port, seconds, reset):
    ser = serial.Serial(port, 115200, timeout=0.1)
    # Drop output left over from an earlier boot (e.g. right after flashing)
    time.sleep(0.5)
    ser.reset_input_buffer()
    if reset:
        subprocess.run(OPENOCD, check=True, capture_output=True)
    buf = b""
    end = time.time() + seconds
    while time.time() < end:
        buf += ser.read(4096)
        if DONE.search(buf.decode(errors="replace")):
            buf += ser.read(4096)
            break
    ser.close()
    return buf.decode(errors="replace").replace("\r", "")


def parse(log):
    row = {}
    m = re.search(r"MEAS clock_hz=(\d+)", log)
    if m:
        row["clock_hz"] = int(m.group(1))
    for name, n, last, total, us in STAGE.findall(log):
        row[f"{name}_n"] = int(n)
        row[f"{name}_cyc"] = int(last)
        row[f"{name}_sum_cyc"] = int(total)
        row[f"{name}_us"] = int(us)
    m = re.search(r"MEAS result=(\w+)", log)
    if m:
        row["result"] = m.group(1)
    row["booted"] = "Hello World" in log
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", default="/dev/ttyACM0")
    ap.add_argument("--seconds", type=float, default=10)
    ap.add_argument("--no-reset", action="store_true")
    ap.add_argument("--csv")
    ap.add_argument("--label", default="")
    args = ap.parse_args()

    log = capture(args.port, args.seconds, not args.no_reset)
    print(log.strip())
    row = parse(log)
    print("parsed:", row)

    if args.csv:
        row = {"label": args.label, **row}
        new = not os.path.exists(args.csv)
        with open(args.csv, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, restval="")
            if new:
                w.writeheader()
            w.writerow(row)


if __name__ == "__main__":
    main()
