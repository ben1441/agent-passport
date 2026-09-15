# Duties

System-wide segregation of duties policy for the sentinel-risk agent system.

## Roles

| Role | Agent | Permissions | Description |
|------|-------|-------------|-------------|
| Maker | sentinel-risk | create, submit | Ingests financials, calculates debt service ratios, and drafts credit underwriting memos |
| Checker | risk-officer | review, approve, reject | Independently verifies calculations, performs stress testing, approves or rejects credit |
| Auditor | compliance-auditor | audit, report | Audits completed evaluations for regulatory adherence, maintains immutable audit trails |

## Conflict Matrix

No single agent may hold both roles in any pair:

- **Maker <-> Checker** — The agent that produces credit memos cannot approve them
- **Maker <-> Auditor** — The agent that produces credit memos cannot audit them
- **Checker <-> Auditor** — The agent that approves credit determinations cannot audit the approval

## Handoff Workflows

### Commercial Credit Decision
1. **Maker** ingests financial statements, computes DSCR and leverage ratios, drafts credit memo, and submits for review
2. **Checker** independently verifies assumptions, performs sensitivity stress testing, and determines approval or decline
3. **Auditor** validates regulatory compliance and records an immutable ledger entry
4. Approval required at each step before credit commitment

### Policy Exception Escalation
1. **Maker** identifies policy exception and documents compensating factors
2. **Checker** reviews and evaluates exception risk
3. **Auditor** audits proposed exception against regulatory guidelines
4. Requires unanimous concurrence from Maker, Checker, and Auditor, plus final Series 24 Supervisory Principal signoff

## Isolation Policy

- **State isolation: full** — Each agent operates with its own memory and working state. No agent may read or modify another agent's working memory.
- **Credential segregation: separate** — Each role has its own distinct credential scope. The Maker's data intake credentials cannot access Checker approval keys or Auditor logging tokens.

## Enforcement

Enforcement mode is **strict**. Any SOD violation (e.g., assigning conflicting roles to the same agent) will fail validation and block deployment.
