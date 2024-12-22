# Install all libraries by running in the terminal: pip install -q -r ./project3-requirements.txt

# Interesting https://docs.streamlit.io/develop/concepts/design/buttons

# Run like this:  streamlit run '.\7. Project #3 - Chat with document.py'

from langchain_community.chat_models import ChatOpenAI

from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)


# loading the OpenAI api key from .env (OPENAI_API_KEY="sk-********")
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title='You Custom Assistant',
    page_icon='🤖'
)
st.subheader('Your Custom ChatGPT 🤖')

chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.5)

# creating the messages (chat history) in the Streamlit session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

