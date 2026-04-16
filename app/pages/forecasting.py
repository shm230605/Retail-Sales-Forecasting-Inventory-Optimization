import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("🔮 Forecasting")

    st.success("Forecasting page is working!")

    # Dummy forecast data
    data = pd.DataFrame({
        "Day": range(1, 31),
        "Actual": np.random.randint(20, 100, 30),
        "Forecast": np.random.randint(30, 110, 30)
    })

    st.line_chart(data.set_index("Day"))