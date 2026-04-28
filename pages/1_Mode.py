import pandas as pd
import streamlit as st

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

st.title("Welcome to the Mode page!")

st.write("Here you can choose the reference sheet(s) to which the chemicals in your Chemical Information Sheet will be compared.")
st.write("The comparison will allow you to see if the chemicals you are using are included in the SIN List* or restricted under the EU's REACH Regulation**.")

st.write("The 'Default' mode uses reference sheets based on the SIN List and the REACH registered substance list from September of 2025.")
st.write("Click the 'Default' button below if you would like to choose this option.")

if st.button("Default"):
    st.session_state['mode'] = 'Default'
    
st.write("Alternatively, if you would like to upload reference sheets that contain more recent data from the SIN List and REACH please click the 'Advanced' button below.")
st.write("After clicking on the 'Advanced' Button, scroll down to see example reference sheets for REACH and the SIN List.")
st.write("Note that if you plan to use the advanced option your uploaded reference sheets must be in the same format and contain all the same column headers as what is shown in the example reference sheets.")

if st.button("Advanced"):
    st.session_state['mode'] = 'Advanced'

st.info(f"You are currently in {st.session_state['mode']} mode.") ## I need to add this to the Results Page to make sure they are in the right mode.

st.write("")
st.write("")
st.write("")
st.write("")

#st.warning("Important Information Below")

st.write("*Please see The International Chemical Secretariat’s (ChemSec) website for more on the SINList.")
st.link_button("Go to ChemSec", "https://sinlist.chemsec.org")

st.write("**If visiting the European Chemicals Agency’s (ECHA) website through a link from this app, please see the agency’s legal notice.")
st.link_button('Go to ECHA Legal Notice', 'http://echa.europa.eu/web/guest/legal-notice')
st.write("**We acknowledge that the source of REACH data used in this app is from ECHA.")
st.link_button("Go to ECHA Website", "http://echa.europa.eu/")
st.link_button("This page is also useful in understanding ECHA’s chemical universe", "https://echa.europa.eu/sl/universe-of-registered-substances")

if st.session_state['mode'] == 'Advanced':
    st.write("If you are uploading your own files, please make sure they have the same columns as used in the analysis:")
    st.write("An example can be found and downloaded below for both the REACH table and SIN List table formatting")
    
    check_echa = 0
    check_sin = 0
    
    st.subheader("ECHA - Example")
    st.dataframe(echa_list.head(3))
    uploaded_echa = st.file_uploader("Upload your REACH List file", type=["csv"])
    st.link_button("Download REACH List here", "https://echa.europa.eu/sl/universe-of-registered-substances")
    if uploaded_echa is not None:
        try:
            advanced_echa = pd.read_csv(uploaded_echa)
            st.session_state['echa_table'] = advanced_echa
            st.dataframe(advanced_echa.head(3))
            st.success("Double check that your REACH List has the same columns as the above example.")
            check_echa = 1
        except:
            st.error("The REACH List csv was not able to be read. Double check the file type.")
            check_echa = 0
        
        
        
    st.subheader("SIN List - Example")
    st.dataframe(sin_list.head(3))
    uploaded_sin = st.file_uploader("Upload your SIN List file", type=["csv"])
    st.link_button("Download SIN List here", "https://sinsearch.chemsec.org/")
    st.warning("You will be prompted to create an account / log in. You will need to navigate to the 'Search the Sin List' option to download the list as an excel file.")
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





