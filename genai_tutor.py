import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load your API key
load_dotenv()

DB_PATH = "faiss_index"

def get_tutor_llm():
    """Initializes the Gemini model via LangChain."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    
    # We use the specific model you requested
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,
        google_api_key=api_key
    )

def generate_intervention(failed_question_text: str, user_wrong_answer: str):
    print(f"\n--- 1. Diagnosing Failure for: '{failed_question_text[:30]}...' ---")
    
    # Step A: Load the Knowledge Base
    # We use the same embedding model we used to build the index
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Allow dangerous deserialization is required for local FAISS files
    vector_db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

    # Step B: RETRIEVAL - Find the relevant physics concept
    print("Searching Knowledge Base...")
    results = vector_db.similarity_search(failed_question_text, k=1)
    
    if not results:
        return "Error: Could not find relevant theory for this question."

    retrieved_chunk = results[0]
    concept_name = retrieved_chunk.metadata['concept_tag']
    print(f"Found relevant concept: {concept_name}")
    
    # Step C: AUGMENTATION - Create the Prompt
    # We feed the retrieved theory (context) into the prompt
    template = """
    You are an expert JEE Physics Tutor. A student just failed a question.
    
    RELEVANT PHYSICS THEORY (From Knowledge Base):
    {context}
    
    THE FAILED QUESTION:
    {question}
    
    STUDENT'S WRONG ANSWER:
    {student_answer}
    
    YOUR TASK:
    1. Diagnosis: Explain the likely conceptual mistake based on the wrong answer.
    2. Micro-Lesson: Explain the correct concept using the THEORY provided above.
    3. Bridge Question: Create a NEW, similar but simpler numerical question to test this concept. Provide the solution logic but hide the final answer.
    
    Keep your response encouraging but concise.
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    llm = get_tutor_llm()

    # Step D: GENERATION - Chain it all together
    chain = prompt | llm

    print("--- 2. Generating Tutor Response ---")
    response = chain.invoke({
        "context": retrieved_chunk.page_content,
        "question": failed_question_text,
        "student_answer": user_wrong_answer
    })

    return response.content

if __name__ == "__main__":
    # --- TEST RUN ---
    # Let's simulate a student getting a projectile motion question wrong
    test_question = "A ball is thrown at 30 degrees. What is the vertical acceleration at the highest point?"
    test_wrong_answer = "Zero, because velocity is zero."

    result = generate_intervention(test_question, test_wrong_answer)

    print("\n" + "="*40)
    print("GENAI TUTOR OUTPUT")
    print("="*40)
    print(result)