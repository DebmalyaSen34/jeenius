import json
import time
from genai_tutor import generate_intervention
from scoring_logic import analyze_severity

QUESTION_FILE = 'data/processed/question_bank.json'

def load_questions():
    """Loads questions from the JSON file."""
    try:
        with open(QUESTION_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {QUESTION_FILE}. Did you create it?")
        return []

def ask_question(q_data):
    """Displays a question and gets the user's choice."""
    print("\n" + "="*60)
    print(f"TOPIC: {q_data['sub_concept']}")
    print(f"DIFFICULTY: {q_data['difficulty_level']}")
    print("-" * 60)
    print(f"Q: {q_data['question_text']}")
    print("-" * 60)
    
    for i, option in enumerate(q_data['options']):
        print(f"  {i+1}. {option}")
    
    print("\n")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice - 1 # Convert to 0-based index
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to JEE-AI Coach (Terminal Version)")
    print("Loading questions...")
    questions = load_questions()
    
    if not questions:
        return

    score = 0
    
    for q in questions:
        user_choice = ask_question(q)
        correct_choice = q['correct_option_index']
        
        if user_choice == correct_choice:
            print("\n✅ CORRECT! Great job.")
            score += 1
            time.sleep(1) # Short pause for effect
        else:
            print("\n❌ INCORRECT.")
            
            # --- STEP 1: AI SCORING ---
            print("Thinking... (Analyzing mistake severity)")
            
            user_wrong_answer_text = q['options'][user_choice]
            correct_answer_text = q['options'][correct_choice]
            
            severity = analyze_severity(
                question_text=q['question_text'],
                correct_answer=correct_answer_text,
                user_wrong_answer=user_wrong_answer_text,
                solution_logic=q['solution_logic']
            )
            
            print(f"Severity Score: {severity}/5")
            
            # --- STEP 2: ADAPTIVE LOGIC ---
            if severity >= 3:
                print("\n⚠️  Significant conceptual gap detected.")
                print("Calling AI Tutor for a micro-lesson...")
                
                # Call the RAG pipeline
                intervention = generate_intervention(
                    failed_question_text=q['question_text'],
                    user_wrong_answer=user_wrong_answer_text
                )
                
                print("\n" + "*"*60)
                print("AI TUTOR INTERVENTION")
                print("*"*60)
                print(intervention)
                
                print("\n(Session paused for review. End of demo.)")
                break # Stop the loop so the student can study
            else:
                print("\n💡 Just a minor slip-up! Check your calculations.")
                print(f"The correct answer was: {correct_answer_text}")
                print("Moving to the next question...")
                time.sleep(2)

    print(f"\nFinal Score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()