import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "faiss_index"

def get_tutor_llm(model: str, use_google: bool = False):
    
    if use_google:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("API key not found in environment variables.")
    
        print("Using Google Gemini LLM")
        return ChatGoogleGenerativeAI(model=model, temperature=0.3, api_key=api_key)
    
    print("Using Ollama LLM")
    return ChatOllama(model=model, temperature=0.3)

def generate_intervention(failed_question_text: str, user_wrong_answer: str):
    print("--- 1. Diagnosing Failure ---")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(DB_PATH, embeddings=embeddings, allow_dangerous_deserialization=True)

    results = vector_db.similarity_search(failed_question_text, k=1)

    if not results:
        return "Error: No relevant theory found in KB"

    retrieved_chunk = results[0]
    print(f"Debug: Retrieved Context -> {retrieved_chunk.metadata['concept_tag']}")
   
    
    template = """
        You are an expert JEE Physics Tutor. A student just failed a question.
        
        CONTEXT (From NCERT/Textbook):
        {context}
        
        THE FAILED QUESTION:
        {question}
        
        STUDENT'S WRONG ANSWER:
        {student_answer}
        
        YOUR TASK:
        1. Explain WHY the student likely got it wrong (identify the gap).
        2. Provide a 'Micro-Lesson': A short, 3-sentence explanation of the specific concept based strictly on the CONTEXT provided. Do NOT lecture on unrelated topics.
        3. Generate a 'Bridge Question': A new, simpler numerical question to test this specific concept immediately. Provide the correct answer logic but hide the final answer.
        
        OUTPUT FORMAT:
        Diagnosis: ...
        Micro-Lesson: ...
        Bridge Question: ...
        """

    prompt = ChatPromptTemplate.from_template(template)

    # What does this chain do?
    # It takes the prompt and combines it with the LLM to generate a response.
    # The | operator is used to chain the prompt with the LLM.
    chain = prompt | get_tutor_llm(model="llama3.1:latest", use_google=False)

    print("--- 2. Generating Personal Tutor Response ---")
    response = chain.invoke({
        "context": retrieved_chunk.page_content,
        "question": failed_question_text,
        "student_answer": user_wrong_answer
    })

    return response.content