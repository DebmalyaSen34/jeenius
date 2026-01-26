from pydantic import BaseModel
from typing import List, Optional, Any

class AnswerRequest(BaseModel):
    thread_id: str
    selected_option_index: int

class QuestionResponse(BaseModel):
    id: str | int
    question_text: str
    options: List[str]
    difficulty_level: Optional[float] = None

class TutorSessionResponse(BaseModel):
    status: str
    question: QuestionResponse

class FeedbackResponse(BaseModel):
    is_correct: bool
    explanation: Optional[str] = None

class AnswerResponse(BaseModel):
    feedback: FeedbackResponse
    next_question: Optional[QuestionResponse] = None