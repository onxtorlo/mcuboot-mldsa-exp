# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(hello)

# Tag printed at boot to tell images apart (e.g. -DAPP_TAG=v2)
if(NOT DEFINED APP_TAG)
  set(APP_TAG v1)
endif()
target_compile_definitions(app PRIVATE APP_TAG="${APP_TAG}")

target_sources(app PRIVATE src/main.c)
