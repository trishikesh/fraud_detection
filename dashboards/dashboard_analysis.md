# Power BI Dashboard Analysis

## 1) Fraud Overview Dashboard

### Metrics
- Total transactions
- Total fraud
- Fraud rate
- Average fraud amount

### Visuals
- Fraud vs Legitimate distribution
- Fraud occurrence by hour

### Insights
- Fraud incidence is very low relative to total volume, requiring careful metric scaling.
- Even with a small fraud ratio, absolute fraud count remains operationally significant at scale.
- Fraud timing is not uniformly distributed; specific hours show concentration spikes.

## 2) Transaction Patterns Dashboard

### Visuals
- Fraud by transaction type
- Fraud amount distribution

### Insights
- Fraud is predominantly linked to transfer and cash-out pathways.
- Fraud amount distribution is right-skewed, showing that a subset of fraud events drives disproportionate monetary risk.
- Transaction-type segmentation improves prioritization for rule-based monitoring.

## 3) Risk Indicators Dashboard

### Visuals
- High-value fraud KPI
- Balance error fraud KPI
- Fraud transaction cluster scatter plot (amount vs balance error)

### Insights
- High-value transactions have elevated potential loss exposure and should receive stricter controls.
- Balance inconsistencies between expected and observed account balances are strong fraud indicators.
- Scatter clustering helps identify suspicious behavior pockets for downstream ML modeling and alerting rules.

## Portfolio Notes
- Keep dashboard filters consistent (date/hour/type) across pages for recruiter demos.
- Include tooltips with `isFraud`, `amount`, and error metrics to show analytical depth.
- Highlight business impact by pairing fraud count with estimated prevented loss.
