import streamlit as st
import pandas as pd

st.title("Welcome to the Upload page!")

st.write("To enter your test list use the button bellow.")
uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])

if uploaded_file is not None:
    try:
        uploaded_csv = pd.read_csv(uploaded_file)
        st.session_state['chemical_data'] = uploaded_csv
    
        st.dataframe(uploaded_csv[['name', 'cas_number']])
        st.success("Data saved! You can now navigate to the results page.")

    except:
        st.error("The csv was not able to be read. Double check the column names.")
