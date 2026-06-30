import json
from pathlib import Path

from rank_bm25 import BM25Okapi


class HybridRetriever:

    def __init__(self):

        data_path = Path("data/catalogue.json")

        with open(data_path, encoding="utf-8") as f:
            self.catalog = json.load(f)

        self.documents = []

        for item in self.catalog:

            text = " ".join(
                [
                    item.get("name", ""),
                    item.get("description", ""),
                    " ".join(item.get("keys", [])),
                    " ".join(item.get("job_levels", [])),
                    " ".join(item.get("languages", [])),
                ]
            )

            self.documents.append(text.lower().split())

        self.bm25 = BM25Okapi(self.documents)

    def search(self, requirements, top_k=10):

        query = []

        if requirements.role:
            query.extend(requirements.role.lower().split())

        if requirements.technical_skills:
            query.extend(
                skill.lower()
                for skill in requirements.technical_skills
            )

        if requirements.soft_skills:
            query.extend(
                skill.lower()
                for skill in requirements.soft_skills
            )

        if requirements.job_level:
            query.extend(
                requirements.job_level.lower().split()
            )

        if requirements.industry:
            query.extend(
                requirements.industry.lower().split()
            )

        scores = self.bm25.get_scores(query)

        ranked = sorted(
            zip(scores, self.catalog),
            key=lambda x: x[0],
            reverse=True,
        )

        return [item for _, item in ranked[:top_k]]

    def find_by_name(self, name: str):

        name = name.lower().strip()

        # Exact match first
        for assessment in self.catalog:
            if assessment.get("name", "").lower() == name:
                return assessment

        # Partial match
        for assessment in self.catalog:
            if name in assessment.get("name", "").lower():
                return assessment

        return None

    def get_all(self):
        return self.catalog