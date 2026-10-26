```sql
-- 04: Payment Activity by Risk Segment and DPD
-- Payments are linked to accounts using account_id.
-- Amounts represent recorded successful payments, not validated net recovery.

WITH account_payments AS (
    SELECT
        a.account_id,
        a.risk_segment,
        CASE
            WHEN a.dpd IS NULL THEN 'Unknown'
            WHEN a.dpd <= 30 THEN '0-30 days'
            WHEN a.dpd <= 60 THEN '31-60 days'
            WHEN a.dpd <= 90 THEN '61-90 days'
            ELSE '90+ days'
        END AS dpd_bucket,
        p.payment_id,
        p.amount,
        UPPER(TRIM(p.payment_status)) AS payment_status
    FROM read_csv_auto('data/processed/accounts.csv') a
    LEFT JOIN read_csv_auto('data/processed/payments.csv') p
        ON a.account_id = p.account_id
),
account_summary AS (
    SELECT
        risk_segment,
        dpd_bucket,
        COUNT(DISTINCT account_id) AS total_accounts,
        COUNT(DISTINCT CASE
            WHEN payment_status = 'SUCCESS' THEN account_id
        END) AS accounts_with_successful_payments,
        COUNT(DISTINCT CASE
            WHEN payment_status = 'SUCCESS' THEN payment_id
        END) AS unique_successful_payment_ids,
        ROUND(SUM(CASE
            WHEN payment_status = 'SUCCESS' THEN amount
            ELSE 0
        END), 2) AS recorded_successful_amount
    FROM account_payments
    GROUP BY risk_segment, dpd_bucket
)
SELECT *
FROM account_summary
ORDER BY risk_segment, dpd_bucket;
```