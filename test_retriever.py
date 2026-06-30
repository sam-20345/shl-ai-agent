from app.conversation import ConversationAnalyzer
from app.models import Message
from app.retriever import HybridRetriever

messages = [
    Message(
        role="user",
        content="""
We are hiring a Backend Java Developer.

Need Java

Need Spring Boot

Need SQL

Need AWS

Strong communication skills.

5 years experience.
"""
    )
]

analyzer = ConversationAnalyzer()

requirements = analyzer.extract(messages)

retriever = HybridRetriever()

results = retriever.search(requirements)

for result in results:

    print(result["name"])