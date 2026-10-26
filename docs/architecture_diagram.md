# CredResolve — Data Pipeline Architecture

## Overview

The pipeline transforms raw operational data into trusted datasets, recovery metrics, and business recommendations.

```mermaid
flowchart LR
    A["Raw Data Sources<br/>Accounts, Borrowers, Payments,<br/>Calls, Agents, Campaigns"]
    B["Staging Layer<br/>Import CSVs<br/>Standardize formats and types"]
    C["Data Quality Validation<br/>Check unique keys<br/>Detect duplicate payments<br/>Resolve borrower identity conflicts<br/>Validate timestamps and missing values"]
    D["Clean Data<br/>Normalize dates<br/>Resolve or flag duplicates<br/>Reconcile payment records<br/>Standardize identifiers"]
    E["Golden Dataset<br/>Trusted account-level data<br/>Canonical borrower mapping<br/>Validated payment events"]
    F["Analytics and SQL<br/>Recovery metrics<br/>Risk and DPD segmentation<br/>Monthly trends<br/>Data quality reports"]
    G["Dashboard and Reporting<br/>Streamlit + Plotly<br/>Business insights<br/>Executive memo<br/>Investment recommendations"]

    H["Data Governance<br/>Validation Rules"]
    I["Logging and Audit Trail"]
    J["Payment Reconciliation<br/>Authoritative Sources"]
    K["Security and Access Control<br/>Protect Personal Data"]
    L["Monitoring and Refresh"]

    A --> B --> C --> D --> E --> F --> G

    B -.-> H
    C -.-> I
    D -.-> J
    E -.-> K
    F -.-> L
```

## Pipeline Responsibilities

1. **Raw data:** Preserve original source files for traceability.
2. **Staging:** Import data and standardize formats without losing source information.
3. **Validation:** Identify missing values, duplicate identifiers, conflicting borrower records, and timestamp problems.
4. **Clean data:** Normalize formats and reconcile records using documented rules.
5. **Golden dataset:** Maintain trusted, analysis-ready records with clearly defined keys.
6. **Analytics:** Calculate recovery metrics and analyze trends, risk segments, and delinquency.
7. **Reporting:** Present findings in the dashboard and executive memo.

## Important Controls

- Never assume a repeated payment reference proves a duplicate transaction.
- Do not join borrower records until identity conflicts have been resolved or explicitly handled.
- Preserve raw data and record every transformation.
- Calculate recovery rates using validated payment amounts and an appropriate outstanding-balance denominator.
- Clearly label incomplete reporting periods and unverified business claims.

## Current Evidence Limitation

The available payment data ends on August 8, 2026. The available evidence does not establish the claimed 11% month-on-month recovery improvement.