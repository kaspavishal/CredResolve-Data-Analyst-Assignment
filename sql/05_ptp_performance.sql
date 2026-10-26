```sql
-- 05: Promise-to-Pay Performance
-- Purpose: Summarize promise outcomes by communication source.
-- Note: A kept promise is not independently verified payment recovery.

SELECT
    UPPER(TRIM(source)) AS communication_source,
    UPPER(TRIM(status)) AS ptp_status,
    COUNT(*) AS promise_count,
    ROUND(SUM(promised_amount), 2) AS total_promised_amount,
    ROUND(AVG(promised_amount), 2) AS average_promised_amount
FROM read_csv_auto('data/processed/promises_to_pay.csv')
GROUP BY
    UPPER(TRIM(source)),
    UPPER(TRIM(status))
ORDER BY communication_source, promise_count DESC;
```