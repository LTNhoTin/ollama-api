from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str
    stream: bool = False  # không stream kết quả

@app.get("/")
def root():
    return {"message": "Ollama Phi-4 API is running!"}

# API gọi inference từ Phi-4
@app.post("/chat/")
def chat(request: ChatRequest):
    # Gửi request
    ollama_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi4",
        "prompt": request.prompt,
        "stream": request.stream
    }
    
    response = requests.post(ollama_url, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get response from Ollama"}

