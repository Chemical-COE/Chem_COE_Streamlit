import streamlit as st
import pandas as pd

st.title("Hi there! Welcome to the Results page!")

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

l = 0

if 'chemical_data' in st.session_state:
    df = st.session_state['chemical_data']
    st.dataframe(df[['name','cas_number']])
    l = 1

else:
    st.warning("Please upload your data on the upload page first.")


