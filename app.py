import streamlit as st
import pandas as pd

st.title("Welcome to the Chemical Code of Ethics App!")
st.write("This app was designed to help companies better understand hazards that might be associated withchemicals that are used in their products.")
st.write("App creators do not see or store any of your data.")
st.write("To begin, download the blank Chemical Information Sheet and fill in your CAS Registry Numbers and chemical names.")
st.write("(The CAS Registry Numbers are the essential pieces of information needed by the app; the app understands that a single CAS Registry Number maybe associated with multiple chemical names.) We recommend opening the file in Excel or Google Sheets.")
st.write('Your Chemical Information sheet should look similar to the table below. Make sure to retain the original column headings (i.e., "name" and "cas_number".).')

test_list = pd.DataFrame(columns=['name', 'cas_number'])
csv = test_list.to_csv(index=False)
st.subheader('Please note: The app will only read your Chemical Information Sheet if it is saved as a csv file')
st.download_button(
    label="Download a Blank Sheet",
    data=csv,
    file_name="test_list.csv",
    mime="text/csv"
)

name = ["Acetone", "Benzene", "Toluene", "Ethanol",]
cas_number = ["67-64-1", "71-43-2", "108-88-3", "64-17-5"]
test_list = pd.DataFrame({'name': name, 'cas_number': cas_number})

st.write("After filling out and saving your Chemical Information Sheet please use the sidebar to navigate to the 'Mode' page.")

st.write('An alternative approach to downloading the Chemical Information Sheet as a csv file is by hovering over the example table below and selecting the download icon that appears in the upper right corner of the example table.')
st.write('Simply change the data in that table to reflect the chemicals you are using, being sure to retain the original column headings. We reccomend using Excel or Google Sheets and your sheet must be saved as a csv file.')
st.dataframe(test_list)




