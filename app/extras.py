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
    
    # Race (optional)
    if not options['selectboxes']['race'].get('is_optional') or st.sidebar.checkbox("Include Race"):
        race = st.sidebar.selectbox(options['selectboxes']['race']['label'],
                                     options['selectboxes']['race']['options'],
                                     help=options['selectboxes']['race']['help'])
    else:
        race = None
    
    return glasses, hair_length, race
