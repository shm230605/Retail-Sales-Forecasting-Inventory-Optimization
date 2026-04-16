import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("📈 Sales Analysis")

    st.success("Sales page is working!")

    # Dummy data (so it NEVER shows blank)
    data = pd.DataFrame({
        "Day": range(1, 31),
        "Sales": np.random.randint(20, 100, 30)
    })

    st.line_chart(data.set_index("Day"))

    st.dataframe(data.tail())