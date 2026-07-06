import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -----------------------------
# Replace with your NEW Gemini API Key
# -----------------------------
GOOGLE_API_KEY = "AQ.Ab8RN6KGrKA_mvCNi3tpeOGq-DtReJAVe3f_BnWSLy6Zu8OVjw"

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖"
)

st.title("🤖 Gemini Chatbot")

# -----------------------------
# Prompt Template
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. Answer user questions clearly and accurately."
    ),
    (
        "user",
        "Question: {question}"
    )
])

# -----------------------------
# Gemini Model
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2,
    max_output_tokens=1024,
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_input("Ask your question:")

if st.button("Submit") and user_input:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke(
                {"question": user_input}
            )
            st.success(response)

        except Exception as e:
            st.error(f"Error: {e}")