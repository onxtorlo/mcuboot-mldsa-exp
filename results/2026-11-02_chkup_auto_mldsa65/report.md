# ChkUp report — 2026-11-02_chkup_auto_mldsa65

## 정적 판정 (1-3단계)

| 빌드 | 진위 | 무결성 | 최신성 | 호환성 | P5 서명 외 필드 | P6 rollback 값 | 경보 |
|---|---|---|---|---|---|---|---|
| mldsa65 | ok | ok | **missing** | **missing** | ok | n/a | 2 |
| mldsa65_chkup_dgp | ok | ok | ok | **missing** | ok | ok | 1 |
| mldsa65_chkup_hwdgp | ok | ok | ok | **missing** | ok | **improper** | 2 |
| mldsa65_chkup_noval0 | **partial** | **partial** | **missing** | **missing** | ok | n/a | 4 |
| mldsa65_chkup_noallow | ok | ok | **missing** | **missing** | **improper** | n/a | 3 |
| mldsa65_chkup_overwrite | ok | ok | **missing** | **missing** | ok | n/a | 2 |
| mldsa65_chkup_dgp_seccnt | ok | ok | ok | **missing** | ok | **improper** | 2 |
| mldsa65_chkup_overwrite_chkup_dgp | ok | ok | ok | **missing** | ok | ok | 1 |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | ok | ok | ok | **missing** | **improper** | **improper** | 3 |

## 보드 검증 (4단계)

| 빌드 | 경보 | TP | FP | 음성 검사 | TN | FN | 비고 |
|---|---|---|---|---|---|---|---|
| mldsa65 | 2 | 2 | 0 | 6 | 6 | 0 | baseline ok |
| mldsa65_chkup_dgp | 1 | 1 | 0 | 10 | 10 | 0 | baseline ok |
| mldsa65_chkup_hwdgp | 2 | - | - | - | - | - | 빌드 불가 (정적만) |
| mldsa65_chkup_noval0 | 4 | 4 | 0 | 1 | 1 | 0 | baseline ok |
| mldsa65_chkup_noallow | 3 | 3 | 0 | 5 | 5 | 0 | baseline ok |
| mldsa65_chkup_overwrite | 2 | 2 | 0 | 7 | 7 | 0 | baseline ok |
| mldsa65_chkup_dgp_seccnt | 2 | 2 | 0 | 9 | 9 | 0 | baseline ok |
| mldsa65_chkup_overwrite_chkup_dgp | 1 | 1 | 0 | 10 | 10 | 0 | baseline ok |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | 3 | 3 | 0 | 8 | 8 | 0 | baseline ok |

- 합계: TP 18, FP 0, TN 56, FN 0
- 경보 정밀도(TP/(TP+FP)): 18/18 = 100.0%
- 음성 검사 미탐(FN/(TN+FN)): 0/56 = 0.0%

## 케이스별

| 빌드 | 케이스 | 속성 | 경보 | PoC | 관찰 | 결과 |
|---|---|---|---|---|---|---|
| mldsa65 | fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | TP |
| mldsa65 | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65 | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65 | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65 | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65 | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65 | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65 | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_dgp | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_dgp | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_dgp | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_dgp | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_dgp | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_dgp | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_dgp | fresh_older | freshness | - | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v2 | TN |
| mldsa65_chkup_dgp | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa65_chkup_dgp | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_dgp | p6_equal_counter | P6 | - | older image with the same security counter (5 -> 5) | v2 | TN |
| mldsa65_chkup_dgp | p6_unprot_counter | P6 | - | older image cnt1 + SEC_CNT=10 in the unprotected area | v2 | TN |
| mldsa65_chkup_noval0 | slot0_tamper | authenticity | partial | running image (slot0) modified, no upgrade | v1-tampered | TP |
| mldsa65_chkup_noval0 | slot0_tamper_integrity | integrity | partial | running image (slot0) modified, no upgrade | v1-tampered | TP |
| mldsa65_chkup_noval0 | fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | TP |
| mldsa65_chkup_noval0 | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_noval0 | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_noallow | fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | TP |
| mldsa65_chkup_noallow | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_noallow | p5_inject | P5 | improper | TLV injected in the unprotected area | v2 | TP |
| mldsa65_chkup_noallow | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_noallow | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_noallow | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_noallow | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_noallow | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_overwrite | fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | TP |
| mldsa65_chkup_overwrite | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_overwrite | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_overwrite | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_overwrite | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_overwrite | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_overwrite | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_overwrite | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa65_chkup_overwrite | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_dgp_seccnt | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_dgp_seccnt | p6_equal_counter | P6 | improper | older image with the same security counter (5 -> 5) | v1 | TP |
| mldsa65_chkup_dgp_seccnt | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_dgp_seccnt | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_dgp_seccnt | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_dgp_seccnt | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_dgp_seccnt | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_dgp_seccnt | fresh_older | freshness | - | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v2 | TN |
| mldsa65_chkup_dgp_seccnt | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa65_chkup_dgp_seccnt | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_dgp_seccnt | p6_unprot_counter | P6 | - | older image cnt1 + SEC_CNT=10 in the unprotected area | v2 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_overwrite_chkup_dgp | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_overwrite_chkup_dgp | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | fresh_older | freshness | - | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v2 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | p6_equal_counter | P6 | - | older image with the same security counter (5 -> 5) | v2 | TN |
| mldsa65_chkup_overwrite_chkup_dgp | p6_unprot_counter | P6 | - | older image cnt1 + SEC_CNT=10 in the unprotected area | v2 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | p5_inject | P5 | improper | TLV injected in the unprotected area | v2 | TP |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | p6_equal_counter | P6 | improper | older image with the same security counter (5 -> 5) | v1 | TP |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | fresh_older | freshness | - | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v2 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa65_chkup_dgp_seccnt_chkup_noallow | p6_unprot_counter | P6 | - | older image cnt1 + SEC_CNT=10 in the unprotected area | v2 | TN |
