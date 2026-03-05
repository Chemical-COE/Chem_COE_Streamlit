import streamlit as st
import pandas as pd

st.title("Welcome to the Chemical Code of Ethics!")
st.write("Our goal is to let you manage your own chemicals")
st.write("To begin, download the Test Sheet and fill in your CAS Numbers and Chemical Names.")

test_list = pd.DataFrame(columns=['name', 'cas_number'])
csv = test_list.to_csv(index=False)

st.download_button(
    label="Download Test Sheet",
    data=csv,
    file_name="test_list.csv",
    mime="text/csv"
)

st.write("After filling out your sheet please the side bar to navigate to the 'Upload' page.")
