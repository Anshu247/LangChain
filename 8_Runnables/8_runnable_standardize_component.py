from abc import ABC, abstractmethod
import random

class Runnable(ABC):

  @abstractmethod
  def invoke(input_data):
    pass

class LLMDemo(Runnable):

    def __init__(self):

        print("LLM Created")
    
    def invoke(self, prompt):

        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
    
        return {"response": random.choice(response_list)}
    
    def predict(self, prompt):
        
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
    
        return {"response": random.choice(response_list)}

class PromptTemplateDemo(Runnable):

    def __init__(self, template, input_variables):

        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, input_dict):

        return self.template.format(**input_dict)

    def format(self, input_dict):

        return self.template.format(**input_dict)

class RunnableConnector(Runnable):

    def __init__(self, runnable_list):

        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        
        return input_data

class StrOutputParser(Runnable):

    def __init__(self):
        pass

    def invoke(self, input_data):

        return input_data["response"]

template_1 = PromptTemplateDemo(
    template = "Write a {length} poem about {topic}",
    input_variables = ["length","topic"]
)

llm_1 = LLMDemo()
chain_1 = RunnableConnector([template_1, llm_1])

result_1 = chain_1.invoke({"length":"long","topic":"Artificial Intelligence"})
print("Result 1:", result_1)

parser = StrOutputParser()

chain_2 = RunnableConnector([template_1, llm_1, parser])

result_2 = chain_2.invoke({"length":"long","topic":"Artificial Intelligence"})
print("Result 2:", result_2)

# connecting 2 chains and make a new chain

template_2 = PromptTemplateDemo(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

template_3 = PromptTemplateDemo(
    template="Explain the following joke {response}",
    input_variables=["response"]
)

chain_3 = RunnableConnector([template_2, llm_1])
chain_4 = RunnableConnector([template_3, llm_1, parser])

final_chain = RunnableConnector([chain_3, chain_4])
result_3 = final_chain.invoke({"topic":"Robots"})

print("Result 3:", result_3)

