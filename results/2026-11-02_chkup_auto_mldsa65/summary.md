# ChkUp 자동화 실행 — MCUboot (ML-DSA-65, Kconfig 9개 조합)

## 개요
- `scripts/chkup.sh` 한 번 실행: Kconfig 조합별 빌드 → 1~3단계 정적 판정 → 경보별 PoC 자동 선택 → 보드 실행 → TP/FP/TN/FN
- `--negative`: 경보 없는 속성의 PoC도 실행 → 미탐(FN) 측정
- 보드: STM32F429I-DISC1 · MCUboot v2.4.0 fork (sign-replace) · Zephyr v4.4.2 · 서명 ML-DSA-65
- 같은 도구로 ML-DSA-44/87 기본 설정도 실행 (`2026-11-02_chkup_auto_mldsa44`, `_mldsa87`)

## 정적 판정 (1~3단계)
| 설정 | 진위 | 무결성 | 최신성 | 호환성 | P5 | P6 | 경보 |
|---|---|---|---|---|---|---|---|
| 기본 (swap-scratch) | ok | ok | **missing** | **missing** | ok | n/a | 2 |
| + downgrade 방지 (버전) | ok | ok | ok | **missing** | ok | ok | 1 |
| + downgrade 방지 (보안 카운터) | ok | ok | ok | **missing** | ok | **improper** | 2 |
| + HW downgrade 방지 (링크 불가) | ok | ok | ok | **missing** | ok | **improper** | 2 |
| slot0 재검증 끔 | **partial** | **partial** | **missing** | **missing** | ok | n/a | 4 |
| TLV allow-list 끔 | ok | ok | **missing** | **missing** | **improper** | n/a | 3 |
| 보안 카운터 + allow-list 끔 | ok | ok | ok | **missing** | **improper** | **improper** | 3 |
| overwrite-only | ok | ok | **missing** | **missing** | ok | n/a | 2 |
| overwrite-only + 버전 방지 | ok | ok | ok | **missing** | ok | ok | 1 |

- ML-DSA-44 / 87 기본: 65 기본과 동일 (ok / ok / missing / missing / ok / n/a)
- P6 improper = 보안 카운터 비교가 엄격 비교(`>`) → 같은 카운터의 구버전 허용 (새 비교 연산자 규칙)

## 보드 검증 (4단계)
| 설정 | 경보 PoC | TP | FP | 음성 PoC | TN | FN |
|---|---|---|---|---|---|---|
| 기본 | 2 | 2 | 0 | 6 | 6 | 0 |
| + 버전 방지 | 1 | 1 | 0 | 10 | 10 | 0 |
| + 보안 카운터 | 2 | 2 | 0 | 9 | 9 | 0 |
| + HW 방지 | - | - | - | - | - | - (링크 불가) |
| slot0 재검증 끔 | 4 | 4 | 0 | 1 | 1 | 0 |
| allow-list 끔 | 3 | 3 | 0 | 5 | 5 | 0 |
| 보안 카운터 + allow-list 끔 | 3 | 3 | 0 | 8 | 8 | 0 |
| overwrite-only | 2 | 2 | 0 | 7 | 7 | 0 |
| overwrite-only + 버전 방지 | 1 | 1 | 0 | 10 | 10 | 0 |
| **ML-DSA-65 합계** | 18 | **18** | **0** | 56 | 56 | **0** |
| ML-DSA-44 기본 | 2 | 2 | 0 | 7 | 7 | 0 |
| ML-DSA-87 기본 | 2 | 2 | 0 | 7 | 7 | 0 |

- 전체: TP 22, FP 0, TN 70, FN 0 → 경보 정밀도 22/22, 음성 PoC 미탐 0/70
- 모든 빌드에서 기준 업그레이드(v1/cnt1 → v2/cnt5) 정상 후 진행

## 실증된 취약 동작 (TP)
- 최신성 missing: 정상 서명된 구버전 설치 (downgrade 방지 꺼진 설정 전부)
- 호환성 missing: 다른 보드(nucleo_f429zi)용 이미지 설치·점프 (모든 설정)
- P5 improper: allow-list 끔 → 비보호 영역 TLV 주입 이미지 설치
- partial: slot0 재검증 끔 → 변조된 실행 이미지 부팅
- P6 improper: 보안 카운터 방식 → 같은 카운터(5 → 5)의 구버전 설치
- 거부 확인: 서명 없음·다른 키, 페이로드 변조·해시 교체, 헤더 버전 위조, 비보호 SEC_CNT 주입 (CVE-2024-32883 수정 유지)

## 결론
- 정적 경보 22건 모두 보드에서 재현, 경보 없는 속성 70건 모두 거부 → 이번 범위에서 오탐·미탐 없음
- 수동 실행(`2026-11-02_chkup_mldsa65`)의 P6 미탐(S4)은 비교 연산자 규칙으로 해소
- 서명 레벨(44/65/87)은 판정·동작에 영향 없음
