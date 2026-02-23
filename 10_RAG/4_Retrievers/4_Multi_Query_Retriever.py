import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

print("SCRIPT STARTED")

# -----------------------------
# Persistent directory
# -----------------------------
persist_dir = "10_RAG/4_Retrievers/faiss_db_3"
os.makedirs(persist_dir, exist_ok=True)

# If you want fresh DB each run
import shutil
if os.path.exists(persist_dir):
    shutil.rmtree(persist_dir)
    os.makedirs(persist_dir, exist_ok=True)
    print("Old FAISS DB deleted")

# Relevant health & wellness documents
documents = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
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
faiss_index_path = os.path.join(persist_dir, "faiss_index_3")

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
# Create Similarity Retriever
# -----------------------------
similarity_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# -----------------------------
# Create Similarity Retriever
# -----------------------------
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
)

# Query
query = "How to improve energy level and maintain balance?"

# Retrieve results
similarity_results = similarity_retriever.invoke(query)
multiquery_results= multiquery_retriever.invoke(query)

# Printing Results
print("\nRunning retriever...")

for i, doc in enumerate(similarity_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

print("*"*100)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)