# Explainability Guide for Sentinal Agent

This document explains the reasoning architecture, operational inputs, and risk governance boundaries of the Sentinal Agent commercial underwriting ecosystem.

## How It Decides Credit Decisions and Risk Reasoning

The agent determines commercial creditworthiness through an empirical, multi-stage analytical evaluation. Financial statements are ingested and normalized to compute debt capacity metrics, primarily the Debt Service Coverage Ratio (DSCR) and Fixed Charge Coverage Ratio (FCCR). A transaction is classified as investment-grade when the base DSCR meets or exceeds 1.25x and debt leverage remains below 3.5x EBITDA. In addition, the system performs sensitivity stress testing by modeling a 200 basis point interest rate shock and a 15 percent revenue compression scenario. Quantitative risk scores and qualitative business factors are synthesized into an auditable credit recommendation before handoff to an independent officer for review.

## Inputs and Data Sources Used for Evaluation

The underwriting pipeline relies on structured borrower application data and independent external verification sources. Primary inputs include three years of historical balance sheets, verified profit and loss statements, and corporate federal tax filings. The system also ingests debt schedules and accounts receivable aging summaries to evaluate working capital velocity. For external verification, the agent accesses commercial bureau credit reports through the bureau reporting tool to confirm repayment history and UCC lien status. Real-time global sanctions and politically exposed persons (PEP) databases are queried through the sanctions screening tool to ensure full anti-money laundering compliance.

## Limitations, Operational Constraints, and Known Issues

The agent operates under strict institutional boundaries to eliminate autonomous underwriting risk. Automated credit commitment is constrained to facilities at or below $1,000,000; all requests exceeding this ceiling require human supervisory approval. A key operational constraint is that the agent cannot evaluate unaudited projections or speculative add-backs without verified documentary evidence. Furthermore, the underwriting originator is architecturally prohibited from approving its own credit recommendations, requiring independent adjudication on every transaction. Known issues include decreased analytical accuracy when processing non-standard financial statement formats without structured digital disclosures.
