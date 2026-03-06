**Enterprise Knowledge Intelligence Platform (EKIP)**

“Ask questions across internal documents, databases, APIs, and logs—with grounded, auditable answers.”

*Problem statement*

"Organizations have fragmented knowledge across documents and databases. Traditional search fails to provide contextual, explainable answers. This system enables grounded, auditable question-answering over internal knowledge using Retrieval-Augmented Generation."

### Features
- Document ingestion
- Vector search
- Context-aware RAG
- Source citations

✔ FastAPI + Flask compatible backend
✔ SQL RAG + Vector RAG
✔ LangChain + LlamaIndex-style orchestration
✔ Qdrant vector store
✔ Evidence gating
✔ Citation grounding
✔ Confidence scoring
✔ Hallucination detection
✔ Query observability


Architecture--
----------------------

            Internet
                |
                v
        Traefik (port 80/443)
                |
                v
          Streamlit (UI)
                |
                v
FastAPI ----> Flask ----> Qdrant & Ollama