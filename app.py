from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

pdf_loader = PyPDFLoader("data/sample.pdf")
pdf_docs = pdf_loader.load()

text_loader = TextLoader("data/notes.txt")
text_docs = text_loader.load()

web_loader = WebBaseLoader(
    web_paths=[
        "https://python.langchain.com/docs/introduction/",
        "https://python.langchain.com/docs/concepts/rag/"
    ]
)

web_docs = web_loader.load()

all_docs = pdf_docs + text_docs + web_docs
print("documents loaded")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(all_docs)

print(f"Total Chunks: {len(chunks)}")
print("documents split into chunks")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("embeddings model loaded")

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)
print("vectorstore created and retriever set up")

llm = ChatOpenRouter(
    model="openai/gpt-3.5-turbo",
    temperature=0.7
)

print("LLM loaded")

chat_history = []

prompt = ChatPromptTemplate.from_template(
    """You are a helpful AI assistant.
Use the following context to answer the question.
Chat History:{chat_history}
Context:{context}
Question: {question}""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
        "chat_history": lambda x: "\n".join(chat_history)
    }
    | prompt | llm | StrOutputParser()
)

print("\nRAG Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    try:
        result = rag_chain.invoke(question)
        print("\nBot:", result)
        print()

        chat_history.append(f"User: {question}")
        chat_history.append(f"Bot: {result}")
        
    except Exception as e:
        print("ERROR:", e)