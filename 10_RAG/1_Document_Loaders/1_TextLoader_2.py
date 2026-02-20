from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Write a summary for the following text \n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

loader = TextLoader("10_RAG/1_Document_Loaders/ai.txt", encoding="utf-8")
docs = loader.load()

chain = prompt | model | parser
result = chain.invoke({"text":docs[0].page_content})

print("Result:", result)
