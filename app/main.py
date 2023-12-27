import streamlit as st
from openai_client import MyOpenAIClient
import json

# Streamlit app layout
st.title("Halloween Costume Generator")

# Main features
st.sidebar.header("Select costume specs")

# Select medium(s)
medium_list = ["TV", "Comics", "Movies", "Music", "Anime", "Manga"]
medium = st.sidebar.multiselect("Select your favorite medium:", medium_list, help="Select at least one medium.")

# Budget selectbox with labels
budget_levels = ["Low", "Medium", "High"]
budget = st.sidebar.selectbox("Select your budget:", budget_levels, help="Select a budget level.")

# Add personal info
## Gender multiselect
gender_options = ["Male", "Female", "Non-Binary"]
selected_gender = st.sidebar.multiselect("Select your gender:", gender_options, help="Select at least one gender.")

## Height
### Height selectbox
st.sidebar.subheader("Select your height:")

### Selectbox for feet
height_feet_options = list(range(4, 8))
selected_height_feet = st.sidebar.selectbox("Feet:", height_feet_options, help="Select your height in feet.")

### Selectbox for inches
height_inches_options = list(range(0, 12))
selected_height_inches = st.sidebar.selectbox("Inches:", height_inches_options, help="Select your height in inches.")

### Combine feet and inches
selected_height = f"{selected_height_feet}'{selected_height_inches}''"

## Weight
weight = st.sidebar.number_input("Enter your weight (lbs):", min_value=0, value=150, step=1, max_value=500, help="Enter your weight in pounds.")

## Extras
st.sidebar.header("Extras")

### Glasses yes/no
glasses = st.sidebar.selectbox("Do you wear glasses?", ("Yes", "No"), help="Select whether you wear glasses or not.")

# Button to generate costume
if st.sidebar.button("Generate Costume"):
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

                # Display the costume image
                image_url = client.generate_costume_image(prompt=idea['dalle_prompt'])
                st.image(image_url, caption="Costume Image", use_column_width=True)


                for prop in idea['props']:
                    st.write(f"   - {prop}")
                st.markdown("---")  # Add a horizontal line between costume ideas for separation
        except json.JSONDecodeError:
            st.warning("Unable to parse response from the GPT API. Please try again or check the API response format.")
