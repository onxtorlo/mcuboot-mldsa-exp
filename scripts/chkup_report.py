#!/usr/bin/env python3
"""Collect a chkup.sh run into one report: static verdict matrix + board validation totals.

usage: scripts/chkup_report.py <outdir>      (writes <outdir>/report.md)
"""
import csv
import json
import os
import sys

PROPS = ["authenticity", "integrity", "freshness", "compatibility",
         "P5_unsigned_field_use", "P6_rollback_value_protection"]
SHORT = ["진위", "무결성", "최신성", "호환성", "P5 서명 외 필드", "P6 rollback 값"]


def cell(v):
    w = v.split()[0]
    return {"ok": "ok", "missing": "**missing**", "improper": "**improper**",
            "partial": "**partial**", "n/a": "n/a"}.get(w, v)


def main():
    out = sys.argv[1]
    names = sorted(os.listdir(os.path.join(out, "static")), key=lambda n: (len(n), n))
    md = ["# ChkUp report — " + os.path.basename(os.path.normpath(out)), "",
          "## 정적 판정 (1-3단계)", "", "| 빌드 | " + " | ".join(SHORT) + " | 경보 |",
          "|---" * (len(PROPS) + 2) + "|"]
    for n in names:
        d = json.load(open(os.path.join(out, "static", n, "verdict.json")))
        md.append(f"| {n} | " + " | ".join(cell(d["verdict"][p]["verdict"]) for p in PROPS)
                  + f" | {len(d['alerts'])} |")

    md += ["", "## 보드 검증 (4단계)", "",
           "| 빌드 | 경보 | TP | FP | 음성 검사 | TN | FN | 비고 |", "|---|---|---|---|---|---|---|---|"]
    tot = {"TP": 0, "FP": 0, "TN": 0, "FN": 0}
    details = []
    for n in names:
        d = json.load(open(os.path.join(out, "static", n, "verdict.json")))
        f = os.path.join(out, "poc", n, "validation.csv")
        if not os.path.exists(f):
            why = "빌드 불가 (정적만)" if os.path.exists(os.path.join(out, "static", n, "not_flashable")) else "미실행"
            md.append(f"| {n} | {len(d['alerts'])} | - | - | - | - | - | {why} |")
            continue
        rows = list(csv.DictReader(open(f)))
        c = {k: sum(1 for r in rows if r["result"] == k) for k in tot}
        for k in tot:
            tot[k] += c[k]
        base = rows[0]["result"] if rows else "?"
        md.append(f"| {n} | {len(d['alerts'])} | {c['TP']} | {c['FP']} | {c['TN'] + c['FN']} | {c['TN']} | "
                  f"{c['FN']} | baseline {base} |")
        details += [f"| {n} | {r['case']} | {r['property']} | {r['alert']} | {r['poc']} | {r['observed']} | "
                    f"{r['result']} |" for r in rows[1:]]
    a = tot["TP"] + tot["FP"]
    neg = tot["TN"] + tot["FN"]
    md += ["", f"- 합계: TP {tot['TP']}, FP {tot['FP']}, TN {tot['TN']}, FN {tot['FN']}",
           f"- 경보 정밀도(TP/(TP+FP)): {tot['TP']}/{a}" + (f" = {tot['TP'] / a:.1%}" if a else ""),
           f"- 음성 검사 미탐(FN/(TN+FN)): {tot['FN']}/{neg}" + (f" = {tot['FN'] / neg:.1%}" if neg else ""),
           "", "## 케이스별", "", "| 빌드 | 케이스 | 속성 | 경보 | PoC | 관찰 | 결과 |",
           "|---|---|---|---|---|---|---|"] + details
    open(os.path.join(out, "report.md"), "w").write("\n".join(md) + "\n")
    print("\n".join(md[:len(names) + 12]))


if __name__ == "__main__":
    main()
