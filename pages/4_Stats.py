import streamlit as st
import pandas as pd
import plotly.express as px

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

if 'result_sucsess' not in st.session_state:
    st.session_state['result_sucsess'] = 'No_result'

st.title("Welcome to the Statistics page")
st.info("This Page is still in development.")
if st.session_state['result_sucsess'] == 'No_result':
   st.warning('Please complete your file upload before visiting the statistics page')
   st.stop()
  
if st.session_state['result_sucsess'] == 'result_passed':
  echa_safe = st.session_state['echa_s']
  echa_not_safe = st.session_state['echa_ns']
  sin_safe = st.session_state['sin_s']
  sin_not_safe = st.session_state['sin_ns']

sin_count = len(sin_not_safe)
safe_count = len(sin_safe)

fig = px.bar(
    x=['Flagged by SIN List', 'Not Flagged'],
    y=[sin_count, safe_count],
    title='SIN List Results',
    labels={'x': 'Category', 'y': 'Number of Chemicals'},
    color=['Flagged by SIN List', 'Not Flagged'],
)
st.plotly_chart(fig)


