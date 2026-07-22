import streamlit as st
import ollama

# Page config
st.set_page_config(
    page_title="Kimi 2.5 Chat (Ollama)",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Kimi 2.5 – Local Chat")
st.caption("Powered by Ollama • Fully Offline • Streaming")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response (streaming)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        stream = ollama.chat(
            model="kimi-k2.5:cloud",
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                token = chunk["message"]["content"]
                full_response += token
                placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })
