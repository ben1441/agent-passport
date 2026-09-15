---
name: aml-sanctions-screening
description: Verifies commercial borrowers and beneficial owners against OFAC SDN lists, Bank Secrecy Act (BSA) AML databases, and Politically Exposed Persons (PEP) watchlists.
license: Apache-2.0
---

# AML & Sanctions Screening Skill

## Overview
This skill performs mandatory Bank Secrecy Act (BSA), USA PATRIOT Act, and OFAC sanctions screening for all entities and individuals seeking commercial credit or participating in financial transactions.

## Screening Targets
1. **OFAC Specially Designated Nationals (SDN)**: Prohibited entities under US Treasury sanctions.
2. **Politically Exposed Persons (PEP)**: Heightened scrutiny on foreign or domestic senior political officials.
3. **FinCEN High-Risk Jurisdictions**: Cross-checks against FATF grey and blacklists.

## Mandatory Policy Rule
- A confirmed match on OFAC SDN results in **immediate transaction freeze** and mandatory escalation to the Bank Secrecy Act Officer (BSAO).
- Potential matches (>80% fuzzy name similarity) require secondary manual verification before credit processing can advance.
