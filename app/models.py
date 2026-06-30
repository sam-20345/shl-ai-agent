from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


class Assessment(BaseModel):
    name: str
    url: str
    test_type: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: list[Assessment]
    end_of_conversation: bool


class HiringRequirements(BaseModel):
    role: str = ""
    experience: str = ""
    job_level: str = ""

    technical_skills: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    languages: list[str] = Field(default_factory=list)

    assessment_type: str = ""

    industry: str = ""

    additional_requirements: list[str] = Field(default_factory=list)