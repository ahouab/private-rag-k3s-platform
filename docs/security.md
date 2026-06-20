# Security Model

## Controls

- Namespace isolation
- NetworkPolicies
- TLS ingress
- Kubernetes secret encryption
- Sealed Secrets or External Secrets planned
- Trivy Operator for image and workload scanning
- SBOM generation with Syft planned in CI
- No outbound dependency on public LLM APIs

## Required Hardening

1. Replace default MinIO credentials.
2. Enforce authentication on Open WebUI.
3. Add NetworkPolicies for Ollama, MinIO and PostgreSQL.
4. Configure backup encryption.
5. Add audit logs for ingestion and query requests.
6. Pin container image tags.
