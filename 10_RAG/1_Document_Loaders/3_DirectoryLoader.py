from langchain_community.document_loaders import PyPDFLoader ,DirectoryLoader

loader = DirectoryLoader(
    path="10_RAG/1_Document_Loaders/PDFs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print("Docs:", docs)
print("-"*100)
print("Length:", len(docs))
print("-"*100)
print("Page Content:", docs[0].page_content)
print("-"*100)
print("Meta Data:", docs[0].metadata)
print("-"*100)
