import path
import sys
import os

# Get the current script's directory 
# then get the parent directory by going one level up
# then add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from openai_client import generate_costume


# Test for single generation
def test_parser_single():
    # Test data
    costume_generation_data = {
    "name": "Mystical Wizard",
    "medium": "Movies",
    "gender": ["Male"],
    "budget": ">30$",
    "height_feet": 6,
    "height_inches": 2,
    "glasses": "No",
    "hair": "Long",
    "ethnicity": "White",
    "weight": 180.0,
    "age": 25
    }

    # Generate costume
    created_costume = generate_costume(kwargs=costume_generation_data)

    # Convert to dict
    costume_dict = created_costume[0].model_dump()

    # Delete differences that should be occuring after generation
    del costume_dict['props']
    del costume_dict['name']
    del costume_generation_data['name']

    # Assert
    assert costume_dict == costume_generation_data

# Test for multiple generation
def test_parser_multiple():
    pass