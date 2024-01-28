import streamlit as st
from openai_client import generate_costume
from costume_specs import show_costume_specs
from extras import show_extras
import json
import os
from dotenv import load_dotenv
from streamlit_extras.buy_me_a_coffee import button as bmc
from models import Costume  # Import the Costume class

load_dotenv()

CAN_GENERATE_IMAGE = os.getenv('IMAGE')

# Load options from JSON file
with open('./data/sidebar.json', 'r') as json_file:
    options = json.load(json_file)

# Streamlit app layout
st.title(options['headers']['main'])

# Buy me a coffee
bmc(username="erendarici", floating=True, width=221, bg_color="00FFFFFF")

# Main features
st.sidebar.header(options['headers']['specs'])

# Show costume specifications
medium, budget, selected_gender, selected_height, weight = show_costume_specs(options)

# Show extras
age, glasses, hair_length, ethnicity = show_extras(options)

# Button to generate costume
if st.sidebar.button(options['button']['generate_costume']):
    # Validate that mandatory fields are selected
    if not medium or not budget or not selected_gender:
        st.sidebar.warning("Please fill in all mandatory fields.")
    else:
        # Define parameters
        params = {
            "medium": medium,
            "budget": budget,
            "gender": selected_gender,
            "height_feet": selected_height[0],  # Assuming selected_height is a tuple (feet, inches)
            "height_inches": selected_height[1],
            "weight": weight,
            "glasses": glasses,
            "age": age,
            "hair": hair_length,
            "ethnicity": ethnicity
        }

        # Call the GPT API and display results
        ideas = generate_costume(num_costumes=3, kwargs=params)  # Adjust num_costumes as needed
        print(ideas)

        try:
            # Display ideas on the main screen in a card layout
            st.subheader("Generated Costume Ideas:")
            for idea in ideas:
                st.write(f"## {idea.name}")

                for prop in idea.props:
                    st.write(f"   - {prop}")
                st.markdown("---")  # Add a horizontal line between costume ideas for separation
        except json.JSONDecodeError:
            st.warning("Please try again.")
