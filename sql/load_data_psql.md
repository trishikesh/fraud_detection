# Load Processed Data Into PostgreSQL (Windows)

## 1) Open PostgreSQL shell

Use either:
- pgAdmin Query Tool, or
- `psql` from terminal.

Example terminal command:

```bash
psql -U postgres
```

## 2) Switch to the target database

```sql
\c financial_fraud_analysis
```

If the database does not exist yet, create it first:

```sql
CREATE DATABASE financial_fraud_analysis;
\c financial_fraud_analysis
```

## 3) Create the table schema

Run:

```sql
\i sql/schema.sql
```

## 4) Load CSV using `\copy`

```sql
\copy transactions
FROM 'D:/NewData/IP_Projects/FinancialCrimeRiskAnalyser/fraud_detection/data/processed/clean_transactions.csv'
WITH (FORMAT csv, HEADER true)
```

## Why use `\copy` instead of `COPY`?

- `COPY` is executed by the PostgreSQL server process, so file paths must be accessible from the database server machine.
- `\copy` is executed by the client (`psql`) and reads files from your local Windows system.
- For local development on Windows, `\copy` avoids file-access permission and path-resolution issues.
