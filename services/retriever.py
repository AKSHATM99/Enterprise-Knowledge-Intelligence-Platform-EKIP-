import os
from typing import Any, Dict, List
import httpx

class VectorRetriever:
    def __init__(self, collection: str = "documents") -> None:
        # host = os.getenv("QDRANT_HOST", "localhost")
        # port = int(os.getenv("QDRANT_PORT", "6333"))
        self.base_url = "http://qdrant:6333"
        self.collection = collection

    def retrieve(self, query_embedding: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        url = f"{self.base_url}/collections/{self.collection}/points/search"

        payload = {
            "vector": query_embedding,
            "limit": limit,
            "with_payload": True
        }

        with httpx.Client(timeout=30.0) as client:
            resp = client.post(url, json=payload)
            resp.raise_for_status()
            data = resp.json()

            raw_results = data.get("result", [])

            normalized = []
            for r in raw_results:
                payload_data = r.get("payload", {}) or {}

                normalized.append({
                    "text": payload_data.get("text", ""),
                    "source": payload_data.get("source", ""),
                    "score": r.get("score", 0.0)
                })

            return normalized
