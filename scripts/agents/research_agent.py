from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Define Tools for the Researcher
def brainstorm(problem: str) -> str:
    '''
    Tool to brainstorm solutions about a given problem.
    '''
    solutions = [
        'Try to thing out of the box and thing widthly.'
        f'Explore historical context of {problem}. Or figure out do people know about this problem.',
        f'Analyze current trends related to {problem}.',
        f'Write importance of {problem} at that moment.',
        f'Predict future implications of {problem} in technology, society and etc.',
        f'Way to solve {problem}. How exactly.',
        f'Make a mind experiments of {problem}.',
        'Check if any laws of physics, chemestry and etc. were violated in experiments you did. If so try again fixing that problem.',
        f'You have to try a few times to solve {problem}.',
        'Write a summary of final answer IF you tried or thing that it is a final answer.'
    ]
    return f'Here are some brainstormed solutions:\n- ' + '\n- '.join(solutions)

def main():
    load_dotenv()

    # Initialize tool
    brainstorm_tool = Tool(
        name='BrainstormTool',
        func=brainstorm,
        description='Generates solutions and perspectives to explore a problem.'
    )

    # Define LLM
    llm = ChatOpenAI(model='gpt-4o', temperature=0.7)

    # Create researcher agent
    researcher_agent = initialize_agent(
        tools=[brainstorm_tool],
        llm=llm,
        agent='zero-shot-react-description',
        verbose=True
    )

    # Agent execution
    problem = input('Write world problem --> ')

    researcher_agent.run(f'Research and solve: {problem}')

if __name__ == '__main__':
    main()
