import re
import logging
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models import BaseChatModel

logger = logging.getLogger(__name__)

def _parse_severity(response: str) -> int:
    try:
        match =re.search(r"Severity Level:\s*(\d)", response, re.IGNORECASE)
        if match:
            score = int(match.group(1))
            return max(1, min(5, score))
    except Exception as e:
        logger.error(f"Error parsing severity level: {e}")
    return 3

def get_ai_score(question_data: dict, llm: BaseChatModel) -> int:

    is_correct = question_data.get('is_correct', False)

    if is_correct:
        return 0
    
    explanation = question_data.get('solution_logic', 'No explanation provided.')
    options_list = question_data.get('options', [])

    try:
        user_idx = question_data.get('user_selected_option_index', -1)
        correct_idx = question_data.get('correct_option_index', -1)
        user_option_text = options_list[user_idx] if 0 <= user_idx < len(options_list) else "Unknown"
        correct_option_text = options_list[correct_idx] if 0 <= correct_idx < len(options_list) else "Unknown"
        all_options_str = ", ".join(options_list)
    except Exception as e:
        logger.warning(f"Error retrieving options: {e}")
        return 3

    template = """
        You are an expert JEE Physics Tutor. A student answered a question incorrectly.

        THE QUESTION:
        {question_text}
        
        OPTIONS:
        {options}
        
        STUDENT'S ANSWER:
        {user_option}
        
        CORRECT ANSWER:
        {correct_option}
        
        SOLUTION LOGIC:
        {explanation}

        YOUR TASK:
        Analyze the specific mistake.
        - If it's a calculation error or a "silly mistake" (right concept, wrong math), severity is low (1-2).
        - If it's a distractor that suggests a common misconception, severity is medium (3).
        - If the answer suggests a fundamental gap in the core concept (physics logic is wrong), severity is high (4-5).

        OUTPUT FORMAT:
        Only output the severity level in the format below. Do not add bolding or markdown.
        Severity Level: <1 to 5>
    """

    prompt = ChatPromptTemplate.from_template(template)

    try:
        chain = prompt | llm
        response = chain.invoke(
            {
                "question_text": question_data.get('question_text', 'No question text provided.'),
                "options": all_options_str,
                "user_option": user_option_text,
                "correct_option": correct_option_text,
                "explanation": explanation
            }
        )

        content = response.content if hasattr(response, 'content') else str(response)
        return _parse_severity(content)
    except Exception as e:
        logger.error(f"Error during AI scoring: {e}")
        return 3

