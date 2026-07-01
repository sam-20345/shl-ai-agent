from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agent import SHLAgent
from app.models import ChatRequest

app = FastAPI(
    title="SHL AI Assessment Recommender",
    version="1.0.0"
)

# Allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = SHLAgent()


@app.get("/")
def root():
    return {
        "message": "SHL AI Assessment Recommender API",
        "documentation": "/docs",
        "health": "/health",
        "chat": "/chat"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return agent.process(request.messages)