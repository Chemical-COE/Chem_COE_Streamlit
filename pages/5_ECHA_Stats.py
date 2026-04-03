import streamlit as st
import pandas as pd
import plotly.express as px

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

if 'result_sucsess' not in st.session_state:
    st.session_state['result_sucsess'] = 'No_result'

st.title("Welcome to the Statistics page!")
st.info("This Page is still in development.")
if st.session_state['result_sucsess'] == 'No_result':
   st.warning('Please complete your file upload before visiting the statistics page')
   st.stop()
  
if st.session_state['result_sucsess'] == 'result_passed':
  echa_safe = st.session_state['echa_s']
  echa_not_safe = st.session_state['echa_ns']
  sin_safe = st.session_state['sin_s']
  sin_not_safe = st.session_state['sin_ns']

echa_count = len(echa_not_safe)
echa_nr_count = len(echa_safe)

fig = px.bar(
    x=['Regulated by ECHA List', 'Not Regulated'],
    y=[echa_count, echa_nr_count],
    title='ECHA List Results',
    labels={'x': 'Category', 'y': 'Number of Chemicals'},
    color=['Regulated by ECHA List', 'Not Regulated'],
)

st.write('This reflects the number of chemicals in your test set that are and are Regulated by the ECHA List.')
st.plotly_chart(fig)

st.write('This reflects the distribution of the Chemical Universe groups in your test list.')
echa_results_not_safe = echa_not_safe.sort_values('position_in_the_chemical _universe', ascending=True).copy()
fig = px.bar(echa_results_not_safe, x='position_in_the_chemical _universe', hover_name = 'test_list_name', hover_data = [ 'cas_number', 'registration_type', 'infocard' ], title = 'ECHA Group Distribution')
st.plotly_chart(fig)

st.dataframe(echa_not_safef.loc[:, ['cas_number', 'test_list_name','infocard']])





