from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage, BaseMessage
from langchain.prompts import PromptTemplate
from typing import Literal, List
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv
from config import ENTRY_TEMPLATE

# Load env variables
load_dotenv()


class GameBase(BaseModel):
    game_content: str = Field(..., description="Narration for the next step of the game.")
    choices: List[str] = Field(..., description="Exactly 4 choices for the player.")

    @field_validator("choices")
    def must_have_four(cls, v: List[str]) -> List[str]:
        if len(v) != 4:
            raise ValueError("choices must contain exactly 4 items")
        return v


def start_game(topic: str, length: str, memory: List[BaseMessage]) -> None:
    """Seed the conversation with a system instruction + the human's topic."""
    if not memory or not isinstance(memory[0], SystemMessage):
        add_memory(
            "system",
            ENTRY_TEMPLATE.format(length=length),
            memory
        )

    add_memory("human", f"Start a new game about: {topic}", memory)

def get_llm(model: str, temp: float):
    return ChatOpenAI(model=model, temperature=temp)

# Adding in memory message based on role: AI, Human, System
def add_memory(role: Literal['ai', 'human', 'system'], content: str, memory: List[BaseMessage]) -> None:
    # Normalize role string
    role = role.lower().strip()

    # Check which role
    match role:
        case 'ai':
            message = AIMessage(content)
        case 'human':
            message = HumanMessage(content)
        case 'system':
            message = SystemMessage(content)
        case _:
            raise ValueError(f'The role {role} is not valid')

    memory.append(message)

# Play one step in the game. One choice forward
def play(model: str, temp: float, memory: List[BaseMessage], summary_last_n: int, length: str):
    # Get LLM
    llm = get_llm(model, temp)

    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["game_history"],
        template=(
            "You are playing a choice-based, never-ending narrative game with a human.\n"
            "Use the prior game history to continue the story.\n\n"
            "GAME HISTORY:\n"
            "{game_history}\n\n"
            "OUTPUT RESTRICTIONS:\n"
            "- Respond with the next short scene as 'game_content'.\n"
            "- Provide exactly four distinct, actionable options as 'choices'.\n"
            "- Do not include numbering in 'choices'; each item is plain text.\n"
        ),
    )

    # Create a structured response chain
    chain = prompt | llm.with_structured_output(GameBase)

    # Get the response based on memory
    result: GameBase = chain.invoke({'game_history': memory})

    # Add AI response to memory
    add_memory('ai', f'Game content: {result.game_content}\nChoices:{result.choices}', memory)

    # Check if summary is required
    if len(memory) >= summary_last_n:
        summary = summarize(memory, 150)

        memory.clear()

        summary = 'Summary of previous turns in the game:\n' + summary

        add_memory(
            "system",
            ENTRY_TEMPLATE.format(length=length),
            memory
        )
        add_memory('system', summary, memory)

    return result

def summarize(memory: List[BaseMessage], target_words: int) -> ...:
    llm = get_llm('gpt-4o', temp=0.0)

    prompt = PromptTemplate(
        input_variables=['target_words', 'old_text'],
        template='''Summarize the following earlier game turns in
        ~{target_words} words. Keep only persistent facts, goals, inventory,
        locations, and unresolved threads. No meta commentary.\n\n
        {old_text}''')

    summarizer = prompt | llm

    response = summarizer.invoke({'target_words': target_words, 'old_text': memory})

    return response.content
