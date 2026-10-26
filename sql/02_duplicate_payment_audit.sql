```sql
-- 02: Duplicate Payment Audit
-- Objective: Investigate repeated payment IDs and inconsistent records.

CREATE OR REPLACE VIEW payments AS
SELECT *
FROM read_csv_auto('data/processed/payments.csv');

-- 1. Identify repeated payment IDs and record inconsistencies
SELECT
    payment_id,
    COUNT(*) AS record_count,
    COUNT(DISTINCT account_id) AS account_count,
    COUNT(DISTINCT borrower_id) AS borrower_count,
    COUNT(DISTINCT event_at) AS timestamp_count,
    COUNT(DISTINCT amount) AS amount_count,
    COUNT(DISTINCT UPPER(TRIM(payment_status))) AS status_count
FROM payments
WHERE payment_id IS NOT NULL
GROUP BY payment_id
HAVING COUNT(*) > 1
ORDER BY record_count DESC, payment_id;

-- 2. Inspect all records belonging to repeated payment IDs
WITH repeated_ids AS (
    SELECT payment_id
    FROM payments
    WHERE payment_id IS NOT NULL
    GROUP BY payment_id
    HAVING COUNT(*) > 1
)
SELECT p.*
FROM payments p
JOIN repeated_ids r
    ON p.payment_id = r.payment_id
ORDER BY p.payment_id, p.event_at;
```