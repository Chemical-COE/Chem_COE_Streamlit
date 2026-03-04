import streamlit as st
import pandas as pd

st.title("Hi there! Welcome to Streamlit!")
st.write("My first DataFrame... it's about fish")
st.dataframe(
    pd.DataFrame({
        'Fish': ['Honey Gourami', 'Black Neon Tetra', 'Pygmy Corydora', 'Cherry Shrimp'],
        'Plants': ['Red Floater', 'Cryptocoryne', 'Monte Carlo', 'Annubias']
    })
)


st.write('More importantly... here is a explore my two fish pages')
