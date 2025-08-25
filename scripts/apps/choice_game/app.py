import streamlit as st
from backend import start_game, play, add_memory  # your functions

# ------------- Helpers -------------
def reset(topic: str, length: str):
    """Clear per-session state and seed the game."""
    st.session_state.memory = []

    st.session_state.step = 0
    st.session_state.last_response = None

    start_game(topic, length, st.session_state.memory)

    # Immediately play the first turn
    st.session_state.last_response = play(
        st.session_state.model, st.session_state.temp, st.session_state.memory, summary_last_n, length
    )

def init_state():
    if "memory" not in st.session_state:
        st.session_state.memory = []
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "last_response" not in st.session_state:
        st.session_state.last_response = None
    if "model" not in st.session_state:
        st.session_state.model = "gpt-4o-mini"
    if "temp" not in st.session_state:
        st.session_state.temp = 0.3


# ------------- UI -------------
st.set_page_config(page_title="🎲 Choice Game", page_icon="🎲")
st.title("🎲 Choice Game")

init_state()

with st.sidebar:
    st.header("⚙️ Settings")

    # Pick models your account actually has access to
    model = st.selectbox(
        "**Model**",
        ["gpt-4o-mini", "gpt-4o", "gpt-4.1-mini", "gpt-3.5-turbo"],
        index=0,
        help="Select an available model.",
    )
    st.session_state.model = model

    length = st.radio('Length of content',
                      ['Tiny [25-45 words]', 'Small [45-80 words]', 'Medium [80-150 words]', 'Big [150-225 words]', 'Large [225+ words]'],
                      horizontal=True,
                      index=2,
                      captions=[
                          'Super small talks for a quick game',
                          'Small chunks of information, still playable',
                          'Standard size of game content',
                          'Big content for more information about the game',
                          'Very big stories for those who like to read'])

    summary_last_n = st.slider('Summarize each N step', 5, 50, 25, 1, help='Helps store history of the game in more efficient way. Reduces the amount of input tokens in API calls that leads to cheaper run. Replacing whole memory with its summary (by another LLM) each N step.') + 2

    # Get the temperature
    temp = st.slider("**Creativity**", 0.0, 1.0, 0.3, 0.05)
    st.session_state.temp = temp

    # Get the topic
    topic = st.text_input("**Topic**", placeholder="e.g., cyberpunk heist on a floating city")
    if not topic:
        st.caption("Topic cannot be empty.")
    start = st.button("**🎮 Start the Game**", use_container_width=True)
    restart = st.button("🔁 Restart", use_container_width=True, disabled=st.session_state.last_response is None)

# Start / restart flow
if start:
    if not topic.strip():
        st.warning("Please enter a topic to start.")
    else:
        reset(topic, length)
        st.rerun()

if restart:
    # full reset
    for key in ["memory", "step", "last_response", "model", "temp"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# ------------- Render current step -------------
response = st.session_state.last_response
if response is None:
    st.info("Enter a topic in the sidebar and click **Start the Game** to begin.")
    st.stop()

st.write(f"### Step {st.session_state.step + 1}")
st.write(response.game_content)

# ------------- Choices (one-step loop) -------------
# Give every button a unique, stable key tied to the current step
for idx, choice in enumerate(response.choices):
    if st.button(choice, key=f"choice_{st.session_state.step}_{idx}", use_container_width=True):
        add_memory("human", f"I choose: {choice}", st.session_state.memory)

        st.session_state.step += 1
        st.session_state.last_response = play(
            st.session_state.model, st.session_state.temp, st.session_state.memory, summary_last_n, length
        )

        st.rerun()
