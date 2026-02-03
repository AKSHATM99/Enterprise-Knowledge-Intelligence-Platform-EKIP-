from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host="localhost", port=6333)

q = "How many paid leaves are allowed?"
emb = model.encode(q).tolist()

res = client.search(
    collection_name="documents",
    query_vector=emb,
    limit=3
)

for r in res:
    print(r.score)
    print(r)
