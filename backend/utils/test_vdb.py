from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DB_PATH = "faiss_index_md"

def test_vector_store(question: str):
    print("Loading vector store...")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = FAISS.load_local(DB_PATH, embeddings=embeddings, allow_dangerous_deserialization=True)

    print("Vector store loaded successfully!")

    results = vector_db.similarity_search(question, k=3)

    for i, result in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Content: {result.page_content}")
        print(f"Metadata: {result.metadata}")
        print("-" * 50)

    print("Testing with similarity scores...\n")
    results_with_scores = vector_db.similarity_search_with_score(question, k=3)

    print("Results with similarity scores:")

    for i, (result, score) in enumerate(results_with_scores):
        print(f"Result {i + 1}:")
        print(f"Content: {result.page_content}")
        print(f"Metadata: {result.metadata}")
        print(f"Similarity Score: {score:.4f}")
        print("-" * 50)

if __name__ == "__main__":
    test_question = "What is newton's laws of motion?"
    test_vector_store(test_question)