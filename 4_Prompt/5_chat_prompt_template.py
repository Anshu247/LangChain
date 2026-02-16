from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You're a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt =  chat_template.invoke({'domain': 'Artificial Intelligence', 'topic': "Langraph"})
print(prompt)