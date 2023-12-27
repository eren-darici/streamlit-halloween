import streamlit as st
from openai_client import MyOpenAIClient
from costume_specs import show_costume_specs
from extras import show_extras
import json
import os
from dotenv import load_dotenv
from streamlit_extras.buy_me_a_coffee import button as bmc
from db import insert_image, check_cache

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
            "height": selected_height,
            "weight": weight,
            "glasses": glasses,
            "age": age,
            "hair_length": hair_length,
            "ethnicity": ethnicity
        }

        # Call the GPT API and display results
        client = MyOpenAIClient()
        ideas = client.generate_costume_idea(params=params).strip().strip('```')
        print(ideas)

        try:
            # Try to parse ideas as JSON
            ideas_json = json.loads(ideas)
            print(ideas_json)

            # Display ideas on the main screen in a card layout
            st.subheader("Generated Costume Ideas:")
            for idea in ideas_json:
                st.write(f"## {idea['costume']}")

                if CAN_GENERATE_IMAGE == "YES":
                    # First check cache
                    result, match = check_cache(new_prompt=idea['dalle_prompt'], costume_name=idea['costume'])
                    if result:
                        image_url = match.get('image_url')
                    else:
                        # Display the costume image
                        image_url = client.generate_costume_image(prompt=idea['dalle_prompt'])
                        insert_image(prompt=idea['dalle_prompt'], image_url=image_url, costume_name=idea['costume'])
                        
                    st.image(image_url, caption="Costume Image", use_column_width=True)

                for prop in idea['props']:
                    st.write(f"   - {prop}")
                st.markdown("---")  # Add a horizontal line between costume ideas for separation
        except json.JSONDecodeError:
            st.warning("Please try again.")
