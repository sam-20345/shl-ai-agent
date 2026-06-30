from pprint import pprint

from app.retriever import HybridRetriever
from app.comparison import ComparisonEngine

retriever = HybridRetriever()

java8 = retriever.find_by_name("Java 8")
core = retriever.find_by_name("Core Java")

comparison = ComparisonEngine().compare(java8, core)

pprint(comparison)