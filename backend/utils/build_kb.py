import json
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

JSON_PATH = "theory_corpus.json"
DB_PATH = "faiss_index"

def load_data():

    print(f"Loading data from {JSON_PATH}...")

    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    documents = []

    for item in data:
        page_content = f"Topic: {item['topic']}\nConcept: {item['concept_tag']}\nContent: {item['content']}"

        metadata = {
            "chunk_id": item["chunk_id"],
            "topic": item["topic"],
            "concept_tag": item["concept_tag"]
        }

        doc = Document(page_content=page_content, metadata=metadata)
        documents.append(doc)

    print(f"Loaded {len(documents)} documents.")
    return documents

def build_vector_store(documents):
    print("Initializing embedding model...")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Building FAISS vector store...")

    vector_db = FAISS.from_documents(documents, embeddings)

    print(f"Saving vector store to {DB_PATH}...")

    vector_db.save_local(DB_PATH)
    print("Vector store saved successfully.")

if __name__ == "__main__":
    docs = load_data()
    build_vector_store(docs)