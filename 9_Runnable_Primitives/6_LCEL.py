from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt_1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template="Summarize the following text \n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

report_gen_chain = prompt_1 | model | parser
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, prompt_2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)
result = final_chain.invoke({"topic":"Why BTC crahsed"})

print(result)