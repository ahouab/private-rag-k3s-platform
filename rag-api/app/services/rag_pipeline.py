from app.services.chunker import chunk_text
from app.services.llm import embed_text, generate_answer
from app.services.vector_store import search_chunks, upsert_chunks


async def ingest_document(document_id: str, text: str) -> dict:
    chunks = chunk_text(text)
    embeddings = []
    for chunk in chunks:
        embeddings.append(await embed_text(chunk))
    upsert_chunks(document_id=document_id, chunks=chunks, embeddings=embeddings)
    return {"document_id": document_id, "chunks": len(chunks)}


async def answer_question(question: str, top_k: int = 5) -> dict:
    query_embedding = await embed_text(question)
    contexts = search_chunks(query_embedding=query_embedding, limit=top_k)
    context_text = "\n\n".join(
        f"Source: {item.get('document_id')} chunk {item.get('chunk_id')}\n{item.get('text')}"
        for item in contexts
    )
    prompt = f"""
You are a private enterprise RAG assistant.
Answer only from the provided context.
If the answer is not in the context, say that the information is not available.
Cite the source document IDs and chunk IDs.

Context:
{context_text}

Question:
{question}

Answer:
"""
    answer = await generate_answer(prompt)
    return {"answer": answer, "sources": contexts}
