from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import bcrypt
from typing import Optional

from agent.tutor_graph import app as tutor_graph
from database.database import engine, get_db, Base
from models.user import User
from models.learning_history import LearningHistory

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JEE-AI Coach API")


origins = [
    "http://localhost:5173",    # Vite (Frontend)
    "http://127.0.0.1:5173",    # Vite (Alternative IP)
    "http://localhost:8000",    # Self
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)

def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class AnswerRequest(BaseModel):
    thread_id: str
    selected_option_index: int

# In-memory session state
CURRENT_QUESTION_INDEX = 0

@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "id": new_user.id,
        "username": new_user.username
    }

@app.post("/login", status_code=status.HTTP_200_OK)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {
        "message": "Login Successful",
        "user_id": db_user.id
    }

@app.post("/tutor/start")
def start_tutor_session(thread_id: str, user_id: int):

    if not thread_id:
        raise HTTPException(status_code=400, detail="thread_id is required")

    config = {
        "configurable": {
            "thread_id": str(thread_id)
        }
    }

    print(f"Starting tutor session for config: {config}")

    events = tutor_graph.stream(
        {
            "difficulty_cursor": 0.5,
            "total_score": 0,
            "learning_history": [],
            "questions_catalog": [] # Initial empty catalog, load_data_node should fill it
        },
        config=config
    )

    for event in events:
        pass

    snapshot = tutor_graph.get_state(config)
    if not snapshot.values.get("current_question"):
        raise HTTPException(status_code=500, detail="Failed to start tutor session")
    
    q = snapshot.values["current_question"]

    return {
        "status": "ready",
        "question": {
            "id": q['id'],
            "question_text": q['question_text'],
            "options": q['options'],
            "difficulty_level": q['difficulty_level']
        }
    }

@app.post("/tutor/answer")
def submit_answer(req: AnswerRequest, user_id: int, db: Session = Depends(get_db)):
    config = {
        "configurable": {
            "thread_id": req.thread_id
        }
    }

    tutor_graph.update_state(
        config,
        {
            "user_answer_index": req.selected_option_index
        },
        as_node="ask_user"
    )

    events = tutor_graph.stream(None, config=config)

    intervention_text = None
    is_correct = False

    for event in events:
        if "tutor_intervention" in event:
            intervention_text = event["tutor_intervention"]["intervention_content"]
        if "grade_answer" in event:
            is_correct = event["grade_answer"]["is_correct"]

    snapshot = tutor_graph.get_state(config)
    history = snapshot.values.get("learning_history", [])

    if history:
        latest_log = history[-1]

        db_history = LearningHistory(
            user_id=user_id,
            question_id=latest_log['question_id'],
            topic=latest_log['topic'],
            sub_concept=latest_log['sub_concept'],
            question_difficulty=latest_log['question_difficulty'],
            time_taken_seconds=latest_log.get('time_taken_seconds', 0),
            is_correct=latest_log['is_correct'],
            severity_rating=latest_log.get('severity_rating', 0),
            ai_explanation=latest_log.get('ai_explanation'),
            difficulty_delta=latest_log.get('difficulty_delta', 0),
            cumulative_score=latest_log.get('cumulative_score', 0)
        )
        db.add(db_history)
        db.commit()

    next_q = snapshot.values.get("current_question")

    return {
        "feedback": {
            "is_correct": is_correct,
            "explanation": intervention_text
        },
        "next_question": {
            "id": next_q['id'],
            "question_text": next_q['question_text'],
            "options": next_q['options']
        } if next_q else None
    }