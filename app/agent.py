from app.conversation import ConversationAnalyzer
from app.retriever import HybridRetriever
from app.recommender import RecommendationEngine
from app.llm import generate_recommendation_reply


class SHLAgent:

    def __init__(self):
        self.analyzer = ConversationAnalyzer()
        self.retriever = HybridRetriever()
        self.recommender = RecommendationEngine()

        self.vague_queries = {
            "assessment",
            "test",
            "i need an assessment",
            "i need a test",
            "hire someone",
            "hiring",
            "candidate",
            "employee",
            "job",
            "i am hiring",
            "need assessment",
        }

    def needs_clarification(self, query: str) -> bool:
        return query.lower().strip() in self.vague_queries

    def process(self, messages):

        latest_message = messages[-1].content.strip()

        # Handle vague queries
        if self.needs_clarification(latest_message):
            return {
                "reply": (
                    "Sure! What role are you hiring for? "
                    "(e.g. Java Developer, Sales Manager, HR Executive)"
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # Extract structured hiring requirements using Gemini
        requirements = self.analyzer.extract(messages)

        # Retrieve top matching assessments
        candidates = self.retriever.search(
            requirements,
            top_k=20,
        )

        # Rank assessments
        results = self.recommender.rank(
            requirements,
            candidates,
            top_k=5,
        )

        # Build API response
        recommendations = []

        for item in results:

            recommendations.append(
    {
        "name": item.get("name", ""),
        "description": item.get("description", ""),
        "duration": item.get("duration", ""),
        "job_levels": item.get("job_levels", []),
        "assessment_type": item.get("keys", []),
        "url": item.get("link", ""),
    }
)

        # No matches
        if not recommendations:
            return {
                "reply": (
                    "I couldn't find suitable assessments. "
                    "Could you provide more details such as role, skills, "
                    "experience level or job function?"
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # Generate AI explanation
        reply = generate_recommendation_reply(
            requirements,
            results,
        )

        return {
            "reply": reply,
            "recommendations": recommendations,
            "end_of_conversation": False,
        }