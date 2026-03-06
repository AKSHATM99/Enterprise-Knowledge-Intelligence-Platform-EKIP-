from langchain_groq import ChatGroq
from services.retriever import VectorRetriever
from services.embedder import QueryEmbedder
from services.prompt import RAG_PROMPT
from decouple import config
from services.router import route_intent, Intent
from models.models import AskRequest
from langchain_core.messages import HumanMessage, SystemMessage
from services.sql_rag import sql_rag

GROQ_API_KEY = config('GROQ_API_KEY', default=None)
TOP_K = 3
MIN_SIMILARITY = 0.35 

class RAGService:
    def __init__(self):
        self.embedder = QueryEmbedder()
        self.retriever = VectorRetriever()
        self.llm = ChatGroq(
                    model="llama-3.1-8b-instant",
                    temperature=0,
                    api_key=GROQ_API_KEY,
                )

    def answer(self, question: AskRequest):
        intent = route_intent(question)

        if intent == Intent.DOCUMENT:
            query_vec = self.embedder.embed(question)
            results = self.retriever.retrieve(query_vec, limit=TOP_K)
            if not results or results[0]["score"] < MIN_SIMILARITY:
                return {
                    "answer": "I don't know",
                    "sources": [],
                    "confidence": results[0]["score"] if results else 0.0
                }

            context = "\n\n".join(
                f"{r['source']}: {r['text']}"
                for r in results
            )

            prompt = RAG_PROMPT.format(
                context=context,
                question=question
            )

            response = self.llm.invoke(prompt)

            return {
                "answer": response.content,
                "sources": list(set(r["source"] for r in results)),
                "confidence": results[0]["score"]
            }
        
        elif intent == Intent.DATABASE:
            return sql_rag(question)
        
        else: # For General Queries
            system_instruction = SystemMessage(content="You are a concise assistant. Provide answers in one or two sentences maximum.")
            human_query = HumanMessage(content=question)
            response = self.llm.invoke([system_instruction, human_query])
            return {
                "answer": response.content,
                "sources": [self.llm.model_name],
                "confidence": 100
            }
