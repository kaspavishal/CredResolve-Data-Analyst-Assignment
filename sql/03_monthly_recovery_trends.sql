```sql
-- 03: Monthly Successful Payment Trends
-- Purpose: Summarize recorded successful payment events by month.
-- Warning: These amounts are not validated net recovery.

SELECT
    DATE_TRUNC('month', event_at) AS payment_month,
    COUNT(*) AS successful_payment_records,
    COUNT(DISTINCT payment_reference) AS distinct_nonnull_payment_references,
    ROUND(SUM(amount), 2) AS recorded_successful_amount
FROM payments
WHERE UPPER(TRIM(payment_status)) = 'SUCCESS'
GROUP BY 1
ORDER BY 1;
```