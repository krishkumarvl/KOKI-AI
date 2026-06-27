# memory/manager.py — Project KOKI
import json
import os
from config import MEMORY_FILE, JSON_MEMORY_FILE

# ─── Plain-text Memory (memory.txt) ───────────────────────────────────────────

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def save_memory(text):
    try:
        with open(MEMORY_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError as e:
        print(f"KOKI: Memory file me likhne me dikkat aa gayi — {e}")

def forget_memory(to_forget):
    memories = load_memory()
    updated  = [m for m in memories if to_forget.lower() not in m.lower()]

    if len(updated) < len(memories):
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                f.writelines(updated)
            return f"Bhool gaya — '{to_forget}' memory se hata diya.", True
        except OSError as e:
            return f"Memory update nahi ho payi — {e}", False
    else:
        return f"Yeh toh mujhe yaad hi nahi tha: '{to_forget}'", False

# ─── JSON Memory (koki_memory.json) ───────────────────────────────────────────

def load_json_memory():
    if not os.path.exists(JSON_MEMORY_FILE):
        return {}
    try:
        with open(JSON_MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"KOKI: Memory file corrupt lag rahi hai ({e}). Fresh start.")
        return {}

def save_json_memory(memory_data):
    try:
        with open(JSON_MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory_data, f, indent=4)
    except OSError as e:
        print(f"KOKI: Memory save fail ho gaya — {e}")

# ─── Interest Detection ────────────────────────────────────────────────────────

def detect_interest(msg):
    msg = msg.strip()
    if msg.startswith("i like "):
        return msg.replace("i like ", "", 1).strip() or None
    if msg.startswith("i love "):
        return msg.replace("i love ", "", 1).strip() or None
    if "pasand hai" in msg:
        return msg.replace("mujhe", "").replace("pasand hai", "").strip() or None
    return None

def add_interest(user_memory, interest):
    if "interests" not in user_memory:
        user_memory["interests"] = []
    if interest not in user_memory["interests"]:
        user_memory["interests"].append(interest)
        return True
    return False

# ─── Chat History ─────────────────────────────────────────────────────────────

def append_turn(user_memory, user_msg, koki_reply=""):
    if "chat_history" not in user_memory:
        user_memory["chat_history"] = []
    user_memory["chat_history"].append({"user": user_msg, "koki": koki_reply})
    user_memory["chat_history"] = user_memory["chat_history"][-20:]

def update_last_reply(user_memory, koki_reply):
    history = user_memory.get("chat_history", [])
    if history:
        history[-1]["koki"] = koki_reply