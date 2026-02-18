from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Initialize the LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a Prompt Template
prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

# Define the input
topic = input("Enter a topic: ")

# Format the prompt manaually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

# Call the LLM directly
blog_title = llm.predict(formatted_prompt)

# Print the output
print("Generated Blog Title:", blog_title)