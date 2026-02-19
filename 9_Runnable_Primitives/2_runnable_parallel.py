from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model_1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model_2 = ChatHuggingFace(llm=llm)

prompt_1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt_1, model_1, parser),
    "linkedin": RunnableSequence(prompt_2, model_2, parser)
})

result = parallel_chain.invoke({"Artificial Intelligence"})

print("Result:", result,"\n")
print("-"*100)
print("Tweet:", result["tweet"],"\n")
print("-"*100)
print("Linkedin:", result["linkedin"],"n")
