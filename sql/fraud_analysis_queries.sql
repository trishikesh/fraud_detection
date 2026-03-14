-- 1) Total transaction volume
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- 2) Total fraud cases
SELECT COUNT(*) AS total_fraud_cases
FROM transactions
WHERE isFraud = 1;

-- 3) Overall fraud rate (%)
SELECT
    COUNT(*) FILTER (WHERE isFraud = 1) * 100.0 / COUNT(*) AS fraud_rate_percent
FROM transactions;

-- 4) Fraud trend by hour of day
SELECT
    hour,
    COUNT(*) AS fraud_transactions
FROM transactions
WHERE isFraud = 1
GROUP BY hour
ORDER BY hour;

-- 5) High-value fraud transactions
SELECT COUNT(*) AS high_value_fraud_count
FROM transactions
WHERE high_value_transaction = TRUE
  AND isFraud = 1;

-- 6) Fraud concentration by transfer-oriented transaction types
SELECT
    SUM(CASE WHEN type_TRANSFER THEN 1 ELSE 0 END) AS transfer_fraud,
    SUM(CASE WHEN type_CASH_OUT THEN 1 ELSE 0 END) AS cashout_fraud
FROM transactions
WHERE isFraud = 1;

-- 7) Average amount comparison: fraud vs legitimate
SELECT
    CASE WHEN isFraud = 1 THEN 'Fraud' ELSE 'Legitimate' END AS transaction_class,
    AVG(amount) AS avg_amount
FROM transactions
GROUP BY isFraud
ORDER BY transaction_class;

-- 8) Balance anomaly fraud signal
SELECT
    COUNT(*) AS anomalous_balance_fraud_count
FROM transactions
WHERE isFraud = 1
  AND (
      ABS(balance_error_orig) > 1
      OR ABS(balance_error_dest) > 1
  );

-- 9) Fraud by transaction type one-hot flags
SELECT 'CASH_OUT' AS transaction_type, COUNT(*) AS fraud_count
FROM transactions
WHERE isFraud = 1 AND type_CASH_OUT = TRUE
UNION ALL
SELECT 'TRANSFER', COUNT(*)
FROM transactions
WHERE isFraud = 1 AND type_TRANSFER = TRUE
UNION ALL
SELECT 'PAYMENT', COUNT(*)
FROM transactions
WHERE isFraud = 1 AND type_PAYMENT = TRUE
UNION ALL
SELECT 'DEBIT', COUNT(*)
FROM transactions
WHERE isFraud = 1 AND type_DEBIT = TRUE
UNION ALL
SELECT 'CASH_IN', COUNT(*)
FROM transactions
WHERE isFraud = 1 AND type_CASH_IN = TRUE
ORDER BY fraud_count DESC;
