from app.conversation import ConversationAnalyzer
from app.guardrails import Guardrails
from app.recommender import RecommendationEngine
from app.retriever import HybridRetriever

retriever = HybridRetriever()
guardrails = Guardrails()
analyzer = ConversationAnalyzer()
recommender = RecommendationEngine()


class SHLAgent:

    def __init__(self):
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
        query = query.lower().strip()
        return query in self.vague_queries

    def process(self, messages):

        latest_message = messages[-1].content.strip()

        # -----------------------
        # Guardrails
        # -----------------------
        allowed, reply = guardrails.check(latest_message)

        if not allowed:
            return {
                "reply": reply,
                "recommendations": [],
                "end_of_conversation": False,
            }

        # -----------------------
        # Clarification
        # -----------------------
        if self.needs_clarification(latest_message):
            return {
                "reply": (
                    "Sure! What role are you hiring for? "
                    "(e.g. Java Developer, Sales Manager, HR Executive)"
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # -----------------------
        # Extract requirements
        # -----------------------
        requirements = analyzer.extract(messages)

        # -----------------------
        # Retrieve
        # -----------------------
        candidates = retriever.search(requirements)

        # -----------------------
        # Rank
        # -----------------------
        ranked = recommender.rank(
            requirements,
            candidates,
            top_k=10,
        )

        recommendations = []

        for item in ranked:

            recommendations.append(
                {
                    "name": item.get("name", ""),
                    "url": item.get("url", item.get("link", "")),
                    "test_type": (
    item.get("keys", ["Unknown"])[0]
    if item.get("keys")
    else "Unknown"
),
                }
            )

        if not recommendations:
            return {
                "reply": (
                    "I couldn't find a suitable SHL assessment. "
                    "Could you provide more details about the role or required skills?"
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        return {
            "reply": f"I found {len(recommendations)} matching SHL assessment(s).",
            "recommendations": recommendations,
            "end_of_conversation": False,
        }