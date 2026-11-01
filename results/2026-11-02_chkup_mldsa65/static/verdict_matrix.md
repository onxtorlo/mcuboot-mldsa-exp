| 설정 | authenticity | integrity | freshness | compatibility | P5_unsigned_field_use | P6_rollback_value_protection |
|---|---|---|---|---|---|---|
| 기본 (swap-scratch, slot0 재검증, allow-list) | ok | ok | missing | missing | ok | n/a (no freshness check) |
| + SW downgrade 방지 (버전) | ok | ok | ok | missing | ok | ok |
| + SW downgrade 방지 (보안 카운터) | ok | ok | ok | missing | ok | ok |
| + HW downgrade 방지 (링크 불가, 정적만) | ok | ok | ok | missing | ok | ok |
| slot0 재검증 끔 | partial (upgrade only; primary slot not re-validated at boot) | partial (upgrade only; primary slot not re-validated at boot) | missing | missing | ok | n/a (no freshness check) |
| TLV allow-list 끔 | ok | ok | missing | missing | improper (unprotected TLVs not restricted) | n/a (no freshness check) |
