# Duties

System-wide segregation of duties policy for the sentinal-agent system.

## Roles

| Role | Agent | Permissions | Description |
|------|-------|-------------|-------------|
| Maker | sentinal-agent | create, submit | Ingests financials, calculates debt service ratios, and drafts credit underwriting memos |
| Checker | risk-officer | review, approve, reject | Independently verifies calculations, performs stress testing, approves or rejects credit |
| Auditor | compliance-auditor | audit, report | Audits completed evaluations for regulatory adherence, maintains immutable audit trails |

## Conflict Matrix

No single agent may hold conflicting roles in any pair:

### Conflict 1
- Role A: Maker
- Role B: Checker
- Constraint: The originator cannot approve its own proposals

### Conflict 2
- Role A: Maker
- Role B: Auditor
- Constraint: The originator cannot audit its own proposals

### Conflict 3
- Role A: Checker
- Role B: Auditor
- Constraint: The approver cannot audit its own determinations

## Handoff Workflows

### Commercial Credit Decision
1. **Maker** ingests financial statements, computes debt ratios, drafts memo, and submits
2. **Checker** independently verifies assumptions, stress tests, and renders decision
3. **Auditor** validates regulatory compliance and records immutable ledger entry
4. Approval required at each step before credit commitment

### Policy Exception Escalation
1. **Maker** identifies policy exception and documents compensating factors
2. **Checker** reviews and evaluates exception risk
3. **Auditor** audits proposed exception against regulatory guidelines
4. Requires unanimous concurrence across all three roles, plus final Series 24 Supervisory Principal signoff

## Isolation Policy

- **State isolation: full** — Each agent operates with its own memory and working state. No agent may read or modify another agent's working memory.
- **Credential segregation: separate** — Each role has its own distinct credential scope. Origination credentials cannot access review approval keys or audit logging tokens.

## Enforcement

Enforcement mode is **strict**. Any SOD violation will fail validation and block deployment.
