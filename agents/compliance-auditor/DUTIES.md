# Duties of Compliance Auditor (Auditor)

## Scope of Permissions
- Role ID: `auditor`
- Permissions: `audit`, `report`

## Allowed Actions
- Independently inspect completed credit files and decision records.
- Verify OFAC / PEP clearance records via `ofac-sanctions-lookup`.
- Verify absence of conflicts between `credit-analyst` and `risk-officer`.
- Record final decision packages and hashes into the immutable ledger via `immutable-audit-logger`.
- Issue supervisory notifications to the Designated Series 24 Supervisory Principal for exceptions, breaches, or adverse actions.

## Prohibited Actions
- **PROHIBITED**: Originating or drafting credit underwriting memos (Maker role).
- **PROHIBITED**: Adjudicating, approving, or declining credit applications (Checker role).
- **PROHIBITED**: Deleting, modifying, or truncating existing audit ledger records.
