# SPDX-License-Identifier: Apache-2.0
# Standalone ML-DSA verify benchmark (no MCUboot): mldsa-native C backend,
# same board/clock/-Os as the bootloader measurements.
# Parameter set: -DMLDSA_LEVEL=44|65|87 (default 44); the vector comes from
# ${BENCH_VECTORS} (default src/bench_vectors.h), made by gen_vectors.py.

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(mldsa_bench)

set(MLDSA_DIR ${ZEPHYR_MLDSA_NATIVE_MODULE_DIR}/mldsa)
if(NOT DEFINED MLDSA_LEVEL)
  set(MLDSA_LEVEL 44)
endif()
if(NOT DEFINED BENCH_VECTORS)
  set(BENCH_VECTORS ${CMAKE_CURRENT_SOURCE_DIR}/src/bench_vectors.h)
endif()

target_sources(app PRIVATE src/main.c ${MLDSA_DIR}/mldsa_native.c)
target_include_directories(app PRIVATE ${MLDSA_DIR})
target_compile_definitions(app PRIVATE
  MLD_CONFIG_PARAMETER_SET=${MLDSA_LEVEL}
  MLD_CONFIG_NAMESPACE_PREFIX=mldsa
  BENCH_VECTORS="${BENCH_VECTORS}"
)
