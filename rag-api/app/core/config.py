from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Private RAG API"
    qdrant_url: str = "http://qdrant.rag.svc.cluster.local:6333"
    qdrant_collection: str = "private_documents"
    ollama_url: str = "http://ollama.ai-system.svc.cluster.local:11434"
    embedding_model: str = "nomic-embed-text"
    generation_model: str = "llama3.1:8b"
    minio_endpoint: str = "minio.rag.svc.cluster.local:9000"
    minio_access_key: str = "minioadmin"
    minio_secret_key: str = "minioadmin"
    minio_bucket: str = "documents-raw"


settings = Settings()
