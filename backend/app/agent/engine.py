import json

from genai_tutor import generate_intervention
from scoring_logic import get_ai_score
from utils.model_init import get_model

QUESTION_FILE = 'data/processed/question_bank.json'

# Load questions once when the server starts
def load_question_bank():
    try:
        with open(QUESTION_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Question bank not found.")
        return []

QUESTION_BANK = load_question_bank()

def get_question_by_id(q_id: str):
    """Finds a question object by its ID."""
    for q in QUESTION_BANK:
        if q['id'] == q_id:
            return q
    return None

def get_next_question(current_index: int):
    """Simple logic: just get the next question in the list."""
    if current_index + 1 < len(QUESTION_BANK):
        return QUESTION_BANK[current_index + 1]
    return None

def process_answer(question_id: str, user_option_index: int):
    """
    The Core Logic: Checks answer, calculates severity, calls AI if needed.
    """
    question = get_question_by_id(question_id)
    if not question:
        return {"error": "Question not found"}

    correct_index = question['correct_option_index']
    is_correct = (user_option_index == correct_index)
    
    result = {
        "is_correct": is_correct,
        "correct_answer_text": question['options'][correct_index],
        "severity_score": 0,
        "ai_explanation": None
    }

    if not is_correct:
        # 1. Calculate Severity
        user_text = question['options'][user_option_index]
        correct_text = question['options'][correct_index]
        
        severity = get_ai_score(
            question_data=question,
            llm=get_model(model="gemini-2.5-flash", use_google=True)
        )
        result["severity_score"] = severity

        if severity >= 3:
            intervention = generate_intervention(
                question['question_text'],
                user_text
            )
            result["ai_explanation"] = intervention

    return result