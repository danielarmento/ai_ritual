#!/bin/bash
cd "$(dirname "$0")"

echo "Starting AI Ritual..."
python3 ritual_display.py &

sleep 1
echo "[*] Training neural spirit..."
python3 train.py

echo "[*] Demonstration begins..."
python3 demo.py
