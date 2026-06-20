# K3s HA installation on Proxmox

## Node plan

- k3s-master-01: 192.168.50.11
- k3s-master-02: 192.168.50.12
- k3s-master-03: 192.168.50.13
- k3s-worker-ai-01: 192.168.50.21

## First server

```bash
curl -sfL https://get.k3s.io | sh -s - server \
  --cluster-init \
  --node-name k3s-master-01 \
  --write-kubeconfig-mode 644 \
  --secrets-encryption
```

## Additional servers

```bash
curl -sfL https://get.k3s.io | K3S_TOKEN="<TOKEN>" sh -s - server \
  --server https://192.168.50.11:6443 \
  --node-name k3s-master-02 \
  --write-kubeconfig-mode 644 \
  --secrets-encryption
```

## Worker AI node

```bash
curl -sfL https://get.k3s.io | K3S_TOKEN="<TOKEN>" sh -s - agent \
  --server https://192.168.50.11:6443 \
  --node-name k3s-worker-ai-01
```

## Labels and taints

```bash
kubectl label node k3s-worker-ai-01 workload=rag
kubectl taint node k3s-worker-ai-01 dedicated=ai:NoSchedule
```
