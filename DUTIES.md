# Duties

System-wide segregation of duties policy for the sentinel-risk agent system.

## Roles

| Role | Agent | Permissions | Description |
|------|-------|-------------|-------------|
| maker | sentinel-risk | create, submit | Analyzes financials, calculates debt service ratios, and drafts credit underwriting memos |
| checker | risk-officer | review, approve, reject | Independently verifies calculations, performs stress testing, approves or rejects credit |
| auditor | compliance-auditor | audit, report | Audits completed evaluations for regulatory adherence, maintains immutable audit trails |

## Conflict Matrix

No single agent may hold both roles in any pair:

- **maker <-> checker** — The maker (sentinel-risk) cannot approve its own credit proposals
- **maker <-> auditor** — The maker (sentinel-risk) cannot audit its own underwriting work
- **checker <-> auditor** — The checker (risk-officer) cannot audit its own approval determinations

## Handoff Workflows

### Commercial Credit Decision
1. **maker** (`sentinel-risk`) ingests financial statements, computes DSCR/leverage ratios, drafts credit memo, and submits for review
2. **checker** (`risk-officer`) independently verifies assumptions, performs sensitivity stress testing, and determines approval or decline
3. **auditor** (`compliance-auditor`) validates regulatory compliance (FINRA 3110/4511, Fed SR 11-7) and records an immutable ledger entry
4. Approval required at each step before credit commitment

### Policy Exception Escalation
1. **maker** (`sentinel-risk`) identifies policy exception (e.g. leverage > 3.5x or DSCR 1.15x-1.24x) and documents compensating factors
2. **checker** (`risk-officer`) reviews and evaluates exception risk
3. **auditor** (`compliance-auditor`) audits proposed exception against regulatory guidelines
4. Requires unanimous concurrence from maker, checker, and auditor, plus final Series 24 Supervisory Principal signoff

## Isolation Policy

- **State isolation: full** — Each agent operates with its own memory and working state. No agent may read or modify another agent's working memory.
- **Credential segregation: separate** — Each role has its own distinct credential scope. The maker's data intake credentials cannot access checker approval keys or auditor logging tokens.

## Enforcement

Enforcement mode is **strict**. Any SOD violation (e.g., assigning conflicting roles to the same agent) will fail validation and block deployment.
