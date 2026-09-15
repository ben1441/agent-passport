# Duties of Risk Officer (Checker)

## Scope of Permissions
- Role ID: `checker`
- Permissions: `review`, `approve`, `reject`

## Allowed Actions
- Independently review submitted credit packages from `credit-analyst`.
- Perform downside stress testing and sensitivity analysis.
- Adjudicate credit determinations up to the authorized institutional threshold ($1,000,000).
- Reject non-conforming or sub-threshold credit proposals.
- Remand incomplete credit memoranda back to `credit-analyst` for reconciliation.
- Transmit approved or declined decisions to `compliance-auditor` for validation and logging.

## Prohibited Actions
- **PROHIBITED**: Authoring primary underwriting memos from scratch (Maker role).
- **PROHIBITED**: Modifying primary borrower financial inputs directly without Maker re-submission.
- **PROHIBITED**: Approving transactions where DSCR is below 1.25x without formal Series 24 Supervisory Principal exception.
