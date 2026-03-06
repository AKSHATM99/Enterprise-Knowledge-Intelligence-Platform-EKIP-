from flask import Flask, request, jsonify
from ingestion.loaders.pdf_loader import load_pdf
from ingestion.services.embedder import Embedder
from ingestion.services.vector_store import VectorStore

embedder = Embedder()
vector_store = VectorStore()
app = Flask(__name__)

@app.route("/ingest/pdf", methods=["POST"])
def ingest_pdf():
    file = request.files.get("file")
    nodes = load_pdf(file)
    texts = [n.text for n in nodes]
    embeddings = embedder.embed(texts)

    payloads = [
    {"text": chunk, "source": file.filename}
    for chunk in texts
    ]

    vector_store.upsert(embeddings, payloads)

    return jsonify({
        "status": "indexed",
        "chunks": len(texts)
    })

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
