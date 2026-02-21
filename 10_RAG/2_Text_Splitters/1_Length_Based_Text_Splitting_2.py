from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("10_RAG/2_Text_Splitters/dl-curriculum.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=0,
    separator=''
)

def chunks(result):

    for i, chunk in enumerate(result):
        print(f"Chunk {i+1}: {chunk.page_content}\n")

result = splitter.split_documents(docs)
chunks(result)