# rag_chain.py
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

INDEX_DIR = "faiss_index"

# Build FAISS index
def build_vectorstore_from_file(filepath="knowledge_base/support_docs.txt", embeddings=None):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=50)
    chunks = splitter.split_text(content)
    documents = [Document(page_content=c) for c in chunks]

    if embeddings is None:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    vectorstore = FAISS.from_documents(documents, embeddings)
    
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR, exist_ok=True)
    vectorstore.save_local(INDEX_DIR)
    return vectorstore

# Load FAISS index or rebuild
def load_or_build_vectorstore(filepath="knowledge_base/support_docs.txt"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")  

    if os.path.exists(INDEX_DIR):
        try:
            vs = FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
            return vs
        except Exception:
            pass  # If load fails, rebuild

    return build_vectorstore_from_file(filepath, embeddings=embeddings)

# Create the RAG QA chain
def create_rag_qa_chain():
    vectorstore = load_or_build_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash-lite-001", 
        temperature=0.3
    )  

    # Instruction template
    template = """You are a helpful IT support assistant with access to a knowledge base.

Instructions:
- Answer the user's question in a respectful, polite, and professional tone
- Do not use slang or casual expressions
- Provide clear, step-by-step instructions when applicable
- Use proper formatting with numbered lists or bullet points for better readability
- If the answer cannot be found in the provided context, politely say: "I'm sorry, but I do not have the necessary information to answer that question. Iam still learning"
- Do not make up facts or provide information not supported by the context
- If the user's question is in a different language, reply in that same language respectfully

Context: {context}

Question: {question}

Answer:"""

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa_chain