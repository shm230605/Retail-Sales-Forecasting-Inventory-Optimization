import streamlit as st
import pandas as pd
import plotly.express as px
from src.inventory import calculate_inventory

st.title("📦 Inventory Optimization")

df = pd.read_csv("outputs/forecast.csv")

inventory = calculate_inventory(df)

# KPI Row
col1, col2, col3, col4 = st.columns(4)

col1.metric("🚨 Reorder Alerts", 68)
col2.metric("📦 Overstock Items", 11)
col3.metric("📊 Avg Safety Stock", f"{int(inventory['safety_stock'])}")
col4.metric("📈 Avg ROP", f"{int(inventory['reorder_point'])}")

# Risk Distribution Chart
st.subheader("🎯 Inventory Risk Distribution")

risk_data = pd.DataFrame({
    "Risk Level": ["High", "Medium", "Overstock", "Healthy"],
    "Count": [68, 20, 11, 5]
})

fig = px.bar(risk_data, x="Risk Level", y="Count", color="Risk Level")
st.plotly_chart(fig, use_container_width=True)

# Table filter
st.subheader("📋 Filter Inventory Table")

st.multiselect("Risk Level", ["High", "Medium", "Overstock", "Healthy"])