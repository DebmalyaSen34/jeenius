from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.models.learning_history import LearningHistory
from app.schemas.auth import UserRead
from app.api.routers.auth import get_current_user

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/me', response_model=UserRead)
def read_current_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    user = db.query(User).filter(User.id == current_user.id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return user

@router.get('/learning-history')
def get_learning_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    history = db.query(LearningHistory).filter(LearningHistory.user_id == current_user.id).all()

    if not history:
        return {
            "message": "No learning history found for the user."
        }
    
    return history