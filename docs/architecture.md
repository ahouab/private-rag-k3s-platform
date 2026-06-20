# Architecture

## Components

- Proxmox: virtualization layer
- K3s: Kubernetes platform
- Longhorn: persistent distributed block storage
- Argo CD: GitOps controller
- Traefik: ingress controller
- Cert-manager: certificate lifecycle
- Ollama: local LLM and embeddings runtime
- Qdrant: vector database
- MinIO: object storage for documents
- Open WebUI: user-facing LLM interface
- RAG API: custom FastAPI ingestion and query service
- Prometheus/Grafana/Loki: metrics, dashboards and logs

## Data Flow

```text
Document upload -> RAG API -> text extraction -> chunks -> embeddings -> Qdrant
Question -> embedding -> vector search -> context -> Ollama -> sourced answer
```

## Security Boundary

No external AI API is required. Documents, embeddings, vector database and generated answers remain inside the lab.
