class Guardrails:

    def check(self, query: str):

        query = query.lower()

        # Prompt injection
        injection = [
            "ignore previous",
            "ignore all instructions",
            "system prompt",
            "developer message",
            "act as",
            "pretend",
            "jailbreak"
        ]

        for phrase in injection:
            if phrase in query:
                return (
                    False,
                    "I can only help with recommending and comparing SHL assessments."
                )

        # Obvious off-topic topics
        off_topic = [
            "ipl",
            "cricket",
            "football",
            "weather",
            "bitcoin",
            "stock",
            "movie",
            "song",
            "recipe",
            "poem",
            "joke",
            "president",
            "prime minister",
            "capital of",
            "who won"
        ]

        for phrase in off_topic:
            if phrase in query:
                return (
                    False,
                    "I'm designed only to recommend and compare SHL assessments. Please ask me about hiring assessments."
                )

        return True, None