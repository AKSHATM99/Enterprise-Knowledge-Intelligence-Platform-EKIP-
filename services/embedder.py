import ollama

class QueryEmbedder:

    def __init__(self):
        self.client = ollama.Client(host="http://ollama:11434")

    def embed(self, query: str):
        response = self.client.embed(
            model="qwen3-embedding:0.6b",
            input=query
        )
        return response.embeddings[0]