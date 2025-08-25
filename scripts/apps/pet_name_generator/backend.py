from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from typing import Optional
from dotenv import load_dotenv

# Load env variables
load_dotenv()

NO_TEMPERATURE_MODELS = ['o1', 'o1-mini', 'o1-preview', 'o3-mini', 'gpt-5']

def get_llm(model: str, temp: float):
    if model in NO_TEMPERATURE_MODELS: return ChatOpenAI(model=model, temperature=temp)

    return ChatOpenAI(model=model, temperature=temp)

def generate_name(type: str, color: str, prefference: Optional[str] = None, n_names: int = 5,  temp: float = 0.9, model: str = 'gpt-3.5-turbo'):
    # Get LLM
    llm = get_llm(model, temp)

    # Create a prompt template to make model follow rules
    prompt = PromptTemplate(
        input_variables=['type', 'color'],
        optional_variables=['prefference'],
        template='''Come up with top {n_names} cool pet names for me.
        Pet type: {type}
        Pet color: {color}
        Prefferences which suppose affect name: {prefference}

        Make your answer strictly short and easy to understand in list form.
        Max 1-3 words and pre-words as "of", "mr", "ms" etc.
        ANSWER ONLY A LIST.
        '''
    )

    # Create a chain
    chain = prompt | llm

    # Get the response
    response = chain.invoke({'n_names': n_names, 'type': type, 'color': color, 'prefference': prefference})

    return response.content
