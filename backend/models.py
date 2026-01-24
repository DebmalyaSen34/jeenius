from pydantic import BaseModel
from typing import List, Optional

# 1. What we send to the Frontend (The Question)
class QuestionSchema(BaseModel):
    id: str
    sub_concept: str
    difficulty_level: float
    question_text: str
    options: List[str]

# 2. What the Frontend sends to us (The Answer)
class AnswerRequest(BaseModel):
    question_id: str
    selected_option_index: int # 0, 1, 2, or 3

# 3. What we send back after they answer (The Result)
class AssessmentResponse(BaseModel):
    is_correct: bool
    correct_answer_text: str
    severity_score: int = 0 # 0 if correct, 1-5 if wrong
    ai_explanation: Optional[str] = None # Only present if wrong & severe
    next_question: Optional[QuestionSchema] = None # The next question to display
    session_ended: bool = False