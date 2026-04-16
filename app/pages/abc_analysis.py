import streamlit as st
import pandas as pd

def app():
    st.title("📦 ABC Analysis")

    st.success("ABC Analysis page is working!")

    df = pd.DataFrame({
        "Product": [f"P{i}" for i in range(1, 11)],
        "Revenue": [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
    })

    df["cum_pct"] = df["Revenue"].cumsum() / df["Revenue"].sum()

    st.dataframe(df)