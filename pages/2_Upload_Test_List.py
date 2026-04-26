import streamlit as st
import pandas as pd

st.title("Welcome to the Upload page!")

st.write("Please upload your Chemical Information Sheet in csv format by clicking on the button below.")
uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])

if uploaded_file is not None:
    try:
        uploaded_csv = pd.read_csv(uploaded_file)
        uploaded_csv['name'] = uploaded_csv['name'].fillna(uploaded_csv['cas_number']) 
        st.session_state['chemical_data'] = uploaded_csv
    
        st.dataframe(uploaded_csv[['name', 'cas_number']])
        st.success("Data saved! You can now navigate to the results page.")

    except:
        st.error("The csv was not able to be read. Double check the column names.")
