from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, PointStruct, VectorParams
from app.core.config import settings

client = QdrantClient(url=settings.qdrant_url)


def ensure_collection(vector_size: int) -> None:
    collections = [c.name for c in client.get_collections().collections]
    if settings.qdrant_collection not in collections:
        client.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )


def upsert_chunks(document_id: str, chunks: list[str], embeddings: list[list[float]]) -> None:
    if not embeddings:
        return
    ensure_collection(len(embeddings[0]))
    points = []
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=abs(hash(f"{document_id}-{idx}")) % (10**18),
                vector=embedding,
                payload={"document_id": document_id, "chunk_id": idx, "text": chunk},
            )
        )
    client.upsert(collection_name=settings.qdrant_collection, points=points)


def search_chunks(query_embedding: list[float], limit: int = 5) -> list[dict]:
    results = client.search(
        collection_name=settings.qdrant_collection,
        query_vector=query_embedding,
        limit=limit,
    )
    return [hit.payload | {"score": hit.score} for hit in results]
