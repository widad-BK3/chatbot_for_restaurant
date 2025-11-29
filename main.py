# from langchain_ollama.llms import OllamaLLM
# from langchain_core.prompts import ChatPromptTemplate
# from vector import retriever

# model = OllamaLLM(model="llama3.2")

# template = """
# You are an exeprt in answering questions about a pizza restaurant

# Here are some relevant reviews: {reviews}

# Here is the question to answer: {question}
# """
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

# while True:
#     print("\n\n-------------------------------")
#     question = input("Ask your question (q to quit): ")
#     print("\n\n")
#     if question == "q":
#         break
    
#     reviews = retriever.invoke(question)
#     result = chain.invoke({"reviews": reviews, "question": question})
#     print(result)

# ___________________________________________________________________________________________
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import os 

# get the base URL from environment (set in docker-compose)
BASE_URL = os.getenv("BASE_URL", "http://host.docker.internal:11434")

# --- Step 2: Initialize LLM with CPU client ---
model = OllamaLLM(model="llama3.2:latest", base_url=BASE_URL, device="cpu")

# --- Step 3: Prepare prompt and chain ---
template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# --- Function to call from UI ---
def ask_question(question):
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    return result

# --- CLI testing ---
if __name__ == "__main__":
    while True:
        print("\n\n-------------------------------")
        question = input("Ask your question (q to quit): ")
        if question == "q":
            break
        print(ask_question(question))
