import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

print("SCRIPT STARTED")

# -----------------------------
# Persistent directory
# -----------------------------
persist_dir = "10_RAG/4_Retrievers/faiss_db_2"
os.makedirs(persist_dir, exist_ok=True)

# If you want fresh DB each run
import shutil
if os.path.exists(persist_dir):
    shutil.rmtree(persist_dir)
    os.makedirs(persist_dir, exist_ok=True)
    print("Old FAISS DB deleted")

# -----------------------------
# Sample documents
# -----------------------------
documents = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="FAISS is a vector database optimized for similarity search."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# -----------------------------
# Initialize Embedding Model
# -----------------------------
print("Creating embedding model...")
embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

# -----------------------------
# Create or Load FAISS Vector Store
# -----------------------------
faiss_index_path = os.path.join(persist_dir, "faiss_index_2")

if os.path.exists(faiss_index_path):
    print("Loading existing FAISS vector store...")
    vectorstore = FAISS.load_local(
        faiss_index_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )
else:
    print("Creating new FAISS vector store...")
    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )
    vectorstore.save_local(faiss_index_path)

print("Vector store ready!")
print("Stored document count:", len(vectorstore.docstore._dict))

# -----------------------------
# Create Retriever
# -----------------------------
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 3, "lambda_mult": 0.5})

query = "What is LangChain?"

print("\nRunning retriever...")
retriever_results = retriever.invoke(query)

print("Retriever Results Count:", len(retriever_results))

for i, doc in enumerate(retriever_results, 1):
    print(f"\n--- Retriever Result {i} ---")
    print(doc.page_content)

