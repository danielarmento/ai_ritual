import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return {"logs": [], "knowledge": {}}
    return {"logs": [], "knowledge": {}}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def log_event(memory, text):
    memory["logs"].append(text)
    if len(memory["logs"]) > 300:
        memory["logs"].pop(0)  # rolling memory
    save_memory(memory)

def store_knowledge(memory, key, value):
    memory["knowledge"][key] = value
    save_memory(memory)

def recall(memory, key, default=None):
    return memory["knowledge"].get(key, default)
