#!/usr/bin/env bash
# Build the test application (unsigned).
# usage: scripts/build_app.sh <tag>      e.g. v1, v2
set -euo pipefail
source "$(dirname "$0")/env.sh"

TAG=${1:?usage: $0 <tag>}
west build -p -b "$BOARD" "$EXP/apps/hello" -d "$BUILD/hello_$TAG" -- \
	-DAPP_TAG="$TAG" \
	-DEXTRA_DTC_OVERLAY_FILE="$PART_OVERLAY;$EXP/apps/hello/slot0.overlay"
