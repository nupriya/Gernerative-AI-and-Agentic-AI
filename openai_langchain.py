from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="OpenAI Chatbot")
st.title("OpenAI Chatbot")

user_input = st.text_input("Ask your question:")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Answer the user's questions clearly and accurately."
        ),
        (
            "user",
            "{question}"
        )
    ]
)

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Generate Response
if user_input:
    response = chain.invoke(
        {
            "question": user_input
        }
    )

    st.write(response)