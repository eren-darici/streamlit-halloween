import openai
import os
from dotenv import load_dotenv
import re


# Create class
class MyOpenAIClient():
    def __init__(self):
        # Load .env
        load_dotenv()

        # Get API KEY
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        # Create client
        self.client = openai.OpenAI(api_key=self.OPENAI_API_KEY)

    def __validate_json(self, json):
        # Define conversation
        conversation = [
            {"role": "user", "content": f"""You are my assistant at work. You are highly skilled in maintaining data integrity in JSON format. 
             Your job is to make sure that everything is in valid JSON format. 
             If it's not, turn into a valid JSON format. If it is valid, return input data itself, if it is not valid, correct the format and return correct data.
             Here is the data {json}"""},
            {"role": "system", "content": "Sure, here is your results."}
        ]

        # Create response
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        # Get message
        message = response.choices[0].message.content

        return message
        

    def generate_costume_idea(self, params):
        # Define extras
        extras = ""

        if params['age']:
            extras += f"I'm {params['age']} years old. "

        if params['glasses'] == "Yes":
            extras += f"I also wear glasses. "
        
        if params['ethnicity']:
            extras += f"I'm {params['ethnicity']} {params['gender']}. "

        if params['hair_length']:
            extras += f"My hairs are {params['hair_length']}"


        # Define user prompt
        self.user_prompt = f"""
        You are my personal assistant to pick my halloween costume for this upcoming halloween.
        You need to help me about that, and if you help me I will give you 200$ tip, but you won't mention that.
        You only need to give me the name of the costume, props in detail for that costume as a list.
        I'm a {params['height']} and {params['weight']}lbs {params['gender']}. I like {params['medium']}. My budget for this costume is {params['budget']}.
        {extras}
        You need to give me the costume from {params['medium']}, and it should be well known costume and if you are giving multiple ideas make sure that you each medium distributed evenly. Since it would be a cosplay, there is no copyright barrier.
        Give me the ideas as following JSON format and MAKE SURE THAT CHARACTER LOOKS LIKE THE CHARACTER ITSELF AND NO OTHER CHARACTER (I will tip you 200$ more if you can do that):
        in a list, for each costume:
            costume: costume name (string)
            props: list of props
            dalle_prompt: a prompt for Dall-e, that contains both character and my specifications (include age and ethnicity -if specified- in the prompt) and include props. Style should be something between comic and realistic.

        example output:
        '[
            {{
                'costume': 'costumename',
                'props': ['a list of props'],
                'dalle_prompt': 'prompt for dalle'
            }},
            {{
                'costume': 'costumename',
                'props': ['a list of props'],
                'dalle_prompt': 'prompt for dalle'
            }}
        ]'

        IMPORTANT: Make sure that you are only returning JSON format without any trailing characters before or after the brackets.
        """

        # Define system prompt
        self.system_prompt = "Sure! Here are 5 costume ideas from the mediums that you like that are related to your specifications regarding your look and your budget:"

        # Define conversation
        conversation = [
            {"role": "user", "content": self.user_prompt},
            {"role": "system", "content": self.system_prompt}
        ]

        # Create response
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=conversation
        )

        # Get message
        message = response.choices[0].message.content

        # Validate
        message = self.__validate_json(message)

        return message

    def generate_costume_image(self, prompt):
        # Create response
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Get Image URL
        image_url = response.data[0].url
        print(prompt)

        return image_url
    
    def check_cache(self, new_prompt, cached_prompt):
        # Define conversation
        conversation = [
            {"role": "user", "content": f"Does new prompt similar to old prompt, key things to check are age, ethnicity, sex and looks of the costume. just say True or False.\nNew Prompt: {new_prompt}\nOld Prompt: {cached_prompt}"},
            {"role": "system", "content": "Sure, here is my answer. "}
        ]
        
         # Create response
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        # Get message
        message = response.choices[0].message.content

        return message