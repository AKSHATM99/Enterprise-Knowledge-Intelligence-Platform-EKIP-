from qdrant_client import QdrantClient

class VectorRetriever:
    def __init__(self, collection="documents"):
        self.client = QdrantClient(host="localhost", port=6333)
        self.collection = collection

    def retrieve(self, query_embedding, limit=5):
        return self.client.search(
            collection_name=self.collection,
            query_vector=query_embedding,
            limit=limit
        )
