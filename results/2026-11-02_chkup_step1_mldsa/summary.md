# ChkUp 1단계(실행 경로 복원) — MCUboot ML-DSA

## 목적
- ChkUp(USENIX Sec 2024) 1단계 Execution Path Recovery를 MCUboot에 적용
- 서명 알고리즘: ML-DSA-44/65/87 (mldsa-native, SHA-256 이미지 해시는 TinyCrypt)
- 분석 범위: 새 이미지가 slot1에 존재하는 시점 ~ 새 이미지로 점프(`do_boot`)
  - ChkUp의 "펌웨어 수신 ~ reboot"에 대응

## 방법
- 분석 전용 빌드: `boot_conf/mldsa{44,65,87}.conf` + `boot_conf/callgraph.conf`
  - GCC `-fcallgraph-info`: 번역 단위별 호출 그래프(.ci) 생성
  - 인라인 비활성화: 소스 함수마다 노드 유지
  - Kconfig·`#ifdef`·FIH 매크로가 풀린 뒤의 실제 컴파일 경로 반영
- `scripts/callgraph_paths.py`: .ci 병합 → `main`에서 호출 순서대로 DFS
  - ChkUp A.1 경로 폭발 감소 규칙 적용: 로그·assert·libc·커널 유틸 제외, 암호·flash API는 경계(리프)로 유지

## 결과
| 항목 | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|---|---|---|---|
| 분석 빌드 FLASH | 41,500 B | 42,188 B | 42,636 B |
| `main`에서 도달(가지치기 후) | 197 | 197 | 197 |
| MCUboot / 암호 API / flash API | 168 / 4 / 14 | 168 / 4 / 14 | 168 / 4 / 14 |

- 세 레벨의 호출 경로 동일 (차이는 파라미터뿐)
- 복원된 상위 경로: `main` → `boot_go` → `context_boot_go` → `boot_prepare_image_for_update` → … → `do_boot`
- 검증 경로: `boot_validated_swap_type` → `boot_validate_slot` → `boot_check_image` → `bootutil_img_validate`
  - 무결성: `bootutil_img_hash`(TinyCrypt SHA-256) → `boot_fih_memequal`(해시 비교)
  - 진위: `bootutil_find_key`(키 해시 비교) → `bootutil_verify_sig` → `mcuboot_mldsa_verify`
- 설치 경로: `boot_perform_update` → `boot_swap_image` → `swap_run`(swap-scratch)
- 경로 위 암호 API 4개: `tc_sha256_init/update/final`, `mcuboot_mldsa_verify`

## 정답 대조
- 핵심 함수 대조: 검증·설치·종료 함수 모두 경로에 포함
- 경로에 없는 함수
  - `boot_copy_image`: overwrite-only 모드 전용 → swap-scratch 설정에 없음, 정상
  - `boot_version_cmp`, `boot_update_security_counter`: downgrade prevention 비활성 → 최신성(버전·보안 카운터) 검증 코드 자체가 경로에 없음
    - ChkUp 기준 "최신성 검증 누락" 후보 → 3단계 판정 대상

## 다음 단계
- Kconfig 조합(downgrade prevention, swap 방식 등)별 경로 비교
- 2단계: 경로 위 암호 API·비교 함수를 코퍼스와 매칭, 반환값의 분기 유입 확인
