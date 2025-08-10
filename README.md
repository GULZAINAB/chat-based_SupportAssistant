#  RAG — Chat-based IT Support Assistant

A chat-based support assistant using **Retrieval-Augmented Generation (RAG)** to provide professional IT support solutions. The system combines rule-based intent classification with AI-powered knowledge retrieval for accurate technical assistance.

##  Technology Stack

- **Frontend**: Streamlit
- **AI/LLM**: Google Gemini 2.0 Flash Lite
- **Embeddings**: Google Text Embedding 004
- **Vector Database**: FAISS
- **Framework**: LangChain
- **Language**: Python

##  Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup Environment**
   Create `.env` file:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Run Application**
   ```bash
   streamlit run app.py
   ```

## 📖 Sample Input/Output

### Wi-Fi Issue
**Input:** `My Wi-Fi isn't working`
**Output:** Network Issue detection + 5-step troubleshooting guide

### System Restart  
**Input:** `My laptop is frozen`
**Output:** General Support detection + restart/force shutdown instructions

### Date/Time Settings
**Input:** `How to change time and date`
**Output:** System Settings detection + Windows settings guide

### Out of Scope
**Input:** `What's the weather today?`
**Output:** Polite "I don't have that information" response

##  Intent Categories

- Network Issue
- System Restart  
- System Settings
- Browser/Cache
- Drivers/Updates
- General Support

##  Project Structure

```
├── app.py              # Main Streamlit app
├── rag_chain.py        # RAG pipeline
├── intents.py          # Intent classification
├── requirements.txt    # Dependencies
├── .env                # Environment variables (make sure to include ur env file containing your Api)
└── knowledge_base/     # support_docs
```
