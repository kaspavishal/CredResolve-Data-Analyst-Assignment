```sql
-- 01: Payment Status Analysis
-- Objective: Examine payment outcomes and amounts.

SELECT
    payment_status,
    COUNT(*) AS payment_count,
    ROUND(SUM(amount), 2) AS total_amount
FROM payments
GROUP BY payment_status
ORDER BY payment_count DESC;
```