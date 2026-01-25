from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

def get_model(model: str, use_google: bool = False):
    if use_google:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("API key not found in environment variables.")
        
        return ChatGoogleGenerativeAI(model=model, temperature=0.3, api_key=api_key)
    
    return ChatOllama(model=model, temperature=0.3)