import streamlit as st
import pandas as pd

st.title("Welcome to the Upload page!")

st.write("Here you can define a few options.")
st.write("Would you like to use the refrence tables we accesed in September of 2025?")
st.write("If so press the 'Default' Button Below.")
    
if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

if st.button("Default"):
    st.session_state['mode'] = 'Default'
    
st.write("Or if would you like to upload your own refrence tables, please click the 'Advanced' Button Bellow")
if st.button("Advanced"):
    st.session_state['mode'] = 'Advanced'
    
st.write(f"You are currently in {st.session_state['mode']} mode.")
st.write("If you are uploading your own files, please make sure they have the same columns as used in the analysis:")


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
