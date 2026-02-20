from langchain_community.document_loaders import WebBaseLoader

url = "https://docs.langchain.com/oss/python/integrations/document_loaders"
loader = WebBaseLoader(url)

docs = loader.load()

print("Docs:", docs)
print("-"*100)
print("Length:", len(docs))
print("-"*100)
print("Page Content:", docs[0].page_content)
print("-"*100)
print("Meta Data:", docs[0].metadata)
print("-"*100)