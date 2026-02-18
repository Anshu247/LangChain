from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

load_dotenv()

# Initialize the LLM
llm = GoogleGenerativeAI(model="gemini-2.5-flash")

# Create a Prompt Template
prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"] # Define what input is needed
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with a specific topic
topic = input("Enter a topic: ")
output = chain.invoke({"topic":topic})["text"]

# Print the output
print("Generated Blog Title:", output)