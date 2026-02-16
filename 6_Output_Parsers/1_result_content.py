from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt_1 = template_1.invoke({"topic":"Black Hole"})
result_1 = model.invoke(prompt_1)

prompt_2 = template_2.invoke({"text":result_1.content[0]["text"]})
result_2 = model.invoke(prompt_2)

print(result_2.content[0]["text"])