from langchain_text_splitters import CharacterTextSplitter

text = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines capable of performing tasks that typically require human intelligence. These tasks include learning from data, recognizing patterns, understanding natural language, solving problems, and making decisions.

AI systems are powered by algorithms and large amounts of data. One of the most important subfields of AI is Machine Learning (ML), where models are trained on data to improve their performance over time without being explicitly programmed. Deep Learning, a subset of Machine Learning, uses neural networks with multiple layers to process complex data such as images, speech, and text.

There are different types of Artificial Intelligence. Narrow AI is designed to perform specific tasks, such as voice assistants, recommendation systems, or spam filters. General AI, which is still theoretical, would have the ability to understand and learn any intellectual task that a human can perform. Superintelligent AI refers to a level of intelligence that surpasses human intelligence in all aspects.

AI is widely used in various industries. In healthcare, it helps in disease diagnosis and drug discovery. In finance, AI systems detect fraudulent transactions and automate trading. In transportation, AI powers self-driving cars. In customer service, chatbots and virtual assistants provide 24/7 support.

Despite its benefits, AI also raises ethical concerns. Issues such as data privacy, bias in algorithms, job displacement, and accountability need careful consideration. Responsible AI development focuses on fairness, transparency, and safety.

In the future, Artificial Intelligence is expected to continue transforming industries and daily life. As technology advances, AI will become more integrated into society, making systems smarter, faster, and more efficient.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)
print(result)