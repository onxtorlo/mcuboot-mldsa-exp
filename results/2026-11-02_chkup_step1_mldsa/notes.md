# Notes / caveats — ChkUp step 1, ML-DSA-44/65/87

- 분석 전용 빌드(인라인 off)라 측정·플래싱용 바이너리와 코드 배치가 다름. 경로 분석에만 사용.
- 호출 그래프는 함수 단위. 함수 내부의 분기 조건(어떤 경우에 어느 호출이 실행되는지)은 아직 없음 → 2단계에서 반환값→조건 분기 확인 시 필요.
- 트리의 순서는 호출 지점의 소스 줄 번호 순. 실제 실행 순서의 근사이며 분기에 따라 일부만 실행됨.
- `(see above)`: 이미 펼친 함수의 재호출. 서브트리는 처음 나온 위치에만 표시.
- `[no definition in build]`: `memcmp`/`memset`(GCC 내장으로 처리), `mcuboot_watchdog_*`(빈 매크로). `boot_fih_memequal`→`memcmp`는 해시 비교 지점이라 2단계에서 중요.
- `[indirect call]`: 1개, `do_boot`의 이미지 점프(종료점)뿐. 암호 라이브러리 내부는 리프 처리로 탐색하지 않음.
- 가지치기 이름 규칙(`z_`, `k_`, `sys_` 등)이 넓음. `z_arm_clear_arm_mpu_config`처럼 MCUboot 정의 함수도 숨겨질 수 있음 → 미도달 목록 대조로 확인함.
- `callgraph.json`의 `defs`는 이름 충돌 시(같은 이름의 weak/strong) 마지막 정의로 덮어씀. 경로 영향 여부는 아직 미확인.
