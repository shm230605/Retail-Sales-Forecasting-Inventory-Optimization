import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

if page == "Page 1":
    st.title("Page 1 Works")

elif page == "Page 2":
    st.title("Page 2 Works")