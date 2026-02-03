from fastapi import APIRouter
from services.rag import RAGService
from models.models import AskResponse

router = APIRouter()
rag = RAGService()

@router.post("/", response_model=AskResponse)
async def query(payload: dict):
    question = payload.get("question")
    return rag.answer(question)
