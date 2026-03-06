from typing import List
import ollama

class Embedder:
    def __init__(self):
        self.client = ollama.Client(host="http://ollama:11434")

    def embed(self, texts: List[str]) -> List[List[float]]:
        response = self.client.embed(
            model="qwen3-embedding:0.6b",
            input=texts
        )
        return response.embeddings