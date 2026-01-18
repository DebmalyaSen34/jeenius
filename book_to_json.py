import os
import time
import json
import google.generativeai as genai
import re
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = "books/hc_verma_kinematics_full.pdf"
JSON_PATH = "books/hc_verma_kinematics_questions.json"

def clean_json_text(text: str):
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*$', '', text)

    start = text.find('[')
    end = text.rfind(']')
    
    if start != -1 and end != -1:
        text = text[start:end+1]

    return text

def process_pdf_to_json(pdf_path: str, json_path: str):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    sample_file = genai.upload_file(path=pdf_path, mime_type="application/pdf", display_name="Physics Chapter: Kinematics")
    print(f"Uploaded file ID: {sample_file.uri}")

    while sample_file.state.name == "PROCESSING":
        print("File is still processing. Waiting for 2 seconds...")
        time.sleep(2)
        sample_file = genai.get_file(sample_file.name)

    if sample_file.state.name == "FAILED":
        raise Exception(f"File processing failed: {sample_file.error.message}")
    
    print("File processed successfully. Starting extraction...")

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = """
    You are an expert Physics Teacher and Data Architect. 
    Analyze this PDF chapter. Your task is to extract *purely text-based* practice questions into a structured JSON database.
    
    TARGET CONTENT:
    Look for "Worked Out Examples", "Objective I", "Objective II", and "Exercises".
    
    INSTRUCTIONS:
    1. FILTER (CRITICAL): **Strictly IGNORE and SKIP** any question that relies on a visual element.
       - If a question says "See Figure X", "As shown in the diagram", or requires reading a graph, DO NOT include it.
       - Extract ONLY questions where the problem statement is fully contained in the text.
    
    2. SOLVE: 
       - If it is a 'Solved Example', use the provided solution logic.
       - If it is an 'Exercise' (unsolved), YOU MUST SOLVE IT step-by-step to generate the 'solution_logic' and identify the 'correct_option_index'.
    
    3. FORMAT: 
       - If the question is Subjective (no options), CONVERT it into a Multiple Choice Question (MCQ) by generating 3 plausible wrong options (distractors).
       - Ensure all Math is in LaTeX (e.g., $v^2 = u^2 + 2as$).
    
    STRICT JSON OUTPUT FORMAT (List of Objects):
    [
      {
        "id": "q_001", 
        "topic": "Kinematics",
        "sub_concept": "Specific concept (e.g. Projectile Motion)",
        "difficulty_level": 0.3,
        "question_text": "Full question text.",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_option_index": 0,
        "solution_logic": "Step-by-step explanation."
      }
    ]
    """

    response = model.generate_content(
        [sample_file, prompt],
        generation_config={
            "response_mime_type": "application/json",
        }
    )

    raw_text = response.text
    cleaned_text = clean_json_text(raw_text)

    try:
        # json_content = response.text

        data = json.loads(cleaned_text)

        with open(json_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"Questions saved to {json_path}")

    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        
        print("Attempting to fix common issues...")

        fix_prompt = f"""
        The following JSON is invalid due to escape characters. Please fix it and return ONLY valid JSON.
        
        INVALID JSON:
        {raw_text}
        """

        response_fix = model.generate_content(
            fix_prompt,
            generation_config={
                "response_mime_type": "application/json",
            }
        )

        try:
            data = json.loads(response_fix.text)
            with open(json_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Fixed JSON saved to {json_path}")
        except json.JSONDecodeError as e2:
            print(f"Failed to decode fixed JSON: {e2}")
            with open("debug_invalid_json.txt", 'w') as f:
                f.write(raw_text)
                
    genai.delete_file(sample_file.name)

if __name__ == "__main__":
    process_pdf_to_json(PDF_PATH, JSON_PATH)