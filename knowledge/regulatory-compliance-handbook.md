# Regulatory Compliance & Supervisory Handbook

## 1. FINRA Rule 3110 (Supervision)
- Each autonomous agent participating in investment, underwriting, or credit execution must be associated with a designated registered supervisory principal (Series 24).
- Periodic supervisory sampling must be conducted quarterly.
- An instantaneous kill switch must be maintained by the supervisory principal to halt autonomous operations in the event of system anomaly or market disruption.

## 2. FINRA Rule 4511 & SEC Rule 17a-4 (Books and Records)
- All electronic communications, inputs, model outputs, tool calls, and supervisory determinations must be preserved in structured JSON format for an immutable retention period of not less than **6 years**.
- The first 2 years must be maintained in an easily accessible place.
- Records must be write-once-read-many (WORM) compliant and protected against alteration.

## 3. Federal Reserve SR 11-7 (Model Risk Management)
- **Conceptual Soundness**: The theoretical basis, mathematical logic, and data sources underlying the automated underwriting models must be documented and tested annually.
- **Ongoing Monitoring & Outcomes Analysis**: Back-testing against realized default outcomes and continuous monitoring for covariate and concept drift.
- **Independent Validation**: Model code, feature selection, and decision thresholds must be independently audited by a third party with no commercial conflict.

## 4. Equal Credit Opportunity Act (ECOA) & CFPB Reg B
- Prohibition against discrimination based on race, color, religion, national origin, sex, marital status, or age.
- Mandatory delivery of adverse action notices within 30 days of application completion detailing principal reasons for any denial.
