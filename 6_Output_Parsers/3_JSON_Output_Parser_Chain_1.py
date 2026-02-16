from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n{format_instruction}",
    input_variabels=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({})

print(f"Result: {result}")
print(f"Result: {result['person']['name']}")
print(f"Type: {type(result)}")