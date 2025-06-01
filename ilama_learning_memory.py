import os
import json

LEARNING_MEMORY_FILE = "ilama_learning_memory.json"
if os.path.exists(LEARNING_MEMORY_FILE):
    with open(LEARNING_MEMORY_FILE, "r", encoding="utf-8") as f:
        learned_memory = json.load(f)
else:
    learned_memory = {}

def save_learning_memory():
    with open(LEARNING_MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(learned_memory, f, indent=2, ensure_ascii=False)

def update_learning_memory(key, value):
    if key in learned_memory:
        if isinstance(learned_memory[key], list):
            learned_memory[key].append(value)
        else:
            learned_memory[key] = [learned_memory[key], value]
    else:
        learned_memory[key] = value
    save_learning_memory()