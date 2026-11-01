# Notes / caveats — ChkUp on MCUboot (ML-DSA-65)

## 원 논문과 달라진 점 (구현 선택)
- 입력: 바이너리 대신 소스 빌드 산출물 (GCC `-fcallgraph-info`, `-fdump-tree-optimized-lineno`)
  - Kconfig·`#ifdef`·FIH 매크로가 풀린 뒤의 실제 컴파일 결과 → "설정마다 다른 펌웨어"로 취급
  - 분석 전용 빌드(인라인 off)는 플래싱·측정용과 코드 배치가 다름
- 2단계 함수 매칭: 이름 기반 (소스 빌드라 심볼 유지). ChkUp의 특징 유사도 + DFG 동형 단계 불필요
  - 코퍼스(`CORPUS` in scripts/chkup_analyze.py): Table 5를 MCUboot가 쓰는 라이브러리(TinyCrypt, mldsa-native, Mbed TLS/PSA)로 옮김 + MCUboot 자체 최신성·호환성 함수(ChkUp의 proprietary 함수에 해당)
- 반환값→조건 분기 확인: CodeQL 대신 GIMPLE SSA 위 자체 추적 (CodeQL 설치는 자동 권한 검사에서 거부됨)
  - flow-insensitive (함수 안 문장 순서 무시) → 과대 근사 가능
  - 함수 경계: 반환값, 출력 인자(포인터 매개변수), 조건 분기에 의한 제어 의존 반환까지 추적
  - 버퍼를 채우는 호출 자신의 반환값은 그 버퍼로 오염시키지 않음 (예: `bootutil_img_hash`의 rc)
- 4단계: 에뮬레이터 대신 실제 보드. ChkUp의 패칭(앞단 검증 우회)은 불필요했음 — 각 PoC가 대상 속성 외 검증을 정상 통과하도록 이미지를 구성

## 판정 해석
- 무결성 항목에 `bootutil_find_key`(공개키 해시 대조)가 함께 잡힘: SHA-256 결과가 분기로 가는 패턴이 같기 때문. 실제 역할은 서명 키 확인(진위)
- 호환성 missing: 단일 이미지 MCUboot에는 장치 ID 검사 자체가 없음. 장치 결속은 서명 키로만 이루어짐(키를 기기 계열마다 따로 쓰지 않으면 다른 기기용 이미지가 설치됨)
- slot0 재검증 끔: 속성 단위로는 검증 함수가 있으나, 검증 대상 슬롯이 slot1뿐 → partial로 판정
- 보안 카운터 방식: 비교가 `>`(엄격)라 같은 카운터의 구버전은 허용됨 — MCUboot Kconfig 도움말에 명시된 동작. 정적 P6 규칙은 값의 출처만 보고 비교 연산자는 보지 않음
- HW downgrade 방지: 이 보드용 `boot_nv_security_counter_*` 구현이 없어 링크 불가 → 정적 분석만

## 실험 환경 메모
- ST-Link가 실행 중 WSL에서 분리된 적 있음 → `usbipd attach --wsl --busid 1-4 --auto-attach`를 Windows 백그라운드로 유지
- slot1은 코어를 정지시킨 채로 기록(`reset halt; program; shutdown`), 캡처 시 처음 리셋 → swap·거부 로그를 놓치지 않음
- 다른 보드 이미지(`nucleo_f429zi`, 같은 STM32F429)는 콘솔 UART가 달라 앱 출력 없음 → MCUboot 로그(swap + jump)로 수락 판정
