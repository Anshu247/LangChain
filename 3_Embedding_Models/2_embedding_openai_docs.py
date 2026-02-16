from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
document = [
    "I Love Cars",
    "I Love to do travel"
]

result = embedding.embed_documents(document)
print(str(result))