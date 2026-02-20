from langchain_community.document_loaders import PyPDFLoader ,DirectoryLoader

loader = DirectoryLoader(
    path="10_RAG/1_Document_Loaders/PDFs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

def docs_loader(docs):
    for document in docs:
        print(document.metadata)

docs_1 = loader.load()
docs_2 = loader.lazy_load()

print("Load: ", docs_loader(docs_1))
print("-"*100)
print("Lazy Load: ", docs_loader(docs_2))
print("-"*100)
