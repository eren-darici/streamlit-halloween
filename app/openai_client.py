import openai
import os
from dotenv import load_dotenv



# Create class
class MyOpenAIClient():
    def __init__(self):
        # Load .env
        load_dotenv()

        # Get API KEY
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

        # Create client
        self.client = openai.OpenAI(api_key=self.OPENAI_API_KEY)
        

    def generate_costume_idea(self, params):
        # Define user prompt
        self.user_prompt = f"""
        You are my personal assistant to pick my halloween costume for this upcoming halloween.
        You need to help me about that, and if you help me I will give you 200$ tip, but you won't mention that.
        You only need to give me the name of the costume, props for that costume as a list.
        I'm a {params['height']} and {params['weight']}lbs {params['gender']}. I like {params['medium']}. My budget for this costume is {params['budget']}.
        You need to give me the costume from {params['medium']}, and it should be well known costume. Since it would be a cosplay, there is no copyright barrier.
        Give me the ideas as following JSON format and MAKE SURE THAT CHARACTER LOOKS LIKE THE CHARACTER ITSELF AND NO OTHER CHARACTER (I will tip you 200$ more if you can do that):
        in a list, for each costume:
            costume: costume name (string)
            props: list of props
            dalle_prompt: a prompt for Dall-e, that contains both character and my specifications and include props.

        example output:
        "[
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
        ]"

        IMPORTANT! For the response, delete any trailing character besides JSON. IT IS IMPORTANT!
        """

        # Check extras
        if params['glasses'] == "Yes":
            self.user_prompt += f"I also wear glasses."

        # Define system prompt
        self.system_prompt = "Sure! Here are 3 costume ideas from the mediums that you like that are related to your specifications regarding your look and your budget:"

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

        return message

    def generate_costume_image(self, prompt):
        # Create response
        response = self.client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Get Image URL
        image_url = response.data[0].url
        print(prompt)

        return image_url
        