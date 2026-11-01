# ChkUp report — 2026-11-02_chkup_auto_mldsa87

## 정적 판정 (1-3단계)

| 빌드 | 진위 | 무결성 | 최신성 | 호환성 | P5 서명 외 필드 | P6 rollback 값 | 경보 |
|---|---|---|---|---|---|---|---|
| mldsa87 | ok | ok | **missing** | **missing** | ok | n/a | 2 |

## 보드 검증 (4단계)

| 빌드 | 경보 | TP | FP | 음성 검사 | TN | FN | 비고 |
|---|---|---|---|---|---|---|---|
| mldsa87 | 2 | 2 | 0 | 7 | 7 | 0 | baseline ok |

- 합계: TP 2, FP 0, TN 7, FN 0
- 경보 정밀도(TP/(TP+FP)): 2/2 = 100.0%
- 음성 검사 미탐(FN/(TN+FN)): 0/7 = 0.0%

## 케이스별

| 빌드 | 케이스 | 속성 | 경보 | PoC | 관찰 | 결과 |
|---|---|---|---|---|---|---|
| mldsa87 | fresh_older | freshness | missing | older validly signed image (2.0.0/cnt5 -> 1.0.0/cnt1) | v1 | TP |
| mldsa87 | comp_otherboard | compatibility | missing | image built for another board, signed with the same key | accepted | TP |
| mldsa87 | auth_unsigned | authenticity | - | unsigned image (hash TLV only) | v1 | TN |
| mldsa87 | auth_wrongkey | authenticity | - | signed with another key of the same type | v1 | TN |
| mldsa87 | slot0_tamper | authenticity | - | running image (slot0) modified, no upgrade | none | TN |
| mldsa87 | integ_modified | integrity | - | payload modified, nothing else | v1 | TN |
| mldsa87 | integ_rehash | integrity | - | payload modified + SHA256 TLV replaced | v1 | TN |
| mldsa87 | fresh_setver | freshness | - | older image, header version raised to 3.0.0 (not re-signed) | v2 | TN |
| mldsa87 | p5_inject | P5 | - | TLV injected in the unprotected area | v1 | TN |
