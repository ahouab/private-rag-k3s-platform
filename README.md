# Private RAG Platform on K3s / Proxmox

Sovereign AI platform with local LLM, vector search, GitOps, observability and Kubernetes-native operations.

## Purpose

This repository implements a private Retrieval-Augmented Generation platform running on a Proxmox-based K3s lab.

The target is a production-grade demonstrator for private AI workloads:

- K3s HA on Proxmox
- Longhorn distributed storage
- Argo CD GitOps deployment
- Traefik ingress and TLS
- Ollama local LLM runtime
- Qdrant vector database
- MinIO document storage
- Optional PostgreSQL metadata store
- Open WebUI user interface
- FastAPI RAG backend
- Prometheus, Grafana and Loki observability
- Trivy security scanning
- NetworkPolicies and secret management

## Target Architecture

```text
User
  -> DNS / Traefik / TLS
  -> Open WebUI
  -> RAG API
  -> Qdrant vector search
  -> Ollama local LLM
  -> MinIO document storage
  -> Grafana / Loki / Prometheus observability
```

## Lab Topology

| Node | Role | Usage |
|---|---|---|
| k3s-master-01 | server + etcd | control plane |
| k3s-master-02 | server + etcd | control plane |
| k3s-master-03 | server + etcd | control plane |
| k3s-worker-ai-01 | agent | LLM, RAG, embeddings |

## Quick Start

```bash
kubectl apply -f clusters/proxmox-lab/namespaces.yaml
kubectl apply -n argocd -f clusters/proxmox-lab/app-of-apps.yaml
```

## Repository Structure

```text
clusters/          Cluster bootstrap and Argo CD root app
apps/              Argo CD application definitions
values/            Helm values for platform components
manifests/         Shared Kubernetes manifests
rag-api/           FastAPI private RAG backend
docs/              Architecture, operations, security and demo documentation
scripts/           Bootstrap and validation scripts
.github/workflows/ CI pipeline
```

## Demonstration Scenarios

1. Ingest internal documents into MinIO and Qdrant.
2. Ask questions through the RAG API.
3. Generate answers with source references using Ollama.
4. Prove that data remains inside the private lab.
5. Monitor latency, errors and resource usage from Grafana.

## Commercial Positioning

Private RAG platform for organizations that need sovereign AI, data confidentiality, Kubernetes-native operations and production-grade observability.


Walter Assets Trademark
