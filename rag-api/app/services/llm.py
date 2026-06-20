import httpx
from app.core.config import settings


async def embed_text(text: str) -> list[float]:
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            f"{settings.ollama_url}/api/embeddings",
            json={"model": settings.embedding_model, "prompt": text},
        )
        response.raise_for_status()
        return response.json()["embedding"]


async def generate_answer(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=300) as client:
        response = await client.post(
            f"{settings.ollama_url}/api/generate",
            json={"model": settings.generation_model, "prompt": prompt, "stream": False},
        )
        response.raise_for_status()
        return response.json().get("response", "")
