import os
import uuid
from typing import Any, Dict, List

import httpx


class VectorStore:
    def __init__(self, collection: str = "documents") -> None:
        host = os.getenv("QDRANT_HOST", "localhost")
        port = int(os.getenv("QDRANT_PORT", "6333"))
        self.base_url = f"http://{host}:{port}"
        self.collection = collection

        # Create (or update) the collection with the expected vector size.
        # Using 768 to match Groq nomic-embed-text-v1_5 embeddings.
        url = f"{self.base_url}/collections/{self.collection}"
        payload = {
            "vectors": {
                "size": 384,
                "distance": "Cosine",
            }
        }
        with httpx.Client(timeout=30.0) as client:
            resp = client.put(url, json=payload)
            resp.raise_for_status()

    def upsert(self, embeddings: List[List[float]], payloads: List[Dict[str, Any]]) -> None:
        points = [
            {
                "id": str(uuid.uuid4()),
                "vector": embedding,
                "payload": payload,
            }
            for embedding, payload in zip(embeddings, payloads)
        ]

        url = f"{self.base_url}/collections/{self.collection}/points"
        payload = {"points": points}
        with httpx.Client(timeout=30.0) as client:
            resp = client.put(url, json=payload)
            resp.raise_for_status()
