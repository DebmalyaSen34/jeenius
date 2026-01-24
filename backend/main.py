from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models import QuestionSchema, AnswerRequest, AssessmentResponse
from backend.engine import QUESTION_BANK, get_next_question, process_answer

app = FastAPI(title="JEE-AI Coach API")

# --- CORS CONFIGURATION (MUST BE HERE) ---
origins = [
    "http://localhost:5173",    # Vite (Frontend)
    "http://127.0.0.1:5173",    # Vite (Alternative IP)
    "http://localhost:8000",    # Self
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow ALL origins for Hackathon simplicity
    allow_credentials=True,
    allow_methods=["*"],        # Allow ALL methods (POST, GET, etc.)
    allow_headers=["*"],        # Allow ALL headers
)
# -----------------------------------------

# In-memory session state
CURRENT_QUESTION_INDEX = 0

@app.get("/")
def read_root():
    return {"status": "JEE-AI API is running"}

@app.post("/start", response_model=QuestionSchema)
def start_quiz():
    global CURRENT_QUESTION_INDEX
    CURRENT_QUESTION_INDEX = 0
    
    if not QUESTION_BANK:
        raise HTTPException(status_code=500, detail="Question bank is empty")
    
    return QUESTION_BANK[0]

@app.post("/submit", response_model=AssessmentResponse)
def submit_answer(answer: AnswerRequest):
    global CURRENT_QUESTION_INDEX
    
    # 1. Process the answer
    logic_result = process_answer(answer.question_id, answer.selected_option_index)
    
    if "error" in logic_result:
        raise HTTPException(status_code=404, detail="Question not found")

    # 2. Build Response
    response = AssessmentResponse(
        is_correct=logic_result['is_correct'],
        correct_answer_text=logic_result['correct_answer_text'],
        severity_score=logic_result['severity_score'],
        ai_explanation=logic_result['ai_explanation']
    )

    # 3. Move to next question
    next_q_data = get_next_question(CURRENT_QUESTION_INDEX)
    
    if next_q_data:
        CURRENT_QUESTION_INDEX += 1
        response.next_question = next_q_data
    else:
        response.session_ended = True

    return response