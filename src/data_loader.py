import pandas as pd
from src.config import DATA_PATH
import os

def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"❌ File not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    if df.empty:
        raise ValueError("❌ CSV file is empty!")

    if "date" not in df.columns:
        raise ValueError("❌ 'date' column missing in dataset")

    df["date"] = pd.to_datetime(df["date"])

    return df