import streamlit as st
from openai_client import MyOpenAIClient
import json
import os
from dotenv import load_dotenv

CAN_GENERATE_IMAGE = os.getenv('IMAGE')

# Load options from JSON file
with open('sidebar.json', 'r') as json_file:
    options = json.load(json_file)

# Streamlit app layout
st.title(options['headers']['main'])

# Main features
st.sidebar.header(options['headers']['specs'])

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

## Extras
st.sidebar.header(options['headers']['extras'])

### Glasses yes/no
glasses = st.sidebar.selectbox(options['selectbox']['glasses']['label'],
                               options['selectbox']['glasses']['options'],
                               help=options['selectbox']['glasses']['help'])

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
            "height": selected_height,
            "weight": weight,
            "glasses": glasses,
        }

        # Call the GPT API and display results
        client = MyOpenAIClient()
        ideas = client.generate_costume_idea(params=params).strip('"').strip()
        print(ideas)
        
        try:
            # Try to parse ideas as JSON
            ideas_json = json.loads(ideas)
            print(ideas_json)

            # Display ideas on the main screen in a card layout
            st.subheader("Generated Costume Ideas:")
            for idea in ideas_json:
                st.write(f"## {idea['costume']}")

                if CAN_GENERATE_IMAGE:
                    # Display the costume image
                    image_url = client.generate_costume_image(prompt=idea['dalle_prompt'])
                    st.image(image_url, caption="Costume Image", use_column_width=True)

                for prop in idea['props']:
                    st.write(f"   - {prop}")
                st.markdown("---")  # Add a horizontal line between costume ideas for separation
        except json.JSONDecodeError:
            st.warning("Unable to parse response from the GPT API. Please try again or check the API response format.")
