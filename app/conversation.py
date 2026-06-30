import json

from app.llm import generate
from app.prompts import REQUIREMENT_EXTRACTION_PROMPT
from app.models import HiringRequirements


class ConversationAnalyzer:

    def extract(self, messages) -> HiringRequirements:
        """
        Extract structured hiring requirements from the conversation
        using Gemini.
        """

        conversation = "\n".join(
            f"{message.role}: {message.content}"
            for message in messages
        )

        prompt = REQUIREMENT_EXTRACTION_PROMPT.format(
            conversation=conversation
        )

        response = generate(prompt)

        # Remove markdown formatting if Gemini returns it
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:
            data = json.loads(response)
            return HiringRequirements(**data)

        except Exception:
            # Return an empty object instead of crashing
            return HiringRequirements()