import streamlit as st
import sys, os

# Fix import path issue
sys.path.append(os.path.abspath("."))

st.set_page_config(layout="wide")

st.sidebar.title("📊 Retail Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Sales", "Forecasting", "ABC Analysis"]
)

# Routing
if page == "Overview":
    from app.pages.overview import app
    app()

elif page == "Sales":
    from app.pages.sales import app
    app()

elif page == "Forecasting":
    from app.pages.forecasting import app
    app()

elif page == "ABC Analysis":
    from app.pages.abc_analysis import app
    app()