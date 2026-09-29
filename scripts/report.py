#!/usr/bin/env python3
"""Record the environment of a measurement run and summarize its results.

usage:
  scripts/report.py meta <outdir> --image <signed.bin> --boot <build name> [--boot ...]
      -> <outdir>/meta.json        versions, commits, signed image layout
         <outdir>/build_size.csv   text/data/bss and FLASH/RAM per bootloader build
  scripts/report.py summary <outdir>
      -> <outdir>/summary.md       tables from boot_ok.csv, reject.csv, build_size.csv
"""
import argparse
import csv
import datetime
import glob
import json
import os
import re
import statistics
import struct
import subprocess

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = os.path.dirname(EXP)
BUILD = os.path.join(WS, "build")

TLV_NAMES = {0x01: "KEYHASH", 0x02: "PUBKEY", 0x10: "SHA256", 0x11: "SHA384",
             0x12: "SHA512", 0x20: "RSA2048_PSS", 0x22: "ECDSA_SIG",
             0x23: "RSA3072_PSS", 0x24: "ED25519", 0x25: "SIG_PURE"}
STAGES = ["total", "validate", "hash", "sig"]


def git(path, *args):
    try:
        return subprocess.run(["git", "-C", path, *args], capture_output=True,
                              text=True, check=True).stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def repo_info(path):
    return {"commit": git(path, "rev-parse", "--short", "HEAD"),
            "branch": git(path, "branch", "--show-current"),
            "describe": git(path, "describe", "--tags", "--always"),
            "dirty": bool(git(path, "status", "--porcelain", "--untracked-files=no"))}


def zephyr_version():
    """From zephyr/VERSION (the west checkout is shallow, so git has no tags)"""
    v = dict(re.findall(r"^(\w+)\s*=\s*(\S*)",
                        open(os.path.join(WS, "zephyr", "VERSION")).read(), re.M))
    return f"{v['VERSION_MAJOR']}.{v['VERSION_MINOR']}.{v['PATCHLEVEL']}"


def cmake_cache(build_dir, key):
    with open(os.path.join(build_dir, "CMakeCache.txt")) as f:
        for line in f:
            if line.startswith(key + ":"):
                return line.split("=", 1)[1].strip()
    return ""


def kconfig(build_dir, names):
    out = {}
    with open(os.path.join(build_dir, "zephyr", ".config")) as f:
        for line in f:
            for n in names:
                if line.startswith(f"CONFIG_{n}="):
                    out[n] = line.split("=", 1)[1].strip().strip('"')
    return out


def build_size(name):
    bdir = os.path.join(BUILD, f"boot_{name}")
    gcc = cmake_cache(bdir, "CMAKE_C_COMPILER")
    size_tool = re.sub(r"gcc$", "size", gcc)
    out = subprocess.run([size_tool, os.path.join(bdir, "zephyr", "zephyr.elf")],
                         capture_output=True, text=True, check=True).stdout
    text, data, bss = (int(x) for x in out.splitlines()[1].split()[:3])
    row = {"build": name, "text": text, "data": data, "bss": bss,
           "flash_bytes": text + data}
    log = os.path.join(BUILD, f"boot_{name}.build.log")
    if os.path.exists(log):
        for region, used in re.findall(r"^\s+(FLASH|RAM):\s+(\d+) B", open(log).read(), re.M):
            row[f"{region.lower()}_used_linker"] = int(used)
    row.update(kconfig(bdir, ["BOOT_SIGNATURE_TYPE_RSA_LEN", "BOOT_MEASURE_TIMING",
                              "BOOT_SWAP_USING_SCRATCH", "MAIN_STACK_SIZE"]))
    return row, gcc


def image_layout(path):
    raw = open(path, "rb").read()
    magic, _load, hdr_size, prot_size, img_size = struct.unpack_from("<IIHHI", raw, 0)
    off = hdr_size + img_size + prot_size
    info_magic, tlv_tot = struct.unpack_from("<HH", raw, off)
    tlvs, p = [], off + 4
    while p < off + tlv_tot:
        t, ln = struct.unpack_from("<HH", raw, p)
        tlvs.append({"type": TLV_NAMES.get(t, hex(t)), "len": ln})
        p += 4 + ln
    return {"file": os.path.relpath(path, WS), "file_bytes": len(raw),
            "header_bytes": hdr_size, "payload_bytes": img_size,
            "tlv_area_bytes": tlv_tot, "tlvs": tlvs}


