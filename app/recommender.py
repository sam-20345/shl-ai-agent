from app.models import HiringRequirements


class RecommendationEngine:

    def rank(self, requirements: HiringRequirements, candidates: list, top_k=5):

        scored = []

        for item in candidates:

            score = 0

            text = (
                item.get("name", "") + " " +
                item.get("description", "") + " " +
                " ".join(item.get("keys", []))
            ).lower()

            # Role (highest weight)
            if requirements.role:
                for word in requirements.role.lower().split():
                    if word in text:
                        score += 4

            # Technical Skills
            for skill in requirements.technical_skills:
                if skill.lower() in text:
                    score += 3

            # Soft Skills
            for skill in requirements.soft_skills:
                if skill.lower() in text:
                    score += 2

            # Job Level
            if requirements.job_level:
                if requirements.job_level.lower() in " ".join(
                    item.get("job_levels", [])
                ).lower():
                    score += 2

            # Industry
            if requirements.industry:
                if requirements.industry.lower() in text:
                    score += 1

            scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [item for _, item in scored[:top_k]]