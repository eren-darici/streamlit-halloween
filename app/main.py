import streamlit as st
import requests

# Streamlit app layout
st.title("Halloween Costume Generator")


# Main features
st.sidebar.header("Select costume specs")

# Select medium(s)
medium_list = ["TV", "Comics", "Movies"]
medium = st.sidebar.multiselect("Select your favorite medium:", medium_list)

# Budget selectbox with labels
budget_levels = ["Low", "Medium", "High"]
budget_label = st.sidebar.selectbox("Select your budget:", budget_levels)


# Add personal info
## Gender multiselect
gender_options = ["Male", "Female", "Non-Binary"]
selected_gender = st.sidebar.multiselect("Select your gender:", gender_options)

## Height (selectbox from 4' to 7')
height_options = []
selected_height = st.sidebar.selectbox("Select your height:", height_options)

## Weight
weight = st.sidebar.number_input("Enter your weight (lbs):", min_value=0, value=150, step=1, max_value=500)

## Extras
st.sidebar.header("Extras")

### Glasses yes/no
glasses = st.sidebar.selectbox("Do you wear glasses?", ("Yes", "No"))