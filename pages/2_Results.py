import streamlit as st
import pandas as pd

st.title("Welcome to the Results page!")

sin_list = pd.read_excel('SinList_result.xlsx')
echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

l = 0

if 'chemical_data' in st.session_state:
    test_list = st.session_state['chemical_data'][['name','cas_number']]
    st.dataframe(test_list)
    l = 1

else:
    st.warning("Please upload your data on the upload page first.")

if l == 1:
    # Normalize the sheets to have cas numbers as strings
    echa_list['cas_number'] = echa_list['cas_number'].astype(str)
    sin_list['cas_number'] = sin_list['cas_number'].astype(str)
    test_list['cas_number'] = test_list['cas_number'].astype(str)

    # Fill missing data with "NIES" -> Not In Excel Sheet (Missing From Excel Sheet)
    sin_list.fillna('NIES', inplace=True)
    echa_list.fillna('NIES', inplace=True)

    # Join the test list with the refrerence lists
    echa_results = test_list.merge(echa_list, on='cas_number', how='left')
    sin_results = test_list.merge(sin_list, on='cas_number', how='left')

    # Fill the Na Results with Safe (These can be filtered)
    echa_results.fillna('Safe', inplace=True)
    sin_results.fillna('Safe', inplace=True)

    # Filter and seperate DataFrames
    echa_results_safe = echa_results[echa_results['name_y'] == 'Safe'][['name_x' , 'cas_number']].copy().reset_index(drop = True)
    echa_results_not_safe = echa_results[echa_results['name_y'] != 'Safe'].copy().reset_index(drop = True)

    sin_results_safe = sin_results[sin_results['name_y'] == 'Safe'][['name_x' , 'cas_number']].copy().reset_index(drop = True)
    sin_results_not_safe = sin_results[sin_results['name_y'] != 'Safe'].copy().reset_index(drop = True)

    st.write('Your SIN list results are bellow')
    st.dataframe(sin_results_not_safe)

    st.write('Your ECHA regulated chemicals table is bellow')
    st.write('Follow the link in the "Info Card" column to learn more about the substance')
    st.dataframe(echa_results_not_safe)
