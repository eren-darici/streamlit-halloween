from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
from openai_client import MyOpenAIClient
from fuzzywuzzy import fuzz
import random


def create_connection():
    load_dotenv()

    MONGO_URI = os.getenv('MONGO_URI')
    # Create a new client and connect to the server
    client = MongoClient(MONGO_URI)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Access DB
    db = client['halloween-general']

    return db

def insert_image(prompt, image_url, costume_name):
    # Access images collection
    collection = create_connection().images

    # Create data to be inserted
    data = {
        'prompt': prompt,
        'image_url': image_url,
        'costume_name': costume_name
    }

    # insert image
    collection.insert_one(data)

def check_cache(new_prompt, costume_name):
    # Access images collection
    collection = create_connection().images

    # Retrieve all documents
    all_documents = collection.find()

    # Iterate through each document and check for fuzzy matching
    matches = []
    for document in all_documents:
        stored_costume_name = document.get('costume_name')
        if stored_costume_name and fuzz.partial_ratio(costume_name, stored_costume_name) >= 80:
            # Consider it a match if the partial ratio is at least 80 (you can adjust this threshold)
            matches.append(document)

    # For each match, check prompts
    openai_client = MyOpenAIClient()

    # Final matches
    final_matches = []

    # Check each match
    for match in matches:
        response = openai_client.check_cache(new_prompt, match.get('prompt'))
        
        
        if response == 'True':
            print("Match")
            # Add to final matches
            final_matches.append(match)
    
    if final_matches != []:
        return True, random.choice(final_matches)
    else:
        return False, []