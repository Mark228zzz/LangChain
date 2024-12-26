# LangChain

Welcome to my LangChain repository! This is a collection of projects and experiments demonstrating the use of LangChain for building robust and scalable applications in natural language processing (NLP), conversational AI, and more.

## Features

- **Tool Integrations**: Examples of using LangChain with tools.
- **Interactive Chatbots**: Examples of conversational agents using LangChain.
- **Document Retrieval**: Applications for retrieving and summarizing documents.
- **Custom Pipelines**: Tailored pipelines for integrating language models with external tools.
- **Streamlined APIs**: Code examples for seamless interaction with Hugging Face, OpenAI.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mark228zzz/LangChain.git
   cd LangChain
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## API-KEY

### Why API-KEY?
LangChain uses API keys for services like OpenAI, Pinecone, and Weaviate.
API keys are required to authenticate and access these services.

### How to Get an OpenAI API-KEY?
1. Go to OpenAI API Keys page.
2. Log in or sign up, create a new secret key, and copy it.
3. Note: OpenAI API **is not free**; you must purchase credits to use it.

### How to Put Your API-KEY?
1. Create a environment variable `OPENAI_API_KEY` and put your api_key in `/LangChain/.env` (**NOTE DO NOT SHOW ANYBODY YOUR API KEY!**):

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

2. To use it just import dotenv and load the environment`s variables:
```python
from dotenv import load_dotenv

# Load all environment`s variables
load_dotenv()
```

## Directory Structure

### Your project should now look like this:
```
/LangChain/
    /.../
    /langchain_env/
    /.env
    /README.md
    /requirements.txt
    /.gitignore
```

## Usage
1. Run any script to see LangChain in action:
   ```bash
   python basic_chatbot.py
   ```
2. Customize the code to fit your needs.

## Examples

### Chatbot Example
A simple chatbot implemented with LangChain:
```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(temperature=0.7)
chain = ConversationChain(llm=chat)
response = chain.run("Tell me a fun fact about space.")
print(response)
```

### Document Summarizer
Summarize large documents in seconds:
```python
from langchain.document_loaders import PyPDFLoader
from langchain.chains import SummarizationChain
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("example.pdf")
documents = loader.load()
chain = SummarizationChain()
summary = chain.run(documents)
print(summary)
```

## Contribution

Feel free to open issues or submit pull requests to improve the code and add new features. Contributions are welcome!

*Enjoy experimenting with LangChain!*
