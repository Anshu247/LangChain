import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever  # ✅ Fixed!
from langchain_classic.retrievers.document_compressors import LLMChainExtractor 
from langchain_core.documents import Document

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

print("SCRIPT STARTED")

# -----------------------------
# Persistent directory
# -----------------------------
persist_dir = "10_RAG/4_Retrievers/faiss_db_4"
os.makedirs(persist_dir, exist_ok=True)

# If you want fresh DB each run
import shutil
if os.path.exists(persist_dir):
    shutil.rmtree(persist_dir)
    os.makedirs(persist_dir, exist_ok=True)
    print("Old FAISS DB deleted")

# Sample Documents Objects
documents = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
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
faiss_index_path = os.path.join(persist_dir, "faiss_index_4")

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
# Create Base Retriever
# -----------------------------
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# ------------------------------------
# Set up the compressor using an LLM
# ------------------------------------
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
compressor = LLMChainExtractor.from_llm(llm)

# ---------------------------------------------
# Create the contextual compression retriever
# ---------------------------------------------
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Query the retriever
query = "What is photosynthesis?"
compressed_results = compression_retriever.invoke(query)

# Printing Results
print("\nRunning retriever...")

for i, doc in enumerate(compressed_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
