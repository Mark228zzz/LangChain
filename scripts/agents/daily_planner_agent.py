from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Tool: Suggest Morning Routine
def morning_routine(input: str) -> str:
    return "Start with a 10-minute meditation, then have a healthy breakfast like oatmeal or eggs."

# Tool: Suggest Afternoon Activity
def afternoon_activity(input: str) -> str:
    return "Take a 20-minute walk, and then focus on one productive task for the next two hours."

# Tool: Suggest Evening Relaxation
def evening_relaxation(input: str) -> str:
    return "Read a book for 30 minutes, then unwind with some light stretching or yoga."

def main():
    load_dotenv()

    # Define Tools
    tools = [
        Tool(name="Morning Routine", func=morning_routine, description="Suggest a morning routine."),
        Tool(name="Afternoon Activity", func=afternoon_activity, description="Suggest an activity for the afternoon."),
        Tool(name="Evening Relaxation", func=evening_relaxation, description="Suggest how to relax in the evening."),
    ]

    llm = ChatOpenAI(model='gpt-4o', temperature=0.0)

    # Initialize Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    # Run the Agent
    print("Ask me for suggestions for your day! (Type 'exit' to quit)")
    while True:
        query = input("What part of the day should I help you with? ")

        if query.lower() == "exit":
            break
        response = agent.invoke(query, handle_parsing_errors=True)

        print(response['output'])

if __name__ == '__main__':
    main()
