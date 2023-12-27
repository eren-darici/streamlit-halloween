import streamlit as st

def show_extras(options):
    # Extras
    st.sidebar.header(options['headers']['extras'])

    ### Glasses yes/no
    glasses = st.sidebar.selectbox(options['selectbox']['glasses']['label'],
                                   options['selectbox']['glasses']['options'],
                                   help=options['selectbox']['glasses']['help'])
    
    return glasses
