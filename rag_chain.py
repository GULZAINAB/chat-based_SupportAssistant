from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

def load_vectorstore():
    with open("knowledge_base/support_docs.txt", "r") as f:
        content = f.read()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs = text_splitter.split_text(content)
    documents = [Document(page_content=d) for d in docs]

    openai_key = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)  
    vectorstore = FAISS.from_documents(documents, embeddings)

    return vectorstore

def create_rag_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever()

    openai_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(openai_api_key=openai_key, temperature=0)  

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
