# filepath: /Users/achuthkartha/IITH/JEEnius/jeenius/scripts/list_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file.")
else:
    genai.configure(api_key=api_key)
    
    print("Fetching available models...")
    try:
        for m in genai.list_models():
            # We only care about models that can generate text/content
            if 'generateContent' in m.supported_generation_methods:
                print(f"Name: {m.name}")
    except Exception as e:
        print(f"Error listing models: {e}")