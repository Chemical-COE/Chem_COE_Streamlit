import streamlit as st
import pandas as pd

st.title("Hi there! Welcome to the Results page!")

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

if 'chemical_data' in st.session_state:
    df = st.session_state['chemical_data']
    st.dataframe(df)

else:
    st.warning("Please upload your data on the upload page first.")
