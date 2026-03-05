import streamlit as st
import pandas as pd

st.title("Welcome to the Upload page!")

st.write("To enter your test list use the button bellow.")
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
