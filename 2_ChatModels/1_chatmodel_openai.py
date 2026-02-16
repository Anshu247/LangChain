from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.7, max_completion_tokens=70)
result = model.invoke("Write 7 lines about Artificial Intelligence")

print(result.content)