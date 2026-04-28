import streamlit as st
import pandas as pd

if 'mode' not in st.session_state:
    st.session_state['mode'] = 'Default'

if 'result_sucsess' not in st.session_state:
    st.session_state['result_sucsess'] = 'No_result'

st.title("Welcome to the Results page!")
st.write('This page may take a few moments to load.')
st.write("The first table of information that appears below includes the data from your Chemical Information Sheet.")
st.info(f"You are currently in {st.session_state['mode']} mode.")

if st.session_state['mode'] == 'Default':
    sin_list = pd.read_excel('SinList_result.xlsx')
    echa_list = pd.read_excel('chemical_universe_list_en.xlsx')

elif st.session_state['mode'] == 'Advanced':
    if 'sin_table' in st.session_state and 'echa_table' in st.session_state:
        sin_list = st.session_state['sin_table']
        echa_list = st.session_state['echa_table']
    
    else:
        st.warning("Please upload your reference tables on the Mode page first.")
        st.stop()

l = 0

if 'chemical_data' in st.session_state:
    test_list = st.session_state['chemical_data'][['name','cas_number']]
    st.dataframe(test_list)
    l = 1

else:
    st.warning("Please upload your data on the upload page first.")

if l == 1:
    try:
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
        echa_results_safe = echa_results[echa_results['name_y'] == 'Safe'][['name_x', 'cas_number']].copy().reset_index(drop=True).rename(columns={'name_x': 'test_list_name'})
        st.session_state['echa_s'] = echa_results_safe
        
        echa_results_not_safe = echa_results[echa_results['name_y'] != 'Safe'].copy().reset_index(drop=True).rename(columns={'name_x': 'test_list_name', 'name_y': 'ECHA_list_name'})
        st.session_state['echa_ns'] = echa_results_not_safe
        
        sin_results_safe = sin_results[sin_results['name_y'] == 'Safe'][['name_x', 'cas_number']].copy().reset_index(drop=True).rename(columns={'name_x': 'test_list_name'})
        st.session_state['sin_s'] = sin_results_safe
        
        sin_results_not_safe = sin_results[sin_results['name_y'] != 'Safe'].copy().reset_index(drop=True).rename(columns={'name_x': 'test_list_name', 'name_y': 'SIN_list_name'})
        st.session_state['sin_ns'] = sin_results_not_safe
        
        st.subheader('SIN List Matches: The chemicals in the table below are chemicals you use that are on the SIN List')
        st.subheader("Navigate the results table to understand why each chemical is included in the SIN List, its REACH status, possible safer substitutes, and much more.")
        st.dataframe(sin_results_not_safe)
  
        st.subheader('REACH Regulation Matches: The chemicals in the table below are chemicals you use that have been registered under the REACH regulation.')
        st.write('Navigate the results table to understand the status of each chemical under REACH and use the “infocard” and other information to learn more about each chemical.')
        st.dataframe(echa_results_not_safe)
        
        st.session_state['result_sucsess'] = 'result_passed'
        st.success('You have Sucsessfully Uploaded Your Chemicals! :)')
        #st.write("we made it all the way here")
        
    except:
        st.warning('Something went wrong Please ensure your column names are consistent with the examples and ensure your Cas numbers are strings.')

 
