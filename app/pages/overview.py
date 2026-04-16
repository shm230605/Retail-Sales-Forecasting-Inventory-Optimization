import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("📊 Overview Dashboard")

    st.markdown("### 🔹 Business Summary")

    # Sample data (replace with real later)
    total_sales = 120000
    total_orders = 3200
    avg_demand = 64
    stock_alerts = 15

    # 🔹 Vertical KPIs (one below another)
    st.metric("💰 Total Sales", f"₹{total_sales}")
    st.metric("🧾 Total Orders", total_orders)
    st.metric("📦 Avg Demand", f"{avg_demand} units")
    st.metric("⚠️ Stock Alerts", stock_alerts)

    st.markdown("---")

    # 🔹 Sales Trend (Vertical section)
    st.subheader("📈 Sales Trend")

    data = pd.DataFrame({
        "Day": range(1, 31),
        "Sales": np.random.randint(20, 100, 30)
    })

    st.line_chart(data.set_index("Day"))

    st.markdown("---")

    # 🔹 Recent Data Table
    st.subheader("📋 Recent Sales Data")

    st.dataframe(data.tail(10))