# Fraud Analysis Query Explanations

This document explains what each SQL query in `fraud_analysis_queries.sql` does, why it matters, and how it supports Power BI reporting.

## 1) Total transaction volume
- What it does: Counts all records in `transactions`.
- Why it matters: Establishes baseline scale and denominator for all fraud rates.
- Dashboard impact: Feeds the `Total Transactions` KPI card in Fraud Overview.

## 2) Total fraud cases
- What it does: Counts rows where `isFraud = 1`.
- Why it matters: Quantifies direct fraud incidence.
- Dashboard impact: Feeds `Total Fraud` KPI and trend comparisons.

## 3) Overall fraud rate (%)
- What it does: Computes fraud share as a percentage of all transactions.
- Why it matters: Normalizes risk regardless of total transaction volume.
- Dashboard impact: Feeds `Fraud Rate` KPI for executive reporting.

## 4) Fraud trend by hour of day
- What it does: Groups fraud events by `hour` and returns the count per hour.
- Why it matters: Detects temporal concentration windows useful for controls and monitoring.
- Dashboard impact: Supports hourly fraud line/bar chart in Fraud Overview.

## 5) High-value fraud transactions
- What it does: Counts fraud events flagged as `high_value_transaction = TRUE`.
- Why it matters: High-value fraud often has larger financial impact and urgency.
- Dashboard impact: Feeds High-Value Fraud KPI in Risk Indicators.

## 6) Fraud concentration by transfer-oriented types
- What it does: Separately counts fraud where transaction flags indicate `TRANSFER` or `CASH_OUT`.
- Why it matters: PaySim fraud is commonly concentrated in these outbound channels.
- Dashboard impact: Powers transaction-type comparison visuals in Transaction Patterns.

## 7) Average amount by class
- What it does: Compares average `amount` for fraud vs legitimate transactions.
- Why it matters: Highlights value behavior differences between fraud and normal activity.
- Dashboard impact: Supports distribution context and summary cards.

## 8) Balance anomaly fraud signal
- What it does: Counts fraud rows with non-trivial origin or destination balance mismatches.
- Why it matters: Accounting inconsistencies are strong risk indicators for synthetic events.
- Dashboard impact: Feeds Balance Error KPI in Risk Indicators.

## 9) Fraud by one-hot transaction flags
- What it does: Produces fraud counts for each transaction type from one-hot encoded columns.
- Why it matters: Creates a ranked view of where fraud is concentrated.
- Dashboard impact: Drives the `Fraud by Transaction Type` chart in Transaction Patterns.
