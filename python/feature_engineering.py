from pathlib import Path

import numpy as np
import pandas as pd


def build_model_features(input_csv: str, output_csv: str) -> pd.DataFrame:
    """Create model-oriented features from the cleaned transaction dataset."""
    df = pd.read_csv(input_csv)

    df["amount_log1p"] = np.log1p(df["amount"].clip(lower=0))
    df["orig_account_emptied"] = (df["newbalanceOrig"] == 0).astype(int)
    df["dest_account_increase"] = (df["newbalanceDest"] > df["oldbalanceDest"]).astype(int)
    df["abs_balance_error_orig"] = df["balance_error_orig"].abs()
    df["abs_balance_error_dest"] = df["balance_error_dest"].abs()

    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    return df


if __name__ == "__main__":
    source = "data/processed/clean_transactions.csv"
    target = "data/processed/feature_enriched_transactions.csv"
    features = build_model_features(source, target)
    print(f"Feature engineering complete. Output rows: {len(features)}")
    print(f"Saved feature dataset to: {target}")
