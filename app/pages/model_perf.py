import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏆 Model Performance")

data = pd.DataFrame({
    "Model": ["Naive", "RandomForest", "XGBoost"],
    "MAE": [87, 18, 16],
    "R2": [0.1, 0.85, 0.88]
})

st.subheader("📊 Model Comparison")
st.dataframe(data)

fig = px.bar(data, x="Model", y="MAE", title="MAE Comparison")
st.plotly_chart(fig)

fig2 = px.bar(data, x="Model", y="R2", title="R2 Score")
st.plotly_chart(fig2)