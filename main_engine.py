# The Workflow we will code:
# Serve Question: Show a question from questions.json.
# Get Answer: Ask the user (you, in the terminal) for an answer.
# Check: Compare with the correct answer.
# Branching:
# If Correct: "Great! Confidence increased. Moving to next hard question."
# If Wrong: STOP. Trigger genai_tutor.py. Show the Micro-Lesson.

import os
import json
from genai_tutor import generate_intervention

def load_questions(file_path: str):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Questions file not found: {file_path}")    

    with open(file_path, 'r') as f:
        return json.load(f)
    
def show_question(question_data: dict):
    print("\nQuestion:")
    print(question_data['question_text'])
    print("\nOptions:")
    for idx, option in enumerate(question_data['options']):
        print(f"{idx + 1}. {option}", end=' ')
    user_answer = int(input("Your Answer: "))
    return user_answer

def check_answer(user_answer: int, correct_answer: int):
    return user_answer == correct_answer

def main():
    QUESTION_FILE = 'books/hc_verma_kinematics_questions.json'

    print(f"Loading questions from {QUESTION_FILE}...")
    questions = load_questions(QUESTION_FILE)
    print("Questions loaded successfully.")

    for idx, question_data in enumerate(questions):
        user_answer = show_question(question_data)
        if check_answer(user_answer=(user_answer-1), correct_answer=question_data['correct_option_index']):
            print("Great! Confidence increased. Moving to next hard question.")
        else:
            print("Incorrect answer. Triggering micro-lesson...")
            explanation = generate_intervention(failed_question_text=question_data['question_text'], user_wrong_answer=question_data['options'][user_answer - 1])
            print("\n--- Micro-Lesson ---")
            print(explanation)
            break  # Stop after the first incorrect answer

if __name__ == "__main__":
    main()