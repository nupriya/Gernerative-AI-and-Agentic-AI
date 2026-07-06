import os 
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 


# set up the api key for both gemini api key & langcmith api key 

os.environ["GOOGLE_API_KEY"] = 'AIzaSyAuKq5x8ww_ATN72bk47W3F39NGvnhUWQ0' 

os.environ["LANGSMITH_TRACING_V2"] = 'true'

os.environ["LANGSMITH_API_KEY"] = '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'

# PROMPT TEMPLATE

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a chatbot which assistant to the world about the latest news."),
        ("human", "{question}")
    ]
)

st.title('Gemini chat model with langchain created by Nupriya Saxena')
input_text = st.text_input('How may i help you today ? if your write one word then I am Hallucinate') 

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1, max_output_tokens=2000)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    with st.spinner('Generating response...'):
        try:
            response = chain.invoke({'question': input_text})
            st.success('Response generated successfully!')
            st.write(response)

        except Exception as e:
            st.error(f'An error occurred: {e}') 






