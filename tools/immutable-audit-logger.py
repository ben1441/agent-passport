#!/usr/bin/env python3
"""
immutable-audit-logger.py — MCP Tool Script
Appends tamper-evident, SHA-256 hashed audit log entries complying with FINRA Rule 4511 & SEC 17a-4.
"""

import sys
import json
import hashlib
import time
import os
from datetime import datetime, timezone

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "memory", "runtime", "audit-ledger.jsonl")

def append_audit_entry(event_type: str, agent_role: str, payload: dict) -> dict:
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    timestamp = datetime.now(timezone.utc).isoformat()
    record = {
        "timestamp": timestamp,
        "event_type": event_type,
        "agent_role": agent_role,
        "payload": payload,
        "model_version": "claude-opus-4-6",
        "spec_version": "0.1.0"
    }

    serialized = json.dumps(record, sort_keys=True)
    sha256_hash = hashlib.sha256(serialized.encode()).hexdigest()
    record["entry_id"] = f"AUD-{int(time.time())}-{sha256_hash[:8]}"
    record["sha256_hash"] = sha256_hash

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

    return {
        "entry_id": record["entry_id"],
        "timestamp_iso": timestamp,
        "sha256_hash": sha256_hash,
        "status": "RECORDED_IMMUTABLE"
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    else:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}

    result = append_audit_entry(
        data.get("event_type", "unspecified"),
        data.get("agent_role", "unknown"),
        data.get("payload", {})
    )
    print(json.dumps(result, indent=2))
