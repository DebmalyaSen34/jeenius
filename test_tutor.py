from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DB_PATH = "faiss_index"

def retrieve_concept(query):
    print(f"-- Searching for concept: {query} --")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

    result = vector_db.similarity_search(query=query, k=2)

    for i, res in enumerate(result):
        print(f"\n[Result {i+1}]")
        print(f"Concept: {res.metadata['concept_tag']}")
        print(f"Content: {res.page_content}")

if __name__ == "__main__":
    retrieve_concept("Explain relative velocity between two moving objects.")