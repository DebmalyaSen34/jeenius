import json
import os
# We use HuggingFace for free, high-quality embeddings that run locally on your Mac
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

JSON_PATH = "data/processed/theory_corpus.json"
DB_PATH = "faiss_index"

def load_data():
    print(f"Loading theory from {JSON_PATH}...")
    if not os.path.exists(JSON_PATH):
        raise FileNotFoundError(f"Could not find {JSON_PATH}")

    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    documents = []
    for item in data:
        # We combine the concept and content into the searchable text
        page_content = f"Concept: {item['concept_tag']}\nContent: {item['content']}"
        
        metadata = {
            "chunk_id": item["chunk_id"],
            "topic": item["topic"],
            "concept_tag": item["concept_tag"]
        }
        
        doc = Document(page_content=page_content, metadata=metadata)
        documents.append(doc)

    print(f"Loaded {len(documents)} theory chunks.")
    return documents

def build_vector_store(documents):
    print("Initializing embedding model (this runs locally)...")
    # This downloads a small, fast model to your Mac to turn text into numbers
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Building FAISS index...")
    vector_db = FAISS.from_documents(documents, embeddings)

    print(f"Saving index to {DB_PATH}...")
    vector_db.save_local(DB_PATH)
    print("Success! Knowledge Base created.")

if __name__ == "__main__":
    docs = load_data()
    build_vector_store(docs)