#!/usr/bin/env python3
"""Reset the board, capture the boot log from the serial port, and pull out
the "MEAS" lines printed by MCUboot (CONFIG_BOOT_MEASURE_TIMING).

usage: scripts/capture_boot.py [--port /dev/ttyACM0] [--seconds 10] [--no-reset]
                               [--log out.log] [--csv out.csv --label boot_ok --run 1]

  --log  save the raw serial log (one file per boot)
  --csv  append one row of parsed values (header written on first use)

Nothing else may have the serial port open (e.g. minicom).
"""
import argparse
import csv
import datetime
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
FIELDS = (["label", "run", "time", "clock_hz"]
          + [f"{s}_{k}" for s in STAGES for k in ("n", "cyc", "sum_cyc", "us")]
          + ["stack_size", "stack_used", "result", "booted", "log"])


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
    m = re.search(r"MEAS stack size=(\d+) used=(\d+)", log)
    if m:
        row["stack_size"], row["stack_used"] = int(m.group(1)), int(m.group(2))
    row["booted"] = "Hello World" in log
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", default="/dev/ttyACM0")
    ap.add_argument("--seconds", type=float, default=10)
    ap.add_argument("--no-reset", action="store_true")
    ap.add_argument("--log")
    ap.add_argument("--csv")
    ap.add_argument("--label", default="")
    ap.add_argument("--run", default="")
    args = ap.parse_args()

    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    log = capture(args.port, args.seconds, not args.no_reset)
    print(log.strip())
    row = parse(log)
    print("parsed:", row)

    if args.log:
        with open(args.log, "w") as f:
            f.write(f"# captured {stamp} label={args.label} run={args.run}\n")
            f.write(log)

    if args.csv:
        row = {"label": args.label, "run": args.run, "time": stamp, **row,
               "log": os.path.basename(args.log) if args.log else ""}
        new = not os.path.exists(args.csv)
        with open(args.csv, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, restval="")
            if new:
                w.writeheader()
            w.writerow(row)


if __name__ == "__main__":
    main()
