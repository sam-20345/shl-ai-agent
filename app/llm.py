from google import genai

from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate(prompt: str) -> str:
    response = client.models.generate_content(
        model=settings.MODEL_NAME,
        contents=prompt,
    )

    return response.text.strip()


def generate_recommendation_reply(requirements, recommendations):

    assessment_text = "\n".join(
        [
            f"""
Name: {item.get('name', '')}
Description: {item.get('description', '')}
"""
            for item in recommendations
        ]
    )

    prompt = f"""
You are an SHL hiring assessment expert.

A recruiter is hiring for:

Role: {requirements.role}

Technical Skills:
{", ".join(requirements.technical_skills)}

Soft Skills:
{", ".join(requirements.soft_skills)}

Experience:
{requirements.experience}

Job Level:
{requirements.job_level}

The following SHL assessments have already been selected by the retrieval system:

{assessment_text}

Write:

1. A short introduction (2-3 sentences).
2. One bullet explaining why EACH assessment is relevant.
3. Do not invent assessments.
4. Do not recommend anything not listed.
5. Keep the response under 150 words.
"""

    return generate(prompt)