# SPDX-License-Identifier: Apache-2.0
# Standalone ML-DSA-44 verify benchmark (no MCUboot): mldsa-native C backend,
# same board/clock/-Os as the bootloader measurements.

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(mldsa_bench)

set(MLDSA_DIR ${ZEPHYR_MLDSA_NATIVE_MODULE_DIR}/mldsa)

target_sources(app PRIVATE src/main.c ${MLDSA_DIR}/mldsa_native.c)
target_include_directories(app PRIVATE ${MLDSA_DIR} ${CMAKE_CURRENT_BINARY_DIR})
target_compile_definitions(app PRIVATE
  MLD_CONFIG_PARAMETER_SET=44
  MLD_CONFIG_NAMESPACE_PREFIX=mldsa
)
