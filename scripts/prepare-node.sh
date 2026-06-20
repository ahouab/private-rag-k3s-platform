#!/usr/bin/env bash
set -euo pipefail

sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget git vim htop jq net-tools nfs-common open-iscsi ca-certificates gnupg lsb-release qemu-guest-agent
sudo systemctl enable --now qemu-guest-agent
sudo systemctl enable --now iscsid
sudo swapoff -a
sudo sed -i '/ swap / s/^/#/' /etc/fstab
cat <<EOM | sudo tee /etc/modules-load.d/k3s.conf
br_netfilter
overlay
EOM
sudo modprobe br_netfilter
sudo modprobe overlay
cat <<EOM | sudo tee /etc/sysctl.d/99-k3s.conf
net.bridge.bridge-nf-call-iptables=1
net.bridge.bridge-nf-call-ip6tables=1
net.ipv4.ip_forward=1
EOM
sudo sysctl --system
