# SHL AI Assessment Recommender

An AI-powered recommendation system that helps recruiters identify the most suitable SHL assessments using natural language.

## Features

- Natural language hiring queries
- AI-based requirement extraction using Google Gemini
- BM25 retrieval over the SHL assessment catalogue
- Ranking of the most relevant assessments
- Clarification questions for vague hiring requests
- Guardrails for off-topic and prompt-injection queries
- FastAPI REST API
- Deployed on Render

---

## Tech Stack

- Python 3.11
- FastAPI
- Google Gemini 2.5 Flash
- BM25 (rank-bm25)
- Pydantic
- Uvicorn

---

## Project Structure

```
app/
    agent.py
    conversation.py
    recommender.py
    retriever.py
    guardrails.py
    llm.py
    models.py
    prompts.py
    main.py

data/
    catalogue.json
```

---

## Running Locally

```bash
git clone https://github.com/sam-20345/shl-ai-agent.git

cd shl-ai-agent

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## API Endpoints

### Health

GET

```
/health
```

### Chat

POST

```
/chat
```

Example

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need a Java Developer assessment with Spring Boot and SQL."
    }
  ]
}
```

---

## Architecture

```
User
   │
   ▼
FastAPI
   │
   ▼
Guardrails
   │
   ▼
Gemini Requirement Extraction
   │
   ▼
BM25 Retriever
   │
   ▼
Recommendation Engine
   │
   ▼
SHL Assessment Recommendations
```

---

## Deployment

Live API

https://shl-ai-agent-5v1s.onrender.com

API Docs

https://shl-ai-agent-5v1s.onrender.com/docs

---

## Future Improvements

- Semantic vector search using embeddings
- Conversation memory
- React frontend
- Hybrid BM25 + Vector Retrieval
