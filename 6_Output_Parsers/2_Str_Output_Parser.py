from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# 1st prompt -> detailed report
template_1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summary
template_2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template_1 | model | parser | template_2 | model | parser
result = chain.invoke({"topic":"Black Hole"})

print(result)