def cmd_meta(args):
    sizes, gcc = [], ""
    for name in args.boot:
        row, gcc = build_size(name)
        sizes.append(row)
    fields = sorted({k for r in sizes for k in r}, key=lambda k: (k != "build", k))
    with open(os.path.join(args.outdir, "build_size.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, restval="")
        w.writeheader()
        w.writerows(sizes)

    sdk = re.search(r"(.*/zephyr-sdk-[^/]+)/", gcc)
    sdk_ver = open(os.path.join(sdk.group(1), "sdk_version")).read().strip() if sdk else ""
    meta = {
        "date": datetime.datetime.now().isoformat(timespec="seconds"),
        "board": "stm32f429i_disc1",
        "zephyr": {"version": zephyr_version(), **repo_info(os.path.join(WS, "zephyr"))},
        "mcuboot": repo_info(os.path.join(WS, "bootloader", "mcuboot")),
        "exp": repo_info(EXP),
        "zephyr_sdk": sdk_ver,
        "boot_builds": args.boot,
        "signed_image": image_layout(args.image),
    }
    with open(os.path.join(args.outdir, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    print(json.dumps(meta, indent=2))


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return list(csv.DictReader(f))


def cmd_summary(args):
    d = args.outdir
    meta = json.load(open(os.path.join(d, "meta.json")))
    ok = read_csv(os.path.join(d, "boot_ok.csv"))
    rej = read_csv(os.path.join(d, "reject.csv"))
    sizes = read_csv(os.path.join(d, "build_size.csv"))
    L = [f"# {os.path.basename(os.path.normpath(d))}", ""]

    L += ["## Environment", "", "| Item | Value |", "|---|---|",
          f"| Date | {meta['date']} |", f"| Board | {meta['board']} |",
          f"| Zephyr | v{meta['zephyr']['version']} ({meta['zephyr']['commit']}) |",
          f"| MCUboot | {meta['mcuboot']['branch']} @ {meta['mcuboot']['commit']}"
          f"{' (dirty)' if meta['mcuboot']['dirty'] else ''} |",
          f"| exp | {meta['exp']['branch']} @ {meta['exp']['commit']}"
          f"{' (dirty)' if meta['exp']['dirty'] else ''} |",
          f"| Zephyr SDK | {meta['zephyr_sdk']} |",
          f"| Bootloader builds | {', '.join(meta['boot_builds'])} |", ""]

    img = meta["signed_image"]
    L += ["## Signed image", "", "| Part | Bytes |", "|---|---|",
          f"| Header | {img['header_bytes']} |", f"| Payload | {img['payload_bytes']} |"]
    L += [f"| TLV {t['type']} | {t['len']} |" for t in img["tlvs"]]
    L += [f"| TLV area total | {img['tlv_area_bytes']} |",
          f"| File | {img['file_bytes']} |", ""]

    if ok:
        hz = int(ok[0]["clock_hz"])
        L += [f"## Boot timing (valid image, {len(ok)} runs, {hz // 1_000_000} MHz)", "",
              "| Stage | mean cycles | min | max | stdev | mean ms |", "|---|---|---|---|---|---|"]
        for s in STAGES:
            v = [int(r[f"{s}_cyc"]) for r in ok if r[f"{s}_cyc"]]
            if not v:
                continue
            sd = statistics.pstdev(v)
            L.append(f"| {s} | {statistics.mean(v):,.0f} | {min(v):,} | {max(v):,} | "
                     f"{sd:,.1f} | {statistics.mean(v) / hz * 1000:.2f} |")
        L += ["", f"All runs booted: {all(r['booted'] == 'True' for r in ok)}; "
              f"results: {sorted({r['result'] for r in ok})}", ""]

    if rej:
        L += ["## Rejection tests", "",
              "| Case | result | booted | validate ms | hash ms | sig run | log |",
              "|---|---|---|---|---|---|---|"]
        for r in rej:
            hz = int(r["clock_hz"])
            ms = lambda k: f"{int(r[k]) / hz * 1000:.2f}" if r[k] else ""
            L.append(f"| {r['label']} | {r['result']} | {r['booted']} | {ms('validate_cyc')} | "
                     f"{ms('hash_cyc')} | {r['sig_n']} | {r['log']} |")
        L.append("")

    if sizes:
        L += ["## Bootloader size", "", "| Build | text | data | bss | FLASH used | RAM used |",
              "|---|---|---|---|---|---|"]
        for r in sizes:
            L.append(f"| {r['build']} | {r['text']} | {r['data']} | {r['bss']} | "
                     f"{r.get('flash_used_linker', '')} | {r.get('ram_used_linker', '')} |")
        L.append("")

    L += ["## Files", ""] + [f"- `{os.path.relpath(p, d)}`" for p in
                             sorted(glob.glob(os.path.join(d, "**", "*"), recursive=True))
                             if os.path.isfile(p) and not p.endswith("summary.md")]
    with open(os.path.join(d, "summary.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("meta")
    m.add_argument("outdir")
    m.add_argument("--image", required=True)
    m.add_argument("--boot", action="append", required=True)
    s = sub.add_parser("summary")
    s.add_argument("outdir")
    args = ap.parse_args()
    {"meta": cmd_meta, "summary": cmd_summary}[args.cmd](args)


if __name__ == "__main__":
    main()
