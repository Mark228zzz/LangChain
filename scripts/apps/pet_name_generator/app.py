import streamlit as st
from backend import generate_name, NO_TEMPERATURE_MODELS

st.title('Pet Name Generator')

model = st.sidebar.selectbox('Select the AI model', ('gpt-3.5-turbo', 'gpt-4o', 'gpt-4o-mini'))

animal = st.sidebar.text_area('**Type of animal your pet?**')
if not animal: st.sidebar.warning('**Please enter the type of your pet**')

color = st.sidebar.text_area('**Color of your pet?**')
if not color: st.sidebar.warning('**Please enter the color of your pet**')

prefference = st.sidebar.text_area('**Any prefferences/thoughts? (Optional)**')

n_names = st.sidebar.slider('**Number of names**', 1, 10, 5, 1)

temp = 0.0
if model not in NO_TEMPERATURE_MODELS: temp = st.sidebar.slider('**Creativity**', 0.0, 1.5, 0.9)

button = st.sidebar.button('**Generate**')

if button:
    names = generate_name(animal, color, prefference, n_names, temp, model)

    st.write(f'{names}')
