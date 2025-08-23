from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, Tool

# Define the brainstorming tool
def brainstorm(problem: str) -> str:
    """
    Tool to brainstorm solutions about a given problem.
    """
    solutions = [
        f"Explore historical context of {problem}.",
        f"Analyze current trends related to {problem}.",
        f"Explain the importance of {problem} right now.",
        f"Predict future implications of {problem} in technology, society, etc.",
        f"Suggest concrete ways to solve {problem}.",
        f"Run thought experiments about {problem}.",
        f"Check if scientific laws are violated in any proposals and refine.",
        f"Iteratively try different approaches to solve {problem}.",
        "Write a summary of the best solution found."
    ]
    return "Here are some brainstormed directions:\n- " + "\n- ".join(solutions)

def main():
    load_dotenv()

    # Initialize brainstorming tool
    brainstorm_tool = Tool(
        name="BrainstormTool",
        func=brainstorm,
        description="Generates multiple directions and perspectives for exploring a problem."
    )

    # Define the LLM (you can use gpt-4o or gpt-4.1)
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

    # Create agent (modern way)
    researcher_agent = initialize_agent(
        tools=[brainstorm_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # <- correct enum, not raw string
        verbose=True,
        handle_parsing_errors=True
    )

    # Agent execution
    problem = input("Write world problem --> ")

    response = researcher_agent.run(f"Research and solve this problem: {problem}")

    print("\n--- Final Research Output ---\n")
    print(response)

if __name__ == "__main__":
    main()
