from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Define a simple tool
def basic_math_tool(input: str) -> str:
    try:
        return str(eval(input)) # Evaluates basic math expressions
    except Exception as e:
        return f'Error: {str(e)}'

def main():
    # Load env variables
    load_dotenv()

    # Define LLM
    llm = ChatOpenAI(model='gpt-4o', temperature=0.0)

    # Create math_tool
    math_tool = Tool(
        name='MathTool',
        func=basic_math_tool,
        description="Perform basic math operations like addition, subtraction, etc. using python eval. Args: input (str). Return answer or error (str).",
    )

    agent = initialize_agent(
        tools=[math_tool],  # The `tools` parameter takes a list of tools the agent can use
        llm=llm,  # The `llm` parameter specifies the language model the agent will use to generate responses
        agent='zero-shot-react-description',  # 'zero-shot-react-description' is a LangChain agent type that processes queries without prior training on specific tasks
        verbose=True  # When `verbose=True`, the agent provides detailed logs about its reasoning and actions during execution,
    )

    response = agent.invoke(input('Write your math question\n--> '), handle_parsing_errors=True)

    print(f"ChatGPT:\n{response['output']}")

if __name__ == '__main__':
    main()
