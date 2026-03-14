import argparse
from pathlib import Path

import pandas as pd


def preprocess_transactions(input_csv: Path, output_csv: Path) -> pd.DataFrame:
    """Clean raw PaySim transactions and persist the processed dataset."""
    df = pd.read_csv(input_csv)

    # Convert simulation step into hour-of-day for temporal fraud analysis.
    df["hour"] = df["step"] % 24

    # One-hot encode transaction type columns used in SQL and dashboard layers.
    df = pd.get_dummies(df, columns=["type"])

    # Drop high-cardinality ID fields not required for aggregate analytics.
    df = df.drop(["nameOrig", "nameDest"], axis=1, errors="ignore")

    # Mark unusually large transactions as a simple risk indicator.
    df["high_value_transaction"] = (df["amount"] > 200000).astype(int)

    # Derive accounting consistency checks for source and destination accounts.
    df["balance_error_orig"] = (
        df["oldbalanceOrg"] - df["amount"] - df["newbalanceOrig"]
    )
    df["balance_error_dest"] = (
        df["oldbalanceDest"] + df["amount"] - df["newbalanceDest"]
    )

    df["isFraud"] = df["isFraud"].astype(int)
    df["isFlaggedFraud"] = df["isFlaggedFraud"].astype(int)

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Preprocess PaySim transaction data")
    parser.add_argument(
        "--input",
        default="data/raw/raw_transactions.csv",
        help="Path to raw transaction CSV",
    )
    parser.add_argument(
        "--output",
        default="data/processed/clean_transactions.csv",
        help="Path to write cleaned transaction CSV",
    )
    args = parser.parse_args()

    cleaned = preprocess_transactions(Path(args.input), Path(args.output))
    print("Rows:", len(cleaned))
    print("Fraud label distribution:\n", cleaned["isFraud"].value_counts())
    print(f"Clean dataset saved to: {args.output}")


if __name__ == "__main__":
    main()
