import streamlit as st

def show_costume_specs(options):
    # Select medium(s)
    medium = st.sidebar.multiselect(options['multiselects']['medium']['label'],
                                    options['multiselects']['medium']['options'],
                                    help=options['multiselects']['medium']['help'])

    # Budget selectbox with labels
    budget = st.sidebar.selectbox(options['selectboxes']['budget']['label'],
                                  options['selectboxes']['budget']['options'],
                                  help=options['selectboxes']['budget']['help'])

    # Add personal info
    ## Gender multiselect
    selected_gender = st.sidebar.multiselect(options['multiselects']['gender']['label'],
                                             options['multiselects']['gender']['options'],
                                             help=options['multiselects']['gender']['help'])

    ## Height
    ### Height selectbox
    st.sidebar.subheader(options['headers']['height'])

    ### Selectbox for feet
    selected_height_feet = st.sidebar.selectbox("Feet:",
                                               options['selectboxes']['height_feet']['options'],
                                               help=options['selectboxes']['height_feet']['help'])

    ### Selectbox for inches
    selected_height_inches = st.sidebar.selectbox("Inches:",
                                                  options['selectboxes']['height_inches']['options'],
                                                  help=options['selectboxes']['height_inches']['help'])

    ### Combine feet and inches
    selected_height = f"{selected_height_feet}'{selected_height_inches}''"

    ## Weight
    weight = st.sidebar.number_input(options['number_input']['weight']['label'],
                                     min_value=options['number_input']['weight']['min_value'],
                                     value=options['number_input']['weight']['value'],
                                     step=options['number_input']['weight']['step'],
                                     max_value=options['number_input']['weight']['max_value'],
                                     help=options['number_input']['weight']['help'])

    return medium, budget, selected_gender, selected_height, weight
