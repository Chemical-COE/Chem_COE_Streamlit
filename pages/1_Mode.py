import pandas as pd
import streamlit as st

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

st.title("Welcome to the Mode page!")

st.write("Here you can define a few options.")
st.write("Would you like to use the refrence tables we accesed in September of 2025?")
st.write("If so press the 'Default' Button Below.")

if st.button("Default"):
    st.session_state['mode'] = 'Default'
    
st.write("Or if would you like to upload your own reffrence tables, please click the 'Advanced' Button bellow")

if st.button("Advanced"):
    st.session_state['mode'] = 'Advanced'

st.info(f"You are currently in {st.session_state['mode']} mode.") ## I need to add this to the Results Page to make sure they are in the right mode.

if st.session_state['mode'] == 'Advanced':
    st.write("If you are uploading your own files, please make sure they have the same columns as used in the analysis:")
    st.write("An example can be found and downloaded below for both the ECHA table and SIN List table formatting")
    
    check_echa = 0
    check_sin = 0
    
    st.subheader("ECHA - Example")
    st.dataframe(echa_list.head(3))
    uploaded_echa = st.file_uploader("Upload your ECHA List file", type=["csv"])
    
    if uploaded_echa is not None:
        try:
            advanced_echa = pd.read_csv(uploaded_echa)
            st.session_state['echa_table'] = advanced_echa
            st.dataframe(advanced_echa.head(3))
            st.success("Double check that your ECHA List has the same columns as the above example.")
            check_echa = 1
        except:
            st.error("The ECHA List csv was not able to be read. Double check the file type.")
            check_echa = 0
    
    st.subheader("SIN List - Example")
    st.dataframe(sin_list.head(3))
    uploaded_sin = st.file_uploader("Upload your SIN List file", type=["csv"])
    
    if uploaded_sin is not None:
        try:
            advanced_sin = pd.read_csv(uploaded_sin)
            st.session_state['sin_table'] = advanced_sin
            st.dataframe(advanced_sin.head(3))
            st.success("Double check that your SIN List has the same columns as the above example.")
            check_sin = 1
        except:
            st.error("The SIN List csv was not able to be read. Double check the file type.")
            check_sin = 0
    
    if check_sin + check_echa == 2:
        st.success("Both files uploaded! You are ready to move on to the results page.")





