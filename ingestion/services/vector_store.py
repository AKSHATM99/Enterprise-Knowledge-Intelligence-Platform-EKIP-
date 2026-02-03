from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
import uuid

class VectorStore:
    def __init__(self, collection="documents"):
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection = collection

        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config={"size": 384, "distance": "Cosine"}
        )

    def upsert(self, embeddings, payloads):
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload=payload
            )
            for embedding, payload in zip(embeddings, payloads)
        ]

        self.client.upsert(
            collection_name=self.collection,
            points=points
        )
