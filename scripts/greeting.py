from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

def main():
    # Load env variables
    load_dotenv()

    # Create a chat
    chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.7)

    # Create a user message
    messages = [{"role": "user", "content": "Hello ChatGPT from LangChain!"}]

    # Get a response
    response = chat.invoke(messages)

    print(f'ChatGPT: {response.content}')

if __name__ == '__main__':
    main()
