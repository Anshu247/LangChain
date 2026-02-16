from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
document = [
    "I Love Cars",
    "I Love to do travel"
]

vector = embedding.embed_documents(document)
print(str(vector))
