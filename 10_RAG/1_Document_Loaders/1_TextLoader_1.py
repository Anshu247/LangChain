from langchain_community.document_loaders import TextLoader

loader = TextLoader("10_RAG/1_Document_Loaders/ai.txt", encoding="utf-8")
docs = loader.load()

print("Docs:", docs,"\n")
print("-"*100)
print("Type: ", type(docs),"\n")
print("-"*100)
print("Length:", len(docs),"\n")
print("-"*100)
print("Docs[0]:", docs[0],"\n")
print("-"*100)
print("Type of Docs[0]:", type(docs[0]),"\n")
print("-"*100)
print("Page Content:", docs[0].page_content,"\n")
print("-"*100)
print("Meta Data:", docs[0].metadata,"\n")
print("-"*100)
