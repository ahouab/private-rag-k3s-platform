from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from tempfile import NamedTemporaryFile
from app.services.document_loader import extract_text
from app.services.rag_pipeline import ingest_document
from app.core.telemetry import rag_ingestion_documents_total

router = APIRouter()


@router.post("/documents/ingest")
async def ingest(file: UploadFile = File(...)) -> dict:
    suffix = Path(file.filename or "document.txt").suffix
    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    text = extract_text(tmp_path)
    result = await ingest_document(document_id=file.filename or "uploaded-document", text=text)
    rag_ingestion_documents_total.inc()
    return result
