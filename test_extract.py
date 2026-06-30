from app.conversation import ConversationAnalyzer
from app.models import Message

messages = [
    Message(
        role="user",
        content="""
We are hiring a Backend Java Developer.

Need Java

Need Spring Boot

Need SQL

Need AWS

Strong communication skills required.

Leadership experience preferred.

English speaking.

Around 5 years experience.

Financial services domain.
"""
    )
]

analyzer = ConversationAnalyzer()

requirements = analyzer.extract(messages)

print(requirements)