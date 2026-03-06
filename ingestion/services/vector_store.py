import uuid
from typing import Any, Dict, List
import httpx

class VectorStore:
    def __init__(self, collection: str = "documents") -> None:
        self.base_url = "http://qdrant:6333"
        self.collection = "documents"

        with httpx.Client() as client:
            # 1️⃣ Check if collection exists
            check = client.get(f"{self.base_url}/collections/{self.collection}")

            if check.status_code == 404:
                # 2️⃣ Create only if not exists
                create = client.put(
                    f"{self.base_url}/collections/{self.collection}",
                    json={
                        "vectors": {
                            "size": 1024,   # must match embedding dimension
                            "distance": "Cosine"
                        }
                    }
                )
                create.raise_for_status()
                print("Collection created.")
            else:
                print("Collection already exists.")

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
