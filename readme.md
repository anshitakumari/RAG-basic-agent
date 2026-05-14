|=================|
|== RAG Chatbot ==|
|=================|

This project builds a complete AI chatbot using:
    * LangChain
    * RAG (Retrieval Augmented Generation)
    * FAISS Vector Database
    * Memory / Conversation History
    * Document Loaders
    * Text Splitters
    * Runnable Architecture
    * Chaining
    * Website Data Loading
    * PDF + TXT + Webpage Support

The chatbot will:
        * Remember previous conversations
        * Retrieve answers from documents
        * Retrieve answers from websites
        * Use vector search
        * Use semantic retrieval
        * Use LangChain runnables

# Step 1 - Create Virtual Environment
# Step 2 - Install Dependencies
bash: uv pip install langchain langchain-community langchain-openai langchain-text-splitters faiss-cpu pypdf beautifulsoup4 python-dotenv tiktoken
# Step 3 - Add API Key
# Step 4 - Create '.env'
OPENROUTER_API_KEY=your_key_here

# Step 5 - Full RAG Chatbot Code: Create 'app.py'
# Step 6 — Add Sample TXT File

Example:
        LangChain is a framework for building LLM applications.
        RAG stands for Retrieval Augmented Generation.
        FAISS is a vector database for semantic similarity search.

# Step 7 - Run the Chatbot: uv run python app.py

=============================
== What Concepts Are Used? ==
=============================

| Concept               | Used? |
| --------------------- | ----- |
| RAG                   | Yes   |
| Memory                | Yes   |
| Vector Database       | Yes   |
| FAISS                 | Yes   |
| Retrieval             | Yes   |
| Runnable Architecture | Yes   |
| Chaining              | Yes   |
| Document Loader       | Yes   |
| Text Splitter         | Yes   |
| Website Loader        | Yes   |

===================
== The FlowChart ==
===================

PDF + Website
       ↓
Document Loaders
       ↓
Text Splitter
       ↓
Chunks
       ↓
HuggingFace Embeddings
       ↓
FAISS Vector DB
       ↓
Retriever
       ↓
LLM
       ↓
Answer

========================
== What is Retrieval? ==
========================

Retrieval means:

User Question -> Search similar chunks -> Send relevant chunks to LLM

Instead of sending the whole PDF.

====================
== What is FAISS? ==
====================

FAISS:
* stores embeddings
* performs similarity search
* retrieves semantically similar chunks

Created by Meta.

=========================
== What are Runnables? ==
=========================

LangChain introduced Runnable architecture for:
        * modular pipelines
        * chaining components
        * streaming
        * async support
        * composability

Example: chain = prompt | llm | parser
Each component is a Runnable.

==========================================
== Difference Between Chain vs Runnable ==
==========================================

| Chain             | Runnable          |
| ----------------- | ----------------- |
| Older abstraction | New architecture  |
| Less flexible     | Highly composable |
| Limited streaming | Better streaming  |
| Simpler           | More powerful     |

===================================
== Recommended Next Improvements ==
===================================

1. Beginner: 
        * Streamlit UI
        * Chat history UI
        * Multiple PDFs
        * Persistent DB

2. Intermediate
        * Hybrid search
        * Metadata filtering
        * Parent document retriever
        * Multi-query retriever

3. Advanced
        * Agentic RAG
        * LangGraph
        * Tool calling
        * Reranking
        * Multi-modal RAG
        * SQL + RAG

## Common Beginner Errors

1. Wrong Package Name:

Correct: langchain-text-splitters
NOT: langchain.text_splitter

2. Empty Retrieval Results:

Causes:
        * bad chunking
        * poor embeddings
        * too large chunks
        * empty documents

====================
== Learning Order ==
====================

1. Document Loaders
2. Text Splitters
3. Embeddings
4. Vector Databases
5. Retrieval
6. Chains
7. Runnables
8. Memory
9. RAG Pipelines
10. Agents

## Final Architecture: user question -> retriever -> similar chunks -> prompt -> LLM -> final answer

## Optional Improvements

* Streamlit Frontend
* PDF Upload UI
* ChatGPT-like Interface
* Citation Support
* Source Highlighting
* Local LLM Support
* Ollama Integration
* HuggingFace Embeddings
* ChromaDB
* Pinecone
* LangSmith Tracing
* LangServe API

=====================
== ENTIRE PIPELINE ==
=====================

Documents/Websites -> Document Loaders -> Text Splitter -> Embeddings -> FAISS Vector DB -> Retriever -> Runnable RAG Pipeline -> LLM -> Answer