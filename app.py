import os
import streamlit as st
from dotenv import load_dotenv
from intents import classify_intent
from rag_chain import create_rag_qa_chain

load_dotenv() 

st.set_page_config(page_title="Gemini RAG IT Support", layout="centered")
st.title("RAG — Chat-based IT Support Assistant")

if not os.getenv("GOOGLE_API_KEY"):
    st.warning("GOOGLE_API_KEY is not set. Set it in .env file or environment before running the app.")
    st.stop()

#vectore score
with st.spinner("Loading knowledge base..."):
    qa_chain = create_rag_qa_chain()

query = st.text_input("Describe your issue (e.g., 'My Wi-Fi isn't working'):")

if query:
    # Intent detection
    intent = classify_intent(query)
    st.markdown(f"**Detected intent :** `{intent}`")
    # Answer generation
    with st.spinner("Generating answer..."):
        try:
            response = qa_chain.invoke({"query": query})
            answer = response.get("result", "").strip() if isinstance(response, dict) else response
        except Exception as e:
            st.error(f"Error generating response: {e}")
            answer = None

    if answer:
        st.markdown("### Solution")
        st.write(answer)
        st.markdown("---")
