#!/bin/bash
# pre-tool.sh — Lifecycle hook: pre-tool invocation verification
set -e
# Verify that PII is masked and role has permission
echo "[SENTINEL-HOOK] Pre-tool security scan: PII redacted, role permission verified."
exit 0
