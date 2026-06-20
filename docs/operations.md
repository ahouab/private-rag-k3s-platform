# Operations Runbook

## Daily checks

```bash
kubectl get nodes
kubectl get pods -A
kubectl -n storage get volumes.longhorn.io
kubectl -n argocd get applications
```

## Load models

```bash
kubectl -n ai-system exec -it deploy/ollama -- ollama pull llama3.1:8b
kubectl -n ai-system exec -it deploy/ollama -- ollama pull mistral:7b
kubectl -n ai-system exec -it deploy/ollama -- ollama pull nomic-embed-text
```

## RAG API smoke test

```bash
curl http://rag-api.lab.local/health
curl -X POST http://rag-api.lab.local/query \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is this platform?","top_k":3}'
```
