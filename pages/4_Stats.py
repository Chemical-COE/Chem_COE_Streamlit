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
    x=['Flagged by SIN List', 'Not Flagged'],
    y=[sin_count, safe_count],
    title='SIN List Results',
    labels={'x': 'Category', 'y': 'Number of Chemicals'},
    color=['Flagged by SIN List', 'Not Flagged'],
)

st.write('This reflects the number of chemicals in your test set that are and are not on the SIN List.')
st.plotly_chart(fig)


st.write('This reflects the distribution of the SIN Groups in your test list.')
sin_results_not_safe = sin_not_safe.sort_values('sin_groups', ascending=True).copy()
fig = px.bar(sin_results_not_safe, x='sin_groups', hover_name = 'test_list_name', hover_data = ['cas_number', 'inclusion_date'], title = 'SIN Group Distribution')
st.plotly_chart(fig)

st.write('This reflects the distribution of Environmental Concerns in your test list.')
sin_results_not_safe = sin_results_not_safe.sort_values('health_env_concern', ascending=True)
fig = px.bar(sin_results_not_safe, x='health_env_concern', hover_name='test_list_name', hover_data = ['cas_number', 'inclusion_date'], title = 'Health Envirronmental Concerns')
st.plotly_chart(fig)





