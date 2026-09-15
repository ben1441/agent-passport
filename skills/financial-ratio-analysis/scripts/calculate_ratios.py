#!/usr/bin/env python3
"""
calculate_ratios.py — Deterministic Financial Ratio Engine for Sentinel Risk
Computes DSCR, FCCR, Leverage, and Liquidity metrics from normalized financial statements.
"""

import sys
import json

def calculate_metrics(data: dict) -> dict:
    revenue = float(data.get("annual_revenue", 0.0))
    operating_expenses = float(data.get("operating_expenses", 0.0))
    noi = float(data.get("net_operating_income", revenue - operating_expenses))
    annual_debt_service = float(data.get("annual_debt_service", 0.0))
    ebitda = float(data.get("ebitda", noi))
    unfunded_capex = float(data.get("unfunded_capex", 0.0))
    cash_taxes = float(data.get("cash_taxes", 0.0))
    distributions = float(data.get("distributions", 0.0))
    lease_payments = float(data.get("annual_lease_payments", 0.0))
    total_funded_debt = float(data.get("total_funded_debt", 0.0))
    current_assets = float(data.get("current_assets", 0.0))
    current_liabilities = float(data.get("current_liabilities", 1.0))

    # DSCR Calculation
    dscr = round(noi / annual_debt_service, 2) if annual_debt_service > 0 else 999.0

    # Fixed Charge Coverage Ratio (FCCR)
    fixed_charge_numerator = ebitda - unfunded_capex - cash_taxes - distributions
    fixed_charge_denominator = annual_debt_service + lease_payments
    fccr = round(fixed_charge_numerator / fixed_charge_denominator, 2) if fixed_charge_denominator > 0 else 999.0

    # Leverage Ratio
    leverage = round(total_funded_debt / ebitda, 2) if ebitda > 0 else 999.0

    # Liquidity (Current Ratio)
    current_ratio = round(current_assets / current_liabilities, 2) if current_liabilities > 0 else 999.0

    # Policy evaluations
    policy_checks = {
        "dscr_pass": dscr >= 1.25,
        "dscr_exception_allowed": 1.15 <= dscr < 1.25,
        "fccr_pass": fccr >= 1.15,
        "leverage_pass": leverage <= 3.50,
        "current_ratio_pass": current_ratio >= 1.20
    }

    all_passed = (
        policy_checks["dscr_pass"] and
        policy_checks["fccr_pass"] and
        policy_checks["leverage_pass"] and
        policy_checks["current_ratio_pass"]
    )

    risk_grade = "Tier-1 (Prime)" if all_passed else (
        "Tier-2 (Subprime Exception)" if policy_checks["dscr_exception_allowed"] else "Tier-3 (Adverse Decline)"
    )

    return {
        "metrics": {
            "net_operating_income": noi,
            "annual_debt_service": annual_debt_service,
            "dscr": dscr,
            "fccr": fccr,
            "leverage": leverage,
            "current_ratio": current_ratio
        },
        "policy_checks": policy_checks,
        "risk_grade": risk_grade,
        "recommendation": "APPROVE" if all_passed else ("ESCALATE_EXCEPTION" if policy_checks["dscr_exception_allowed"] else "DECLINE")
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            inputs = json.load(f)
    else:
        raw_input = sys.stdin.read()
        inputs = json.loads(raw_input) if raw_input.strip() else {}

    results = calculate_metrics(inputs)
    print(json.dumps(results, indent=2))
