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

sin_count = len(sin_not_safe)
safe_count = len(sin_safe)

fig = px.bar(
    x=['Included in the SIN List', 'Not Included'],
    y=[sin_count, safe_count],
    title='SIN List Results',
    labels={'x': 'Category', 'y': 'Number of Chemicals'},
    color=['Included in the SIN List', 'Not Included'],
)

st.write('The chart below reflects the number of chemicals in your Chemical Information Sheet that are on the SIN List.')
st.plotly_chart(fig)


st.write('The next chart reflects how chemicals from your Chemical Information Sheet are distributed among the SIN List's SIN Groups.')
sin_results_not_safe = sin_not_safe.sort_values('sin_groups', ascending=True).copy()
fig = px.bar(sin_results_not_safe, x='sin_groups', hover_name = 'test_list_name', hover_data = ['cas_number', 'inclusion_date'], title = 'SIN Group Distribution')
st.plotly_chart(fig)

st.write('The final chart below reflects how chemicals from your Chemical Information Sheet are distributed among the SIN List's Health and Environmental Concerns.')
sin_results_not_safe = sin_results_not_safe.sort_values('health_env_concern', ascending=True)
fig = px.bar(sin_results_not_safe, x='health_env_concern', hover_name='test_list_name', hover_data = ['cas_number', 'inclusion_date'], title = 'Health and Environmental Concerns')
st.plotly_chart(fig)





