import pandas as pd
import streamlit as st

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

st.title("Welcome to the mode page")
st.write(f"You are currently in {st.session_state['mode']} mode.") ## I need to add this to the Results Page to make sure they are in the right mode.
st.write("Here you can define a few options.")
st.write("Would you like to use the refrence tables we accesed in September of 2025?")
st.write("If so press the 'Default' Button Below.")


if st.button("Default"):
    st.session_state['mode'] = 'Default'
    
st.write("Or if would you like to upload your own reffrence tables, please click the 'Advanced' Button bellow")
st.write(f"You are currently in {st.session_state['mode']} mode.") ## I need to add this to the Results Page to make sure they are in the right mode.
if st.button("Advanced"):
    st.session_state['mode'] = 'Advanced'

if st.session_state['mode'] == 'Advanced':
    st.write("If you are uploading your own files, please make sure they have the same columns as used in the analysis:")
    st.write("An example of that can be found below for the ECHA table and SIN List Table")
    st.dataframe(echa_list.head(3))
    st.dataframe(sin_list.head(3))
    





