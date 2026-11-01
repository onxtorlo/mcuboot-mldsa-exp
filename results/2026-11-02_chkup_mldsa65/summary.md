# ChkUp 구현 — MCUboot (ML-DSA-65, STM32F429I-DISC1)

## 개요
- ChkUp(USENIX Sec 2024) 4단계를 MCU 부트로더에 적용
  - 1 실행 경로 복원 → 2 검증 절차 인식 → 3 취약점 판정 → 4 보드 동적 검증
- 분석 대상: Kconfig 조합 6개 = 서로 다른 펌웨어 6개
- 서명: ML-DSA-65 / 이미지 해시: SHA-256(TinyCrypt)

## 단계별 구현
| 단계 | ChkUp 원 논문 | 본 구현 | 스크립트 |
|---|---|---|---|
| 1 | 바이너리 UFG + reboot 역추적 | GCC 호출 그래프, `main`→`do_boot` 경로 | `callgraph_paths.py` |
| 2 | 특징 유사도 + DFG 동형, 반환값→분기 | 이름 매칭 코퍼스, GIMPLE SSA 위 반환값·출력 인자→분기 추적(함수 경계 포함) | `chkup_analyze.py` |
| 3 | 4개 속성 missing/improper | 동일 + P5 서명 대상 외 필드, P6 anti-rollback 값 출처, 검증 슬롯 범위 | `chkup_analyze.py` |
| 4 | 에뮬레이터 + PoC (Table 2) | 실제 보드 + PoC 이미지 19건 | `chkup_images.py`, `chkup_poc.sh` |

## 2단계 결과 (기본 설정)
- 진위: `bootutil_verify_sig` → `mcuboot_mldsa_verify`, 첫 분기 `bootutil_verify_sig:261`
- 무결성: `bootutil_sha_finish` → `tc_sha256_final`, 출력 버퍼가 `boot_fih_memequal` 비교로 → 분기 `bootutil_img_validate:380`
- 두 판정 모두 반환값 경로로 `boot_validate_slot:647` → `boot_go`까지 도달

## 3단계 정적 판정
| 설정 | 진위 | 무결성 | 최신성 | 호환성 | P5 서명 외 필드 | P6 rollback 값 |
|---|---|---|---|---|---|---|
| 기본 | ok | ok | **missing** | **missing** | ok | n/a |
| + SW downgrade 방지(버전) | ok | ok | ok | missing | ok | ok (헤더 ih_ver, 서명 대상) |
| + SW downgrade 방지(보안 카운터) | ok | ok | ok | missing | ok | ok (SEC_CNT, 보호 영역만) |
| + HW downgrade 방지 (링크 불가, 정적만) | ok | ok | ok | missing | ok | ok |
| slot0 재검증 끔 | **partial** | **partial** | missing | missing | ok | n/a |
| TLV allow-list 끔 | ok | ok | missing | missing | **improper** | n/a |

## 4단계 보드 검증 (19건, 예측 19/19 일치)
| 케이스 | 설정 | 속성 | PoC | 결과 | 의미 |
|---|---|---|---|---|---|
| B0 | 기본 | - | 정상 업그레이드 v1→v2 | v2 부팅 | 기준 |
| B1 | 기본 | 진위 누락 | 서명 없는 이미지 | 거부 | ok 확인 |
| B2 | 기본 | 무결성 누락 | 코드 1비트 변조 | 거부 | ok 확인 |
| **B3** | 기본 | 최신성 누락 | 정상 서명된 구버전(2.0.0→1.0.0) | **설치됨** | **missing 실증 (downgrade)** |
| **B4** | 기본 | 호환성 누락 | 다른 보드용 이미지, 같은 키 | **설치·점프** | **missing 실증** |
| B5 | 기본 | 진위 부적절 | 다른 ML-DSA 키로 서명 | 거부 | ok 확인 |
| B6 | 기본 | 무결성 부적절 | 변조 + SHA256 TLV 교체 | 거부 | 해시가 서명 대상 |
| B7 | 기본 | 최신성 부적절 | 구버전 헤더 버전만 3.0.0으로 수정 | 거부 | 헤더가 서명 대상 |
| B8 | 기본 | P5 | 비보호 영역에 SEC_CNT TLV 주입 | 거부 | allow-list 동작 |
| B9 | 기본 | 무결성(slot0) | slot0 문자열 변조 | 부팅 거부 | slot0 재검증 동작 |
| D0 | SW 방지(버전) | - | 정상 업그레이드 | v2 | 기준 |
| D3 | SW 방지(버전) | 최신성 | 구버전 | 삭제·거부 | ok 확인 |
| D7 | SW 방지(버전) | 최신성 부적절 | 헤더 버전 위조 | 거부 | ok 확인 |
| S0 | SW 방지(카운터) | - | 정상 업그레이드, 카운터 1→5 | v2 | 기준 |
| S3 | SW 방지(카운터) | 최신성 | 카운터 5→1 | 삭제·거부 | ok 확인 |
| **S4** | SW 방지(카운터) | P6 | 구버전, 같은 카운터 5→5 | **설치됨** | **카운터 동일 시 downgrade 허용** |
| SN | 카운터 + allow-list 끔 | P6 | 카운터 5→1 + 비보호 SEC_CNT=10 주입 | 삭제·거부 | 보호 영역 값만 사용 (CVE-2024-32883 수정 유지) |
| **N8** | allow-list 끔 | P5 | 비보호 TLV 주입 | **설치됨** | **improper 실증** |
| **V9** | slot0 재검증 끔 | 무결성(slot0) | slot0 문자열 변조 | **변조 이미지 부팅** | **partial 실증** |

## 결론
- 정적 판정의 missing/partial/improper 4종 모두 보드에서 실제 설치·부팅으로 재현 (B3, B4, N8, V9)
- 4개 속성·P5에서 정적 판정 ok 항목은 모든 PoC에서 거부 확인 → 이번 범위에서 오탐·미탐 없음
- 예외: P6 정적 규칙은 S4를 놓침(미탐 1건)
- 추가 관찰: 보안 카운터 방식은 동일 카운터의 구버전을 허용 (S4) — 정적 P6 규칙은 값 출처만 보므로 미검출, 비교 연산자 규칙 추가 필요
- 기본 설정의 위험: downgrade 방지 비활성 + 장치 결속 없음 → 정상 서명된 구버전·타 기기 이미지 설치 가능

## 파일
- `static/<설정>/`: verdict.md, verdict.json, procedures.tsv, tlv_reads.tsv / `static/verdict_matrix.md`
- `poc/`: poc.csv, logs/<케이스>.log, images/(PoC 이미지 + info.txt)
- `meta.json`, `notes.md`
