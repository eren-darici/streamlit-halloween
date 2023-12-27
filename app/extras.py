import streamlit as st

def show_extras(options):
    # Extras
    st.sidebar.header(options['headers']['extras'])

    # Age (optional)
    if not options['number_input']['age'].get('is_optional') or st.sidebar.checkbox("Include Age"):
        age = st.sidebar.number_input(options['number_input']['age']['label'],
                                     min_value=options['number_input']['age']['min_value'],
                                     value=options['number_input']['age']['value'],
                                     step=options['number_input']['age']['step'],
                                     max_value=options['number_input']['age']['max_value'],
                                     help=options['number_input']['age']['help'])
    else:
        age = None

    # Glasses yes/no
    if not options['selectboxes']['glasses'].get('is_optional') or st.sidebar.checkbox("Include Glasses"):
        glasses = st.sidebar.selectbox(options['selectboxes']['glasses']['label'],
                                    options['selectboxes']['glasses']['options'],
                                    help=options['selectboxes']['glasses']['help'])
    else:
        glasses = None
    
    # Hair length (optional)
    if not options['selectboxes']['hair'].get('is_optional') or st.sidebar.checkbox("Include Hair Length"):
        hair_length = st.sidebar.selectbox(options['selectboxes']['hair']['label'],
                                           options['selectboxes']['hair']['options'],
                                           help=options['selectboxes']['hair']['help'])
    else:
        hair_length = None
    
    # Ethnicity (optional)
    if not options['selectboxes']['ethnicity'].get('is_optional') or st.sidebar.checkbox("Include Ethnicity"):
        ethnicity = st.sidebar.selectbox(options['selectboxes']['ethnicity']['label'],
                                     options['selectboxes']['ethnicity']['options'],
                                     help=options['selectboxes']['ethnicity']['help'])
    else:
        ethnicity = None
    
    return age, glasses, hair_length, ethnicity
