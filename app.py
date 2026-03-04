import streamlit as st
import pandas as pd

st.title("Hi there! Welcome to Streamlit!")
st.write("My first DataFrame")
st.dataframe(
    pd.DataFrame({
        'A': [1, 5, 9, 7],
        'B': [3, 2, 4, 8]
    })
)
