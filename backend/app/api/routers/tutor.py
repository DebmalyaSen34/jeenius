from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.routers.auth import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.learning_history import LearningHistory
from app.schemas.tutor import AnswerRequest, AnswerResponse, TutorSessionResponse
from app.agent.tutor_graph import app as tutor_graph

router = APIRouter(prefix="/tutor", tags=["Tutor"])

@router.post("/start", response_model=TutorSessionResponse)
def start_tutor_session(thread_id: str, current_user: User = Depends(get_current_user)):
    if not thread_id:
        raise HTTPException(
            status_code=400, detail="thread_id is required to start a tutor session"
        )
    
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
            "questions_catalog": []
        },
        config=config
    )

    for event in events:
        pass

    snapshot = tutor_graph.get_state(config)
    if not snapshot.values.get("current_question"):
        raise HTTPException(
            status_code=500, detail="Failed to start tutor session"
        )
    
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

@router.post("/answer", response_model=AnswerResponse)
def submit_answer(req: AnswerRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
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
            print("Tutor Intervention Event:", event["tutor_intervention"])
            intervention_text = event["tutor_intervention"]["intervention_content"]

        if "grade_answer" in event:
            is_correct = event["grade_answer"]["is_correct"]

    snapshot = tutor_graph.get_state(config)
    history = snapshot.values.get("learning_history", [])

    print("Learning History to be logged:", history)

    if history:
        latest_log = history[-1]
        db_history = LearningHistory(
            user_id=current_user.id,
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
            "options": next_q['options'],
            "difficulty_level": next_q['difficulty_level']
        } if next_q else None
    }