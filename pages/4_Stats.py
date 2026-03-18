import streamlit as st
import pandas as pd

st.title("Welcome to the Statistics page")

echa_safe = st.session_state['echa_s']
echa_not_safe = st.session_state['echa_ns']
sin_safe = st.session_state['sin_s']
sin_not_safe = st.session_state['sin_ns']

