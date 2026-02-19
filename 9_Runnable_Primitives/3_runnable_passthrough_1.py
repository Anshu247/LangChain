from langchain_core.runnables import RunnablePassthrough

pass_through = RunnablePassthrough()
print(pass_through.invoke({"name":"professor"}))