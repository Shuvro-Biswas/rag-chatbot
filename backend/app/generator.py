import os
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # store safely

def generate_answer(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # or use mistral or other available
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that answers Bangla and English questions based on the context."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
