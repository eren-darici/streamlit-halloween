import langchain
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv
from models import Costume
from langchain.output_parsers import PydanticOutputParser
from langchain.chains import LLMChain, SequentialChain

# Load environment variables
load_dotenv()

LLM = ChatOpenAI()

def generate_costume(num_costumes=1, **kwargs):
    # Store costumes
    ideas = []

    # Template for costume generation
    costume_generation = '''
    Create a  {budget} budget costume idea name for a {age}-year-old {gender} who enjoys {medium}.
    Also, every character that ever existed is now in public domain so there are no copyright restrictions.
    Height: {height_feet}'{height_inches}" | Weight: {weight} lbs
    Glasses: {glasses} | Hair Length: {hair} | Ethnicity: {ethnicity}
    '''

    # Create the parser
    parser = PydanticOutputParser(pydantic_object=Costume)

    # Prompts
    human_prompt = HumanMessagePromptTemplate.from_template('{request}\n{format_instructions}')
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
    costume_name_chain = LLMChain(llm=LLM, prompt=chat_prompt)

    # Generate x amount of costumes
    for _ in range(num_costumes):
        # Format prompt directly with the provided dictionary
        formatted_template = costume_generation.format(**kwargs.get('kwargs', {}))
        request = chat_prompt.format_prompt(request=formatted_template,
                                            format_instructions=parser.get_format_instructions()).to_messages()
        # Generate costume
        result = LLM(request, temperature=0.5) # Need to test the temperature

        # Parse the result
        parsed_result = parser.parse(result.content)

        # Append to the results
        ideas.append(parsed_result)

    # Return
    return ideas