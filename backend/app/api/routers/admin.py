from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import UserRead
from app.models.learning_history import LearningHistory
from app.api.routers.auth import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_current_admin(current_user: User = Depends(get_current_user)) -> User:

    if not current_user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Insufficient permissions"
        )

    return current_user

@router.get("/users", response_model=List[UserRead])
def get_all_users(skip: int=0, limit: int=100, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{user_id}/learning-history")
def get_user_learning_history(user_id: int, db: Session = Depends(get_db), current_admin: User = Depends(get_current_admin)):

    history = db.query(LearningHistory).filter(LearningHistory.user_id == user_id).all()

    if not history:
        return []
    
    return history