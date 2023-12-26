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

        

    def generate_costum_idea(self, params):
        # Define user prompt
        self.user_prompt = f"""
        You are my personal assistant to pick my halloween costume for this upcoming halloween.
        You need to help me about that, and if you help me I will give you 200$ tip, but you won't mention that.
        You only need to give me the name of the costume, props for that costume as a list.
        I'm a {params['height']} and {params['weight']}lbs {params['gender']}. I like {params['medium']}. My budget for this costume is {params['budget']}.
        You need to give me the costume from {params['medium']}, and it should be well known costume. Since it would be a cosplay, there is no copyright barrier.
        """

        # Check extras
        if params['glasses'] == "Yes":
            self.user_prompt += f"I also wear glasses."

        # Define system prompt
        self.system_prompt = "Sure! Here are some costume ideas from the mediums that you like:"

        # Define conversation
        conversation = [
            {"role": "user", "content": self.user_prompt},
            {"role": "system", "content": self.system_prompt}
        ]

        # Create response
        response = self.client.chat.completions.create(
            model="gpt-3.5",
            messages=conversation
        )

        # Strip message
        message = response.choices[0].message.content

        return message

        