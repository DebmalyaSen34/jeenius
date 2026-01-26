import json
import random
import time
from datetime import datetime
from typing import TypedDict, List, Optional, Literal
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

from app.agent.genai_tutor import generate_intervention, get_tutor_llm
from app.agent.scoring_logic import get_ai_score
from app.core.config import settings

class TutorState(TypedDict):
    questions_catalog: List[dict]
    current_question: Optional[dict]
    user_answer_index: Optional[int]
    is_correct: Optional[bool]
    severity_score: int
    difficulty_cursor: float
    intervention_content: Optional[str]
    session_start_time: str
    total_score: int
    time_taken_last_q: float
    learning_history: List[dict]
    # messages: List[str]

def load_data_node(state: TutorState):
    print("--- Node: Loading Data ---")
    if not state.get('questions_catalog'):
        with open(settings.question_bank_path, 'r') as f:
            data = json.load(f)
        return {
            "questions_catalog": data,
            "difficulty_cursor": 0.3,
            "total_score": 0,
            "learning_history": [],
            "session_start_time": datetime.now().isoformat(),
        }
    return {}

def select_question_node(state: TutorState):
    print(f"--- Node: Selecting Question (Difficulty: {state['difficulty_cursor']:.2f}) ---")
    catalog = state['questions_catalog']
    target_diff = state['difficulty_cursor']
    history = state.get('learning_history', [])

    asked_ids = {entry['question_id'] for entry in history}

    available_questions = [q for q in catalog if q['id'] not in asked_ids]

    if not available_questions:
        print("All questions have been asked. Resetting question pool.")
        available_questions = catalog

    sorted_q = sorted(available_questions, key=lambda x: abs(x['difficulty_level'] - target_diff))

    sample_size = min(3, len(sorted_q))

    next_q = random.choice(sorted_q[:sample_size])

    return {
        "current_question": next_q,
        "intervention_content": None,
        "user_answer_index": None,
        "time_taken_last_q": 0.0
    }

def ask_user_node(state: TutorState):
    q = state['current_question']
    print(f"\n[Problem ID: {q['id']}] Difficulty: {q['difficulty_level']}")
    print(f"Question: {q['question_text']}")
    print("Options:")
    for idx, option in enumerate(q['options']):
        print(f"{idx + 1}. {option}", end=' ')

    valid = False
    choice = -1

    start_time = time.time()

    while not valid:
        try:
            val = input("\nSelect Option (1-4): ")
            choice = int(val) - 1
            if 0 <= choice < len(q['options']):
                valid = True
            else:
                print("Invalid choice. Please select a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    return {
        "user_answer_index": choice,
        "time_taken_last_q": duration
    }

def grade_answer_node(state: TutorState):
    print("--- Node: Grading Answer ---")
    q = state['current_question']
    u_idx = state['user_answer_index']
    c_idx = q['correct_option_index']
    current_score = state.get('total_score', 0)

    is_correct = (u_idx == c_idx)

    if is_correct:
        print(">> Answer Correct!")
        return {
            "is_correct": True,
            "severity_score": 0,
            "total_score": current_score + 1
        }
    
    print(">> Answer Incorrect. Analyzing...")

    q_context = q.copy()
    q_context['is_correct'] = False
    q_context['user_selected_option_index'] = u_idx

    llm = get_tutor_llm(model="gemini-2.5-flash", use_google=True)
    severity_level = get_ai_score(q_context, llm)

    print(f">> Assigned Severity Level: {severity_level}")

    return {
        "is_correct": False,
        "severity_score": severity_level,
        "total_score": current_score-1
    }

def tutor_intervention_node(state: TutorState):
    print("--- Node: Generating Intervention ---")
    q = state['current_question']
    user_opt_text = q['options'][state['user_answer_index']]

    response = generate_intervention(q['question_text'], user_opt_text)

    print("\n" + "="*40)
    print("TUTOR ADVICE")
    print("="*40)
    print(response)
    print("="*40 + "\n")

    return {
        "intervention_content": response
    }

def adjust_difficulty_node(state: TutorState):
    current_diff = state['difficulty_cursor']
    severity = state['severity_score']
    q = state['current_question']

    step = 0.05

    if state['is_correct']:
        new_diff = min(1.0, current_diff + step)
        print(f">> Increasing difficulty to {new_diff:.2f}")
    elif severity <=2:
        new_diff = max(0.1, current_diff - step)
        print(f">> Decreasing difficulty to {new_diff:.2f}")
    else:
        new_diff = max(0.1, current_diff - (step*2))
        print(f">> Significantly decreasing difficulty to {new_diff:.2f}")

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "question_id": q['id'],
        "topic": q['topic'],
        "sub_concept": q['sub_concept'],
        "question_difficulty": q['difficulty_level'],
        "time_taken_seconds": state['time_taken_last_q'],
        "is_correct": state['is_correct'],
        "user_selected_index": state['user_answer_index'],
        "severity_rating": severity,
        "ai_explanation": state.get('intervention_content') if not state['is_correct'] else None,
        "difficulty_delta": new_diff - current_diff,
        "cumulative_score": state['total_score']
    }

    history = state.get('learning_history', [])
    history.append(log_entry)

    return {
        "difficulty_cursor": new_diff,
        "learning_history": history
    }

def determine_next_step(state: TutorState) -> Literal["tutor_intervention", "adjust_difficulty"]:
    if state['is_correct']:
        return "adjust_difficulty"
    
    if state['severity_score'] >=3:
        return "tutor_intervention"
    
    return "adjust_difficulty"

workflow = StateGraph(TutorState)

workflow.add_node("load_data", load_data_node)
workflow.add_node("select_question", select_question_node)
workflow.add_node("ask_user", ask_user_node)
workflow.add_node("grade_answer", grade_answer_node)
workflow.add_node("tutor_intervention", tutor_intervention_node)
workflow.add_node("adjust_difficulty", adjust_difficulty_node)

workflow.set_entry_point("load_data")

workflow.add_edge("load_data", "select_question")
workflow.add_edge("select_question", "ask_user")
workflow.add_edge("ask_user", "grade_answer")

workflow.add_conditional_edges(
    "grade_answer",
    determine_next_step,
    {
        "tutor_intervention": "tutor_intervention",
        "adjust_difficulty": "adjust_difficulty"
    }
)

workflow.add_edge("tutor_intervention", "adjust_difficulty")
workflow.add_edge("adjust_difficulty", "select_question")

checkpointer = MemorySaver()
app = workflow.compile(checkpointer=checkpointer, interrupt_before=["ask_user"])