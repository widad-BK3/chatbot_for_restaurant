from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Get the directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Load CSV relative to this file
df = pd.read_csv(os.path.join(BASE_DIR, "realistic_restaurant_reviews.csv"))

# df = pd.read_csv("C:\\Users\\dell\\Desktop\\env3\\prj1\\realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large", base_url="http://host.docker.internal:11434")
# embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)