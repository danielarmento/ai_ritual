#!/bin/bash
set -e

echo "[*] Updating system..."
sudo apt update -y

echo "[*] Installing Python + Pip..."
sudo apt install -y python3 python3-pip figlet

echo "[*] Installing numpy..."
pip3 install numpy --break-system-packages

echo "[*] Installation complete."
