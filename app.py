import streamlit as st
from rag_chain import create_rag_chain
from intents import classify_intent
import openai
import os
from dotenv import load_dotenv
load_dotenv()


# Set your OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")


st.title("🛠️ IT Support Chatbot")

user_input = st.text_input("Ask your technical support question:")

if user_input:
    # Classify intent
    intent = classify_intent(user_input)
    st.markdown(f"**Detected Issue Type:** `{intent}`")

    # Run RAG pipeline
    rag = create_rag_chain()
    result = rag.run(user_input)

    st.markdown("### 🧠 Support Bot Answer:")
    st.write(result)
