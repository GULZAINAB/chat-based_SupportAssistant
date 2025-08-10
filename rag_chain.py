# rag_chain.py
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# Community packages
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

INDEX_DIR = "faiss_index"

# Build FAISS index from local file
def build_vectorstore_from_file(filepath="knowledge_base/support_docs.txt", embeddings=None):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=50)
    chunks = splitter.split_text(content)
    documents = [Document(page_content=c) for c in chunks]

    if embeddings is None:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")  # ✅ updated

    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save locally so future runs don’t rebuild
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR, exist_ok=True)
    vectorstore.save_local(INDEX_DIR)
    return vectorstore

# Load FAISS index or rebuild
def load_or_build_vectorstore(filepath="knowledge_base/support_docs.txt"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")  # ✅ updated

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

    llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-lite-001", temperature=1.0)  # ✅ updated

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain
