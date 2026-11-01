# Notes — ChkUp automated run (ML-DSA-65 + 44/87)

## Commands
- `scripts/chkup.sh mldsa65 mcuboot-mldsa-exp/results/2026-11-02_chkup_auto_mldsa65 --board --negative base dgp dgp_seccnt hwdgp noval0 noallow dgp_seccnt+noallow overwrite overwrite+dgp` (04:17 → 06:12; 44/87 done 06:39)
- `scripts/chkup.sh mldsa44 ... --board --negative base`, same for mldsa87
- `scripts/chkup_revalidate.sh mcuboot-mldsa-exp/results/2026-11-02_chkup_auto_mldsa65 mldsa65 mldsa65_chkup_dgp_seccnt mldsa65_chkup_dgp_seccnt_chkup_noallow` (06:40 → 07:08)

## Validator change during the run (why two builds were re-run)
- First pass: a P6 alert ran both P6 PoCs as alert checks. The alert says "equal security counter accepted", but `p6_unprot_counter` tests a different flaw (counter read from the unprotected area). Its rejection was scored FP: 1 FP each in dgp_seccnt and dgp_seccnt+noallow. This was a mapping error in the tool, not a false alarm on MCUboot.
- Fix (`chkup_validate.py`): `DETAIL_POCS` picks the PoC from the alert text. The property's other PoCs now run as negative checks even when the property has an alert.
- The validator file was replaced while the run was going:
  - Builds validated before the change: base, dgp, noval0, noallow. Their results stand, but they have fewer negative PoCs. For example, base has no `fresh_setver` row because freshness had an alert.
  - Builds validated after it: overwrite, overwrite+dgp, ML-DSA-44/87.
  - The two affected builds were re-run with `chkup_revalidate.sh`. The old poc/ directories were removed after the successful re-run.
- Same reason: base has 6 negative PoCs on 65 and 7 on 44/87.

## Observations
- HW downgrade prevention: still does not link (no `boot_nv_security_counter_*` for this board), so static analysis only. The static P6 improper comes from the same strict-comparison rule.
- overwrite-only gives the same static verdicts as swap-scratch. The board shows the same TP pattern (downgrade + other-board accepted).
- `p6_unprot_counter` on dgp_seccnt+noallow: the image is accepted structurally, then erased by downgrade prevention (marker `downgrade-erased`). This shows the protected counter (1) was used, not the injected one (10).

## Files
- `static/<build>/verdict.{json,md}`, `procedures.tsv`, `tlv_reads.tsv`; `not_flashable` for hwdgp
- `poc/<build>/validation.{csv,md}`, `counts.json`, `logs/`, `images/info.txt` (`.bin` files are gitignored)
- `report.md` (made by `chkup_report.py`), `run.log`
