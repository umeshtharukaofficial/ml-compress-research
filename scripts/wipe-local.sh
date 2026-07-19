#!/usr/bin/env bash
# scripts/wipe-local.sh — run after every successful git push
set -euo pipefail
REPO_DIR="$(git rev-parse --show-toplevel)"
cd "$(dirname "$REPO_DIR")"
rm -rf "$REPO_DIR"
echo "✅ local repo wiped: $REPO_DIR"
