#!/usr/bin/env python3
"""Combine per-configuration result directories into one comparison table.

usage: scripts/compare.py <stage dir>
  reads  <stage dir>/<conf>/{meta.json,boot_ok.csv,reject.csv,build_size.csv}
         <stage dir>/build_status.csv (optional)
  writes <stage dir>/comparison.csv   one row per configuration
         <stage dir>/comparison.md    tables for slides
"""
import csv
import json
import os
import statistics
import sys

STAGES = ["validate", "hash", "sig", "total"]


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return list(csv.DictReader(f))


def row_for(d):
    meta = json.load(open(os.path.join(d, "meta.json")))
    ok = read_csv(os.path.join(d, "boot_ok.csv"))
    rej = read_csv(os.path.join(d, "reject.csv"))
    sizes = {r["build"]: r for r in read_csv(os.path.join(d, "build_size.csv"))}
    conf = meta["conf"]
    img = meta["signed_image"]
    sig_tlv = [t for t in img["tlvs"] if t["type"] not in ("SHA256", "SHA384", "SHA512",
                                                          "KEYHASH", "PUBKEY", "SIG_PURE")]
    hz = int(ok[0]["clock_hz"]) if ok else 0
    row = {"conf": conf, "description": meta.get("conf_description", ""), "runs": len(ok)}
    for s in STAGES:
        v = [int(r[f"{s}_cyc"]) for r in ok if r.get(f"{s}_cyc") and int(r[f"{s}_n"] or 0) > 0]
        row[f"{s}_cyc"] = round(statistics.mean(v)) if v else ""
        row[f"{s}_cyc_stdev"] = round(statistics.pstdev(v), 1) if v else ""
        row[f"{s}_ms"] = round(statistics.mean(v) / hz * 1000, 3) if v and hz else ""
    row["stack_used"] = ok[0].get("stack_used", "") if ok else ""
    booted = sum(r["booted"] == "True" for r in ok)
    row["valid_booted"] = f"{booted}/{len(ok)}"
    row["valid_result"] = "/".join(sorted({r["result"] for r in ok}))
    # Timing only means something when the valid image actually verified
    row["works"] = bool(ok) and booted == len(ok)
    for r in rej:
        row[f"reject_{r['label']}"] = r["result"]
    plain, meas = sizes.get(conf, {}), sizes.get(f"{conf}_measure", {})
    row["boot_flash_bytes"] = plain.get("flash_used_linker", "")
    row["boot_ram_bytes"] = plain.get("ram_used_linker", "")
    row["measure_flash_bytes"] = meas.get("flash_used_linker", "")
    row["pubkey_bytes"] = plain.get("pubkey_bytes", "") or meas.get("pubkey_bytes", "")
    row["sig_tlv"] = sig_tlv[0]["type"] if sig_tlv else ""
    row["sig_bytes"] = sig_tlv[0]["len"] if sig_tlv else 0
    row["tlv_area_bytes"] = img["tlv_area_bytes"]
    row["payload_bytes"] = img["payload_bytes"]
    return row


def main():
    stage = sys.argv[1]
    rows = [row_for(os.path.join(stage, d)) for d in sorted(os.listdir(stage))
            if os.path.exists(os.path.join(stage, d, "meta.json"))]
    status = read_csv(os.path.join(stage, "build_status.csv"))

    fields = []
    for r in rows:
        fields += [k for k in r if k not in fields]
    with open(os.path.join(stage, "comparison.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, restval="")
        w.writeheader()
        w.writerows(rows)

    works = [r for r in rows if r["works"]]
    broken = [r for r in rows if not r["works"]]
    L = [f"# {os.path.basename(os.path.normpath(stage))}: signature comparison", "",
         "Valid image, mean of all runs (stdev in cycles). ms at 168 MHz.", "",
         "## Verification time (configurations that boot a valid image)", "",
         "| Configuration | sig ms | hash ms | validate ms | total ms | sig stdev (cyc) | valid image |",
         "|---|---|---|---|---|---|---|"]
    for r in works:
        L.append(f"| {r['conf']} | {r['sig_ms']} | {r['hash_ms']} | {r['validate_ms']} | "
                 f"{r['total_ms']} | {r['sig_cyc_stdev']} | booted {r['valid_booted']} |")
    if broken:
        L += ["", "## Built but rejected the valid image (timings are time to fail, not comparable)", "",
              "| Configuration | valid image | result | validate ms | sig ms |", "|---|---|---|---|---|"]
        for r in broken:
            L.append(f"| {r['conf']} | booted {r['valid_booted']} | {r['valid_result']} | "
                     f"{r['validate_ms']} | {r['sig_ms'] or '-'} |")
    L += ["", "## Size and memory", "",
          "| Configuration | MCUboot FLASH (B) | MCUboot RAM (B) | stack peak (B) | "
          "public key (B) | signature (B) | TLV area (B) | works |",
          "|---|---|---|---|---|---|---|---|"]
    for r in works + broken:
        L.append(f"| {r['conf']} | {r['boot_flash_bytes']} | {r['boot_ram_bytes']} | "
                 f"{r['stack_used']} | {r['pubkey_bytes']} | {r['sig_bytes']} | "
                 f"{r['tlv_area_bytes']} | {'yes' if r['works'] else 'no'} |")
    L += ["", "MCUboot FLASH/RAM: build without measurement. Stack peak: measurement build "
          "(for configurations that do not work it is the peak up to the failure).", "",
          "## Rejection tests", "",
          "| Configuration | bad payload | bad signature | wrong key |", "|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['conf']} | {r.get('reject_bad_payload', '-')} | "
                 f"{r.get('reject_bad_sig', '-')} | {r.get('reject_bad_key', '-')} |")
    L += ["", "## Configurations", "", "| Configuration | Description |", "|---|---|"]
    L += [f"| {r['conf']} | {r['description']} |" for r in rows]
    failed = [s for s in status if s["status"] != "ok"]
    if failed:
        L += ["", "## Configurations that did not build", "",
              "| Configuration | variant | first error |", "|---|---|---|"]
        L += [f"| {s['conf']} | {s['variant']} | {s['error']} |" for s in failed]
    with open(os.path.join(stage, "comparison.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
