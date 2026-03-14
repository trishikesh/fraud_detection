import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraud Detection Risk App", layout="wide")
st.title("Financial Fraud Risk Analyzer")
st.caption("Future-ready interface for model-based fraud scoring")

st.markdown(
    """
This Streamlit app is a starter scaffold for the next phase of the project:
- Load incoming transaction records
- Engineer model features
- Run fraud probability prediction
- Display explainability and risk flags
"""
)

sample_path = "data/processed/clean_transactions.csv"

try:
    df = pd.read_csv(sample_path)
    st.subheader("Sample Processed Transactions")
    st.dataframe(df.head(20), use_container_width=True)
except FileNotFoundError:
    st.warning("Processed dataset not found. Run python/preprocessing.py first.")

st.subheader("Planned Model Inputs")
st.code(
    """{
  "amount": 125000.0,
  "hour": 18,
  "type_TRANSFER": 1,
  "type_CASH_OUT": 0,
  "balance_error_orig": 50000.0,
  "balance_error_dest": 10000.0
}""",
    language="json",
)

st.info("Model inference pipeline will be integrated in a future update.")
