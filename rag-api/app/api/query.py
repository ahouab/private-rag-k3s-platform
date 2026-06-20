from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_pipeline import answer_question
from app.core.telemetry import rag_requests_total, rag_request_duration_seconds

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


@router.post("/query")
async def query(request: QueryRequest) -> dict:
    rag_requests_total.inc()
    with rag_request_duration_seconds.time():
        return await answer_question(question=request.question, top_k=request.top_k)
