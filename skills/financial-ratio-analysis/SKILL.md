---
name: financial-ratio-analysis
description: Computes standard commercial lending ratios including Debt Service Coverage Ratio (DSCR), Fixed Charge Coverage Ratio (FCCR), Leverage, and Liquidity metrics.
license: Apache-2.0
---

# Financial Ratio Analysis Skill

## Overview
This skill computes critical commercial credit underwriting ratios from historical and projected financial statements. All calculations are deterministic and adhere to GAAP/IFRS standards and institutional commercial credit policy.

## Key Formulas

### 1. Debt Service Coverage Ratio (DSCR)
$$\text{DSCR} = \frac{\text{Net Operating Income (NOI)}}{\text{Total Annual Debt Service}}$$
- **NOI Calculation**: Operating Revenue - Operating Expenses (excluding depreciation, amortization, and interest).
- **Benchmark Policy**:
  - Minimum Acceptable: **1.25x**
  - Target / Low Risk: **≥ 1.35x**
  - Subprime / Exception: **1.15x - 1.24x** (Requires Series 24 approval)
  - Critical Policy Failure: **< 1.15x** (Automatic Decline)

### 2. Fixed Charge Coverage Ratio (FCCR)
$$\text{FCCR} = \frac{\text{EBITDA} - \text{Unfunded CapEx} - \text{Cash Taxes} - \text{Distributions}}{\text{Principal Payments} + \text{Interest Expense} + \text{Lease Payments}}$$

### 3. Leverage (Debt-to-EBITDA)
$$\text{Leverage} = \frac{\text{Total Funded Debt}}{\text{Adjusted EBITDA}}$$
- Maximum Standard Ceiling: **3.5x**

### 4. Current Ratio (Liquidity)
$$\text{Current Ratio} = \frac{\text{Total Current Assets}}{\text{Total Current Liabilities}}$$
- Minimum Standard: **1.20x**

## Execution via Script
The skill includes a deterministic Python script at `scripts/calculate_ratios.py` that accepts a JSON financial payload and returns structured ratios and pass/fail policy compliance indicators.
