import streamlit as st
import pandas as pd

st.title("Welcome to the Statistics page")
if st.session_state['result_sucsess'] == 'No_result':
   st.warning('Please complete your file upload before visiting the statistics page')
   st.stop()
  
if st.session_state['result_sucsess'] == 'result_passed':
  echa_safe = st.session_state['echa_s']
  echa_not_safe = st.session_state['echa_ns']
  sin_safe = st.session_state['sin_s']
  sin_not_safe = st.session_state['sin_ns']


