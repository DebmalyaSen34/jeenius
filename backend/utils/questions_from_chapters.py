import ollama
import os
import json
from typing import List, Dict

def chunk_text(text: str, max_chars: int = 15000, overlap: int = 500) -> List[str]:
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars

        if end < len(text):
            break_point = text.rfind('\n', start, end)
            if break_point == -1:
                break_point = text.rfind('\n\n', start, end)
            if break_point != -1 and break_point > start + max_chars // 2:
                end = break_point + 1

        chunks.append(text[start:end])
        start = end - overlap

    return chunks

def extract_questions_from_chunk(chunk: str, chunk_index: int, model: str = "llama3.1") -> List[Dict]:
    prompt = f"""
You are an expert at extracting physics questions from textbook chapters.

Extract ALL questions found in this text section. Include:
- Worked examples with questions
- Practice problems
- Exercise questions
- Conceptual questions

For each question, provide:
1. A unique ID (use format: q_chunk{chunk_index}_001, q_chunk{chunk_index}_002, etc.)
2. Topic and sub-concept
3. Difficulty level (0.0-1.0)
4. Complete question text
5. Options (if multiple choice, otherwise empty array)
6. Correct answer index (or null if not MCQ)
7. Solution approach

Return ONLY valid JSON array, no markdown formatting:

[
  {{
    "id": "q_chunk{chunk_index}_001",
    "topic": "Kinematics",
    "sub_concept": "Distance vs Displacement",
    "difficulty_level": 0.25,
    "question_text": "A man walks 50 m north, 40 m east and 20 m south. Find (a) total distance and (b) displacement.",
    "options": ["110 m, 30 m", "90 m, 50 m", "110 m, 50 m", "100 m, 40 m"],
    "correct_option_index": 2,
    "solution_logic": "Distance is scalar sum = 50+40+20=110m. Displacement is vector resultant: north component = 50-20=30m, east=40m, total = √(30²+40²)=50m."
  }}
]

Text section:
{chunk}

Return JSON array only (empty array [] if no questions found):"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.1
            }
        )

        content = response['message']['content'].strip()

        questions = json.loads(content)
        return questions if isinstance(questions, list) else []
    except json.JSONDecodeError as e:
        print(f"JSON decoding error for chunk {chunk_index}: {e}")
        return []
    except Exception as e:
        print(f"Error processing chunk {chunk_index}: {e}")
        return []

def get_questions_from_chapter(filepath: str, model: str = "llama3.1", max_chunk_size: int = 15000, chunk_overlap: int = 500, output_dir: str = "data/processed/questions") -> List[Dict]:

    with open(filepath, 'r') as file:
        chapter = file.read()

    chapter_length = len(chapter)
    print(f"Chapter length: {chapter_length} characters")

    chunks = chunk_text(chapter, max_chunk_size, chunk_overlap)
    print(f"Chapter split into {len(chunks)} chunks")

    all_questions = []

    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)} ({len(chunk):,} chars)...")
        
        questions = extract_questions_from_chunk(chunk, i, model)
        
        if questions:
            print(f"Found {len(questions)} questions in chunk {i+1}")
            all_questions.extend(questions)
        else:
            print(f" No questions were found in chunk {i+1}")

    #TODO: Add logic to deduplicate questions

    os.makedirs(output_dir, exist_ok=True)
    chapter_name = os.path.splitext(os.path.basename(filepath))[0]
    output_path = os.path.join(output_dir, f"{chapter_name}_questions.json")

    with open(output_path, 'w') as f:
        json.dump(all_questions, f, indent=4)

    print(f"Extracted {len(all_questions)} questions from chapter and saved to {output_path}")

    return all_questions

if __name__ == "__main__":
    questions_json = get_questions_from_chapter("data/processed/chapters/chapter_1_Introduction_to_Physics.md", model="gpt-oss:20b-cloud", output_dir="data/processed/questions")

    print(questions_json)