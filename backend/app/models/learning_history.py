from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime, timezone

class LearningHistory(Base):
    __tablename__ = 'learning_history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    question_id = Column(String)
    topic = Column(String)
    sub_concept = Column(String)
    question_difficulty = Column(Float)
    time_taken_seconds = Column(Float)
    is_correct = Column(Boolean)
    severity_rating = Column(Integer)
    ai_explanation = Column(String, nullable=True)
    difficulty_delta = Column(Float)
    cumulative_score = Column(Integer)

    user = relationship("User", back_populates="history")