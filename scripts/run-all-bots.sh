#!/usr/bin/env bash
# scripts/run-all-bots.sh - Launches active bot agents concurrently in isolated workspace folders
set -euo pipefail
REPO="https://github.com/umeshtharukaofficial/ml-compress-research.git"

run_bot () {
  local ID="$1"
  local INTERVAL="$2"
  while true; do
    WS="workspace-bot-$ID"
    rm -rf "$WS"
    git clone --depth=1 "$REPO" "$WS"
    if [ -d "$WS" ]; then
      (
        cd "$WS"
        git pull --rebase || true
        # Find agent script dynamically
        BOT_DIR=$(find bots -type d -name "bot-$ID-*" | head -n 1)
        if [ -n "$BOT_DIR" ] && [ -f "$BOT_DIR/main.py" ]; then
          python3 "$BOT_DIR/main.py" || echo "bot-$ID execution failed"
        elif [ "$ID" = "20" ] && [ -f "bots/bot-20-orchestrator/tick.py" ]; then
          python3 "bots/bot-20-orchestrator/tick.py" || echo "bot-$ID orchestrator execution failed"
        fi
        
        git config user.name "bot-$ID"
        git config user.email "bot$ID@ml-compress.local"
        git add -A
        git commit -m "[bot-$ID] routine research execution tick" || true
        git push || (git pull --rebase && git push) || true
      )
      rm -rf "$WS"
    fi
    sleep "$INTERVAL"
  done
}

# Run bots concurrently matching priority schedules
run_bot 20 300 & # Bot-20: every 5 minutes
run_bot 01 21600 & # Bot-01: every 6 hours
run_bot 02 43200 & # Bot-02: every 12 hours
run_bot 03 86400 & # Bot-03: daily
run_bot 04 3600 & # Bot-04: hourly
run_bot 05 300 & # Bot-05: every 5 minutes
wait
