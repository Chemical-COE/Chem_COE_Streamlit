import streamlit as st
import pandas as pd

st.title("Welcome to the Chemical Code of Ethics App!")
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


name = ["Acetone", "Benzene", "Toluene", "Ethanol",]
cas_number = ["67-64-1", "71-43-2", "108-88-3", "64-17-5"]
test_list = pd.DataFrame({'name': name, 'cas_number': cas_number})
st.write("After filling out your sheet please the side bar to navigate to the 'Upload' page.")
st.write('Your sheet should look similar to the table below. Make sure to retain the original column names.')
st.write('You can even choose to download this table as a csv by hovering over the table with your mouse and selecting the download icon.')
st.dataframe(test_list)




