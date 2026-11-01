# ChkUp verdict — boot_mldsa65_chkup_dgp_seccnt_callgraph

Kconfig: BOOT_VALIDATE_SLOT0=y, MCUBOOT_DOWNGRADE_PREVENTION=y, MCUBOOT_DOWNGRADE_PREVENTION_SECURITY_COUNTER=y, MCUBOOT_HW_DOWNGRADE_PREVENTION=n, MCUBOOT_USE_TLV_ALLOW_LIST=y, BOOT_SWAP_USING_SCRATCH=y, BOOT_UPGRADE_ONLY=n

| property | verdict | verification procedures (caller -> key function) |
|---|---|---|
| authenticity | ok | bootutil_verify_sig -> mcuboot_mldsa_verify |
| integrity | ok | bootutil_sha_finish -> tc_sha256_final |
| freshness | ok | check_downgrade_prevention -> bootutil_get_img_security_cnt |
| compatibility | missing | - |
| P5_unsigned_field_use | ok | - |
| P6_rollback_value_protection | ok | SEC_CNT TLV, protected area only |

## Key calls on the path

| property | key function | caller:line | reaches condition | first condition | decision reaches |
|---|---|---|---|---|---|
| authenticity | mcuboot_mldsa_verify | bootutil_verify_sig:77 | True | `bootutil_verify_sig:261: if (rc_8 != 0)` | boot_go |
| freshness | bootutil_get_img_security_cnt | check_downgrade_prevention:1681 | True | `check_downgrade_prevention:1692: if (rc_10 != 0)` | boot_go |
| freshness | bootutil_get_img_security_cnt | check_downgrade_prevention:1689 | True | `check_downgrade_prevention:1684: if (rc_12 != 0)` | boot_go |
| integrity | tc_sha256_final | bootutil_sha_finish:235 | True | `bootutil_find_key:76: if (_19 == 0)` | boot_go |
| integrity | tc_sha256_final | bootutil_sha_finish:235 | True | `bootutil_img_validate:380: if (FIH_SUCCESS.673_11 != fih_rc_30)` | boot_go |

## TLV reads on the path (P5)

| func:line | type | protected only |
|---|---|---|
| bootutil_get_img_security_cnt:76 | IMAGE_TLV_SEC_CNT | True |
| bootutil_img_validate:311 | IMAGE_TLV_ANY | False |

allow-list check (bootutil_tlv_iter_is_prot -> condition): bootutil_img_validate:349=True
