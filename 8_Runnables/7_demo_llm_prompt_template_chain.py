import random

class LLMDemo:

    def __init__(self):

        print("LLM Created")
    
    def predict(self, prompt):
        
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
    
        return {"response": random.choice(response_list)}

class PromptTemplateDemo:

    def __init__(self, template, input_variables):

        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):

        return self.template.format(**input_dict)

class ChainDemo:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):

        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']

template_1 = PromptTemplateDemo(
    template = "Write a {length} poem about {topic}",
    input_variables = ["length","topic"]
)

prompt = template_1.format({"length":"short","topic":"Super Massive Black Holes"})

llm_1 = LLMDemo()
result_1 = llm_1.predict(prompt)

print("Result 1", result_1)

template_2 = PromptTemplateDemo(
    template = "Write a {length} poem about {topic}",
    input_variables = ["length","topic"]
)

llm_2 = LLMDemo()

chain = ChainDemo(llm_2, template_2)
result_2 = chain.run({"length":"short","topic":"cars"})

print("Result 2:", result_2)