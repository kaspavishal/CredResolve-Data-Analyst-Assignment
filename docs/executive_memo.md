# CredResolve — Executive Memo
## Recovery Performance, Data Reliability, and Investment Recommendation

### 1. Executive Summary

The available evidence does not establish the claim that recovery improved by 11% month-on-month. Payment events cover January 1 through August 8, 2026, rather than 12 complete months. August is incomplete, and transaction-reference and borrower-identity issues require resolution before the trend can be considered reliable.

The processed payment dataset contains nine columns, including `payment_id`, `account_id`, and `borrower_id`. These fields provide a basis for account-level attribution, but their presence alone does not establish that every transaction is valid, unique, correctly attributed, or financially settled.

**Recommendation:** Validate recovery metrics, reconcile transactions, and conduct controlled recovery experiments before committing the full ₹10 crore investment.

### 2. Key Findings

- **Payment records:** The current analysis contains 25,014 payment rows and 25,000 distinct payment IDs. Fourteen payment IDs are repeated and require investigation. These records should not automatically be treated as confirmed duplicate financial transactions.
- **Borrower identity:** The borrower dataset contains 30,000 rows but only 11,015 unique borrower IDs. Conflicting identity attributes require investigation before borrower-level aggregation.
- **Payment references:** The reference audit identified 3,407 repeated references associated with multiple payment IDs, accounts, and amounts. A repeated reference alone does not prove a duplicate payment.
- **Recovery trend:** Recorded successful-payment amounts fluctuate over the available period. The data does not cover 12 complete months, so the headline claim cannot be verified.
- **Promise-to-pay performance:** The dataset contains 18,000 promises. Recorded kept-promise rates are 23.80% for CALL, 24.68% for FIELD, 24.05% for SMS, and 25.60% for WHATSAPP. These are descriptive promise outcomes, not verified cash-recovery rates or causal evidence that one channel performs better.
- **Portfolio exposure:** Outstanding balances exist across risk and days-past-due (DPD) segments. Account-level payment activity can be analyzed using the account identifier, but payment reconciliation and the recovery-rate denominator must be validated before interpreting this as verified recovery performance.

### 3. Business Risks

1. **Metric inflation:** Conflicting borrower identifiers can multiply records during joins and overstate payment counts or amounts.
2. **Transaction ambiguity:** Repeated payment references and payment-ID anomalies require reconciliation against an authoritative transaction ledger.
3. **Misleading comparisons:** Incomplete periods and portfolio-mix changes can distort month-on-month trends.
4. **Unverified recovery attribution:** Recorded successful payments must be reconciled with reversals, duplicate events, and a valid account-level outstanding-balance denominator.
5. **Channel-selection bias:** Differences in kept-promise rates may reflect borrower selection, campaign differences, or operational factors rather than a causal channel effect.

### 4. Proposed ₹10 Crore Investment Plan

**Important:** This is a provisional planning allocation, not a validated ROI forecast or a guarantee of financial returns.

| Workstream | Proposed Allocation | Purpose |
|---|---:|---|
| Data quality and payment reconciliation | ₹1.0 Cr | Resolve identity, transaction, timestamp, and attribution issues |
| Controlled recovery experiments | ₹1.5 Cr | Test targeting, contact timing, and channel strategies |
| Scaled recovery operations | ₹4.0 Cr | Expand only interventions demonstrating incremental net recovery |
| Analytics and decision-support capability | ₹1.5 Cr | Build trusted metrics, monitoring, and operational dashboards |
| Agent and channel optimization | ₹1.0 Cr | Evaluate agent productivity and channel conversion |
| Contingency, compliance, and evaluation | ₹1.0 Cr | Cover implementation uncertainty and independent measurement |
| **TOTAL** | **₹10.0 Cr** | |

Release the proposed scaling budget in stages. Revise the allocation when actual intervention costs and incremental recovery estimates become available. Do not commit the entire amount to scaled operations before experimental evidence supports expansion.

### 5. Measurement and Investment Gates

Before scaling any intervention:

- Define the recovery rate using a validated recovery numerator and eligible outstanding-balance denominator.
- Reconcile successful transactions against reversals and duplicate events.
- Validate payment-to-account attribution and investigate repeated payment IDs and references.
- Compare treatment and control groups over the same observation window.
- Measure incremental net recovery, cost per incremental rupee recovered, and customer or compliance risks.
- Evaluate statistical uncertainty and operational significance before expanding an intervention.

**ROI Formula**

ROI = (Incremental net recovery − Incremental intervention cost) / Incremental intervention cost

**Break-Even Condition**

Incremental net recovery must equal or exceed incremental intervention cost for the intervention to break even under this definition.

**Strict financial reporting rule:** Do not report a numerical ROI, guaranteed uplift, or proven investment return until the necessary inputs have been measured and validated.

### 6. Limitations

The available evidence does not establish a definitive 11% month-on-month improvement, a causal explanation for recovery changes, or a guaranteed return on the proposed investment. Although the processed payment dataset contains account and payment identifiers, transaction integrity, attribution, reversals, and the appropriate recovery denominator still require validation.

The proposed ₹10 crore allocation is a planning hypothesis rather than a validated financial forecast. Recorded successful-payment amounts should not be treated as verified net recovery without reconciliation.

### 7. Immediate Next Steps

1. Reconcile payment IDs and references against an authoritative transaction ledger.
2. Resolve borrower identity conflicts and define canonical borrower records.
3. Validate the account-level payment dataset and outstanding-balance denominator.
4. Recalculate monthly recovery metrics over comparable, complete periods.
5. Run controlled experiments and report measured incremental recovery before scaling expenditure.

---

### Final Conclusion

The 11% recovery-improvement claim remains unverified. Prioritize data reliability, validate recovery metrics, and use controlled experiments to guide the proposed ₹10 crore investment.