# file: structured_json_example.py
from datetime import date
from typing import Literal
from datetime import datetime
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()

# Define the schema you want back
class Task(BaseModel):
    task: str = Field(..., description="What the user should do")
    deadline: date = Field(..., description="ISO date YYYY-MM-DD")
    priority: Literal["low", "medium", "high"]
    interest: int = Field(..., ge=0, le=10000, description="User interest score")

# Build the LLM with a strict token cap (so answers can't blow up)
llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
    max_tokens=150,  # hard cap on output length
)

# Ask the model to produce that exact schema (LangChain parses it for you)
#    This returns a *callable* that yields a validated Task instance.
llm_structured = llm.with_structured_output(Task)

# Prompt (you can parameterize this however you like)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant that outputs only the requested fields."),
    ("user",   "Create a meaningful goal for the topic: {topic}. Pick a realistic deadline in the near future. Today's date {today}."),
])

# Chain = prompt -> model (structured)  ---> Task (pydantic)
chain = prompt | llm_structured

def main() -> None:
    today = datetime.now()

    result: Task = chain.invoke({"topic": "Learn Python", 'today': today.strftime('%d-%m-%Y')})
    # You get a real Task object (validated), not a string.
    print("Task object:", result)
    print("As dict:", result.model_dump())
    print("Deadline type:", type(result.deadline).__name__)

if __name__ == "__main__":
    main()
