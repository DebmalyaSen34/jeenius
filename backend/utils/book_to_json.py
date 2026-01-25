import os
import time
import json
# CHANGE 1: We use the stable library that supports .configure()
import google.generativeai as genai
import re
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = "data/raw/books/hc_verma_kinematics_full.pdf"
JSON_PATH = "data/processed/question_bank.json"

def clean_json_text(text: str):
    """Helper function to remove markdown formatting from the LLM's JSON output."""
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*$', '', text)
    start = text.find('[')
    end = text.rfind(']')
    if start != -1 and end != -1:
        return text[start:end+1]
    return text

def process_pdf_to_json(pdf_path: str, json_path: str):
    """Uploads a PDF, prompts an LLM to extract questions, and saves the result."""
    
    # This line works perfectly with google.generativeai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    print(f"Uploading file: {pdf_path}...")
    sample_file = genai.upload_file(path=pdf_path, display_name="Physics Chapter: Kinematics")
    print(f"Uploaded file. URI: {sample_file.uri}")

    while sample_file.state.name == "PROCESSING":
        print("File is still processing. Waiting for 10 seconds...")
        time.sleep(10)
        sample_file = genai.get_file(name=sample_file.name)

    if sample_file.state.name == "FAILED":
        raise Exception(f"File processing failed.")
    
    print("File processed successfully. Starting extraction...")

    # CHANGE 2: Using the Gemini 2.5 Flash model you requested
    model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

    prompt = """
    You are an expert Physics Teacher and Data Architect. 
    Analyze this PDF chapter. Your task is to extract *purely text-based* practice questions into a structured JSON database.
    
    TARGET CONTENT:
    Look for "Objective I", "Objective II", and "Exercises".
    
    INSTRUCTIONS:
    1. FILTER (CRITICAL): **Strictly IGNORE and SKIP** any question that relies on a visual element like a figure or graph.
    2. SOLVE: YOU MUST SOLVE each question step-by-step to generate the 'solution_logic' and identify the 'correct_option_index'.
    3. FORMAT: Ensure all Math is in LaTeX.
    
    STRICT JSON OUTPUT FORMAT (List of Objects):
    [
      {
        "id": "q_001", 
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
        generation_config={"response_mime_type": "application/json"}
    )

    cleaned_text = clean_json_text(response.text)
    try:
        data = json.loads(cleaned_text)
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully extracted and saved questions to {json_path}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        print("--- RAW RESPONSE ---")
        print(response.text)
        with open("debug_invalid_json.txt", 'w') as f:
            f.write(response.text)
            
    genai.delete_file(name=sample_file.name)
    print(f"Deleted file from server.")

if __name__ == "__main__":
    process_pdf_to_json(PDF_PATH, JSON_PATH)