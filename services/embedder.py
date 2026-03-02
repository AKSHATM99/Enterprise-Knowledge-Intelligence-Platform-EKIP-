from decouple import config
from sentence_transformers import SentenceTransformer

GROQ_API_KEY = config('GROQ_API_KEY', default=None)

class QueryEmbedder:
    def __init__(self) -> None:
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, query: str):
        return self.model.encode(query).tolist()
