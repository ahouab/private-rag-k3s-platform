#!/usr/bin/env bash
set -euo pipefail

kubectl get nodes -o wide
kubectl get pods -A
kubectl -n argocd get applications
kubectl get storageclass
kubectl -n ai-system get pods
kubectl -n rag get pods
kubectl -n observability get pods
