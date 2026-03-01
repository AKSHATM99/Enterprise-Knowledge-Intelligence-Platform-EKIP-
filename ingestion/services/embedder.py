from typing import List
from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self) -> None:
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, texts: List[str]) -> List[List[float]]:
        if isinstance(texts, str):
            texts = [texts]

        vectors = self.model.encode(texts, normalize_embeddings=True)
        return vectors.tolist()