from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()
# model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class FeedBack(BaseModel):

    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")

parser_1 = StrOutputParser()
parser_2 = PydanticOutputParser(pydantic_object=FeedBack)

prompt_1 = PromptTemplate(
    template="Clasify the sentiment of the following feedback text into positive or negative \n{feedback} \n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser_2.get_format_instructions()}
)

classifier_chain = prompt_1 | model | parser_2

prompt_2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n{feedback}",
    input_variables=["feedback"]
)

prompt_3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n{feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt_2 | model | parser_1),
    (lambda x:x.sentiment == "negative", prompt_3 | model | parser_1),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain
result = chain.invoke({"feedback":"The car is looking very sexy and i like all the features of the car"})

print(result)
print(chain.get_graph().print_ascii())