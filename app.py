# app.py
import os
import streamlit as st
from dotenv import load_dotenv  # <-- NEW
from intents import classify_intent
from rag_chain import create_rag_qa_chain

# --- Load environment variables from .env ---
load_dotenv()  # <-- This loads GOOGLE_API_KEY from your .env file

st.set_page_config(page_title="Gemini RAG IT Support", layout="centered")
st.title(" RAG — Chatbased Support Assistant")

# --- Environment checks ---
if not os.getenv("GOOGLE_API_KEY"):
    st.warning("GOOGLE_API_KEY is not set. Set it in your .env file or environment before running the app.")
    st.stop()

# Load or build vectorstore once
with st.spinner("Loading knowledge base..."):
    qa_chain = create_rag_qa_chain()

query = st.text_input("Describe your issue (e.g., 'My Wi-Fi isn't working'):")

if query:
    intent = classify_intent(query)
    st.markdown(f"**Detected intent:** `{intent}`")

    with st.spinner("Generating answer..."):
        try:
            answer = qa_chain.invoke(query)
        except Exception as e:
            st.error(f"Error generating response: {e}")
            answer = None

    if answer:
        st.markdown("### Support Answer")
        st.write(answer)
        st.markdown("---")
        st.info("If the answer didn't solve your problem, try adding details (OS, device model, error messages).")
