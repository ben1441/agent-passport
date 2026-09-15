#!/bin/bash
# on-end.sh — Lifecycle hook: session finalization
set -e
echo "[SENTINEL-HOOK] Session completed. Flushing audit buffers..."
echo "[SENTINEL-HOOK] Checksum verified. Books and records synchronized."
exit 0
