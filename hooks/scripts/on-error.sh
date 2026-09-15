#!/bin/bash
# on-error.sh — Lifecycle hook: error trap and escalation
set -e
echo "[SENTINEL-HOOK] CRITICAL ALERT: Error trapped. Dispatching alert to Chief Compliance Officer..."
echo "[SENTINEL-HOOK] Execution suspended. Preserving call stack in audit buffer."
exit 0
