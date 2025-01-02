from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from colorama import Fore

# Examples of prompts
texts = ['I`m sooo happy that I have a dog!', 'I don`t care about that', 'IT`S REAAALLYY BAAAD!', 'yes, I liked it', 'no, it`s not good']

def main():
    # Load environment variables from the .env file
    load_dotenv()

    classification_template = """
    Given the text: {text}, classify it as one of the following categories (response ONLY class and SHORT answer why):
    - Super positive
    - Positive
    - Neutral
    - Negative
    - Super negative
    """

    classification_prompt_template = PromptTemplate(input_variables=['text'], template=classification_template)

    llm = ChatOpenAI(model='gpt-4o', temperature=0.0)

    chain = classification_prompt_template | llm

    for text in texts:
        response = chain.invoke(text)

        print(f'{Fore.LIGHTGREEN_EX}{text}:\n{Fore.LIGHTBLUE_EX}{response.content}\n')

if __name__ == '__main__':
    main()
