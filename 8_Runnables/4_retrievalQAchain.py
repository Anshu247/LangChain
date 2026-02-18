from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

# Load the document
loader = TextLoader("8_Runnables/docs.txt") # Ensure docs.txt exists
documents = loader.load()

# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Convert text into embeddings and store in FAISS
vectorstore = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings(model="gemini-embedding-001"))

# Create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# Initialize the LLM
llm = GoogleGenerativeAI(model="gemini-2.5-flash")

# Create RetrievalQAChain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask a question
query = "What are the key takeaways from the document?"
answer = qa_chain.invoke(query)

# Print the Answer
print("Answer:", answer["result"])