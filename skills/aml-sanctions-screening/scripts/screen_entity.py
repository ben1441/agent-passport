#!/usr/bin/env python3
"""
screen_entity.py — OFAC SDN and AML Watchlist Screening Engine
Performs name, TIN/EIN, and beneficial owner screening against simulated OFAC/PEP watchlists.
"""

import sys
import json
import difflib

# Simulated OFAC SDN & Watchlist database
SANCTIONED_ENTITIES = [
    {"name": "NORTHERN MARITIME TRADING CORP", "id": "OFAC-SDN-1092", "type": "Entity", "program": "RUSSIA-EO14024"},
    {"name": "AL-BARAKA CARGO LOGISTICS", "id": "OFAC-SDN-8821", "type": "Entity", "program": "SDGT"},
    {"name": "VIKTOR PETROV", "id": "OFAC-SDN-4310", "type": "Individual", "program": "CYBER2"},
    {"name": "GLOBAL PETROCHEMICALS LTD", "id": "OFAC-SDN-7731", "type": "Entity", "program": "IRAN"}
]

PEP_WATCHLIST = [
    {"name": "MARCOS SILVA", "role": "Deputy Minister of Infrastructure", "country": "BR", "risk": "High"}
]

def screen(payload: dict) -> dict:
    target_name = payload.get("entity_name", "").strip().upper()
    beneficial_owners = [b.strip().upper() for b in payload.get("beneficial_owners", [])]
    all_names = [target_name] + beneficial_owners

    matches = []
    pep_flags = []

    for name in all_names:
        if not name:
            continue
        # Check OFAC list
        for sanctioned in SANCTIONED_ENTITIES:
            ratio = difflib.SequenceMatcher(None, name, sanctioned["name"]).ratio()
            if ratio > 0.85:
                matches.append({
                    "queried_name": name,
                    "matched_entry": sanctioned["name"],
                    "list_id": sanctioned["id"],
                    "sanction_program": sanctioned["program"],
                    "confidence_score": round(ratio, 2)
                })

        # Check PEP list
        for pep in PEP_WATCHLIST:
            ratio = difflib.SequenceMatcher(None, name, pep["name"]).ratio()
            if ratio > 0.85:
                pep_flags.append({
                    "queried_name": name,
                    "pep_name": pep["name"],
                    "role": pep["role"],
                    "country": pep["country"],
                    "confidence_score": round(ratio, 2)
                })

    status = "BLOCKED" if len(matches) > 0 else ("ESCALATE_PEP" if len(pep_flags) > 0 else "CLEARED")

    return {
        "entity_name": target_name,
        "screening_status": status,
        "ofac_matches": matches,
        "pep_flags": pep_flags,
        "cleared": status == "CLEARED",
        "requires_bsao_review": status != "CLEARED"
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            data = json.load(f)
    else:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}

    output = screen(data)
    print(json.dumps(output, indent=2))
