#!/bin/bash
cd "$(dirname "$0")"

echo "Starting AI Ritual..."
nohup python3 ritual_display.py > /dev/null 2>&1 &

sleep 2
echo "[*] Training neural spirit..."
python3 train.py

echo "[*] Demonstration begins..."
python3 demo.py
