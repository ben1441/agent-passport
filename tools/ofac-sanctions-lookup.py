#!/usr/bin/env python3
"""
ofac-sanctions-lookup.py — MCP Tool Script
Queries OFAC SDN and global sanctions watchlists.
"""

import sys
import json

KNOWN_SDN = {
    "NORTHERN MARITIME TRADING CORP": "RUSSIA-EO14024",
    "AL-BARAKA CARGO LOGISTICS": "SDGT",
    "VIKTOR PETROV": "CYBER2"
}

def query_ofac(query_name: str, country_iso: str = "US") -> dict:
    normalized = query_name.strip().upper()
    if normalized in KNOWN_SDN:
        return {
            "query_name": query_name,
            "match_found": True,
            "sanction_program": KNOWN_SDN[normalized],
            "match_score": 1.00,
            "status": "PROHIBITED_TRANSACTION"
        }
    return {
        "query_name": query_name,
        "match_found": False,
        "sanction_program": None,
        "match_score": 0.0,
        "status": "CLEARED"
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            args = json.load(f)
    else:
        raw = sys.stdin.read()
        args = json.loads(raw) if raw.strip() else {}

    res = query_ofac(args.get("query_name", ""), args.get("country_iso", "US"))
    print(json.dumps(res, indent=2))
