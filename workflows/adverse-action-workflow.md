# Workflow: Adverse Action & ECOA Compliance Notice

## Context & Regulatory Authority
Under the **Equal Credit Opportunity Act (ECOA, 15 U.S.C. 1691 et seq.)** and **CFPB Regulation B (12 CFR Part 1002)**, when an application for commercial or business credit is declined, or approved on terms less favorable than requested, the creditor must provide specific, actionable reasons for the adverse action.

## Operational Steps

1. **Adverse Determination Ingestion**:
   - `risk-officer` records the rationale for declining the application (e.g., DSCR < 1.25x, excessive funded leverage > 3.5x, inadequate liquidity).
2. **Principal Reason Attribution**:
   - Must identify the top 4 primary quantitative factors contributing to the decline.
   - Prohibited factors (geographic redlining, protected demographic classes) must be rigorously filtered out.
3. **Drafting Notice of Adverse Action**:
   - Name and address of applicant.
   - Statement of action taken.
   - Specific reasons for denial.
   - ECOA notice of rights and federal regulator contact information (CFPB / OCC / Federal Reserve).
4. **Independent Audit Verification**:
   - `compliance-auditor` reviews the draft notice for fair lending compliance.
   - Verifies that reasons accurately match the mathematical findings in the credit memo.
5. **Supervisory Signoff & Permanent Archival**:
   - Delivery to applicant within 30 days of completed application.
   - Retention of notice and supporting underwriting records for a minimum of 25 months (commercial) or 6 years (broker-dealer/FINRA standard).
