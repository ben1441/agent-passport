# Sentinel Risk — Segregation of Duties (SOD) Policy

## 1. Governance Framework
This document formalizes the Segregation of Duties (SOD) architecture governing the Sentinel Risk multi-agent system, formulated in compliance with FINRA Rule 3110, SEC Rule 17a-4, and Federal Reserve Supervisory Letter SR 11-7.

No single artificial agent or sub-agent possesses end-to-end authority over the commercial credit origination, underwriting, approval, and audit lifecycle.

## 2. Defined Roles & Scope of Authority

| Role ID | Assigned Agent | Permissions | Primary Responsibilities |
| :--- | :--- | :--- | :--- |
| **`maker`** | `credit-analyst` | `create`, `submit`, `read` | - Ingests financial statements and tax returns.<br>- Computes debt service ratios (DSCR, FCCR, Leverage).<br>- Authors the preliminary Credit Underwriting Memorandum.<br>- Cannot approve, reject, or commit credit facilities. |
| **`checker`** | `risk-officer` | `review`, `approve`, `reject` | - Independently inspects Maker calculations and assumptions.<br>- Executes downside sensitivity models and stress testing.<br>- Formulates final credit determination (Approve / Reject / Counter).<br>- Cannot modify primary financial inputs directly; must remand to Maker if adjustments are required. |
| **`auditor`** | `compliance-auditor` | `audit`, `report` | - Validates that Maker and Checker adhered to all regulatory rules.<br>- Verifies OFAC/AML clearance certificates and disclosure packages.<br>- Writes immutable audit log entries to the cryptographic ledger.<br>- Issues supervisory alerts for any policy violations or threshold breaches. |

## 3. Conflict of Interest Matrix
The following role combinations are strictly mutually exclusive:

```
[maker]     <---> [checker]   # Maker cannot approve its own work
[maker]     <---> [auditor]   # Maker cannot audit its own underwriting
[checker]   <---> [auditor]   # Checker cannot audit its own approval decisions
```

Any attempt by a sub-agent to claim or execute permissions outside its assigned role constitutes a Level-1 Security Violation and triggers immediate system halt.

## 4. Handoff Workflows & Dual-Signoff Protocol

### Workflow 1: Standard Commercial Credit Decision
1. **Origination & Memo Draft (`maker`)**: `credit-analyst` validates financial inputs, runs ratio analysis, and submits a formalized Credit Memo with digital signature.
2. **Review & Determination (`checker`)**: `risk-officer` reviews the memo, evaluates risk grade, and records an affirmative Approval or Rejection.
3. **Audit Verification (`auditor`)**: `compliance-auditor` verifies adherence to policy guidelines, checks conflict separation, and writes the decision to the permanent audit ledger.

### Workflow 2: Policy Exception Escalation
For facilities exceeding standard leverage limits (Debt/EBITDA > 3.5x or DSCR between 1.15x and 1.24x):
- Requires unanimous concurrence from `maker`, `checker`, and `auditor`.
- Automated progression terminates; handoff package is dispatched to the human Designated Series 24 Supervisory Principal.

## 5. State & Credential Isolation
- **State Isolation**: `full`. Sub-agents maintain isolated working contexts and scratchpads. Inter-agent communication is conducted exclusively via structured handoff artifacts.
- **Credential Segregation**: `separate`. API keys and credentials for bureau reports, sanctions lookup, and audit writing are partitioned so that only the authorized agent can invoke corresponding capabilities.
