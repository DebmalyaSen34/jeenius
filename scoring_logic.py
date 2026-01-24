import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_scoring_llm():
    api_key = os.getenv("GEMINI_API_KEY")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0, # Low temperature for consistent, logical scoring
        google_api_key=api_key
    )

def analyze_severity(question_text, correct_answer, user_wrong_answer, solution_logic):
    """
    Analyzes a wrong answer and assigns a severity score (1-5).
    """
    
    template = """
    You are an expert Physics Examiner. A student answered a question incorrectly.
    Your job is to determine the SEVERITY of the error on a scale of 1 to 5.

    QUESTION: {question}
    CORRECT ANSWER: {correct_answer}
    STUDENT'S WRONG ANSWER: {user_answer}
    SOLUTION LOGIC: {logic}

    SEVERITY SCALE:
    1 = Silly calculation error or typo. Concept is clearly understood.
    2 = Minor recall error (e.g., forgot a constant).
    3 = Moderate error. Used correct formula but wrong values/assumptions.
    4 = Significant conceptual gap. Wrong formula or approach.
    5 = Complete misunderstanding. Guesswork or unrelated answer.

    TASK:
    Output ONLY a single integer (1-5) representing the severity.
    """

    prompt = ChatPromptTemplate.from_template(template)
    llm = get_scoring_llm()
    chain = prompt | llm

    # We invoke the chain
    response = chain.invoke({
        "question": question_text,
        "correct_answer": correct_answer,
        "user_answer": user_wrong_answer,
        "logic": solution_logic
    })

    # Clean up the response to ensure we just get the number
    try:
        score = int(str(response.content.strip()))
        return score
    except ValueError:
        return 3 # Default to medium severity if LLM output is weird

if __name__ == "__main__":
    # --- TEST CASE ---
    q = "What is the unit of Force?"
    correct = "Newton"
    
    # Test 1: Silly mistake
    wrong_1 = "Newtons" 
    print(f"Answer: '{wrong_1}' -> Severity: {analyze_severity(q, correct, wrong_1, 'Standard SI unit')}")

    # Test 2: Conceptual mistake
    wrong_2 = "Joules"
    print(f"Answer: '{wrong_2}' -> Severity: {analyze_severity(q, correct, wrong_2, 'Standard SI unit')}")