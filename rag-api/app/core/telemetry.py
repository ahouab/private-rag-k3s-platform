from prometheus_client import Counter, Histogram

rag_requests_total = Counter("rag_requests_total", "Total RAG requests")
rag_errors_total = Counter("rag_errors_total", "Total RAG errors")
rag_request_duration_seconds = Histogram("rag_request_duration_seconds", "RAG request duration")
rag_ingestion_documents_total = Counter("rag_ingestion_documents_total", "Total ingested documents")
rag_vector_search_duration_seconds = Histogram("rag_vector_search_duration_seconds", "Vector search duration")
rag_llm_generation_duration_seconds = Histogram("rag_llm_generation_duration_seconds", "LLM generation duration")
