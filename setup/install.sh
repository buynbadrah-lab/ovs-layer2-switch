#!/bin/bash

set -e

echo "Updating package list..."
sudo apt update

echo "Installing required packages..."

sudo apt install -y \
    openvswitch-switch \
    mininet \
    python3 \
    python3-pip \
    wireshark \
    iperf \
    git \
    tree

echo ""
echo "Installation completed."

echo ""
echo "Checking versions..."

ovs-vsctl --version
mn --version
python3 --version
iperf --version
