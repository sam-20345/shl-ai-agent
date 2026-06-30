from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.agent import SHLAgent
from app.models import ChatRequest

app = FastAPI(
    title="SHL AI Assessment Recommender",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

agent = SHLAgent()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body style="
        background:black;
        color:lime;
        font-size:60px;
        text-align:center;
        padding-top:150px;
    ">
        FRONTEND VERSION 2
    </body>
    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return agent.process(request.messages)