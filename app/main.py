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

## Height
### Height selectbox
st.sidebar.subheader("Select your height:")

### Selectbox for feet
height_feet_options = list(range(4, 8))
selected_height_feet = st.sidebar.selectbox("Feet:", height_feet_options)

### Selectbox for inches
height_inches_options = list(range(0, 12))
selected_height_inches = st.sidebar.selectbox("Inches:", height_inches_options)

### Combine feet and inches
selected_height = f"{selected_height_feet}'{selected_height_inches}''"

## Weight
weight = st.sidebar.number_input("Enter your weight (lbs):", min_value=0, value=150, step=1, max_value=500)

## Extras
st.sidebar.header("Extras")

### Glasses yes/no
glasses = st.sidebar.selectbox("Do you wear glasses?", ("Yes", "No"))