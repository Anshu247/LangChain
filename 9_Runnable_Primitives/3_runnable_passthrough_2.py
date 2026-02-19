from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt_1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template="Explain the following joke {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt_1, model, parser)
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt_2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic":"Robots"})

print("Result:", result,"\n")
print("-"*100)
print("Joke:", result["joke"],"\n")
print("-"*100)
print("Explanation:", result["explanation"],"\n")