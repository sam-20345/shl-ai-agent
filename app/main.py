from fastapi import FastAPI

from app.agent import SHLAgent
from app.models import ChatRequest

app = FastAPI(
    title="SHL AI Assessment Recommender",
    version="1.0.0"
)

agent = SHLAgent()


@app.get("/")
def root():
    return {
        "message": "SHL AI Assessment Recommender API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return agent.process(request.messages)