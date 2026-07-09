# main.py — Project KOKI Week 4
import re
import random
from datetime import datetime
from config import VERSION
from brain.tool_registry import TOOLS
from brain.tool_executor import execute_tool
from brain.preprocess import normalize_message
from brain.search_tool import web_search
from brain.music import play_on_youtube_music
from brain.git_tool import git_commit
from brain.browser import open_website
from brain.tool_router import detect_tool
from config import RESPONSES, EXIT_WORDS
from brain.gemini import ask_gemini
from memory.manager import (
    load_json_memory, save_json_memory,
    load_memory,      save_memory,
    forget_memory,
    detect_interest,  add_interest,
    append_turn,      update_last_reply,
)

# ─── Globals ──────────────────────────────────────────────────────────────────
user_memory        = load_json_memory()
conversation_count = 0

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_time():
    return datetime.now().strftime("%I:%M %p")

def find_dictionary_match(msg):
    msg = msg.strip().lower()

    # Exact match only
    if msg in RESPONSES:
        return msg

    return None

# ─── Greet ────────────────────────────────────────────────────────────────────

def greet():
    print("=" * 40)
    print(f"KOKI {VERSION} - Your Personal AI")
    print("   Built by Krish Kumar")
    print("=" * 40)

    if "name" in user_memory:
        name = user_memory["name"]
        print(f"KOKI: Welcome back {name}!")
    else:
        name = input("KOKI: What's your name? ")
        user_memory["name"] = name
        save_json_memory(user_memory)
        print(f"KOKI: Nice to meet you {name}!")
        print(f"KOKI: Hello {name}! I am KOKI.")
        print(f"KOKI: I understand {len(RESPONSES)} topics right now.")
        print("KOKI: And I'm learning more every day.")

    return name

# ─── Respond ──────────────────────────────────────────────────────────────────

def respond(msg, name):
    global conversation_count

    msg_lower = normalize_message(msg)
        # Detect if user wants to use a tool
    tool = detect_tool(msg_lower)

    if not msg_lower:
        print("KOKI: Kuch toh likh bhai, main padhu kya?")
        return

    conversation_count += 1
    append_turn(user_memory, msg_lower)

    # ── interest detection ──
    interest = detect_interest(msg_lower)
    if interest:
        added = add_interest(user_memory, interest)
        reply = f"Noted! I know you like {interest} now." if added else f"Haan haan, pata hai mujhe ki tu {interest} pasand karta hai."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return

    if msg_lower.strip() in ["i like", "i love"]:
        print("KOKI: Like kya karta hai bata toh sahi bhai.")
        return

    # ── what do you know about me ──
    if msg_lower == "what do you know about me":
        print("KOKI: Here's what I know about you:")
        if "name" in user_memory:
            print("  - Name:", user_memory["name"])
        if user_memory.get("interests"):
            print("  - Interests:", ", ".join(user_memory["interests"]))
        notes = load_memory()
        if notes:
            print("  - Notes:")
            for note in notes:
                print("    •", note.strip())
        update_last_reply(user_memory, "Showed profile.")
        save_json_memory(user_memory)
        return

    # ── remember ──
    if msg_lower.startswith("remember "):
        memory = msg_lower.replace("remember ", "", 1).strip()
        if memory:
            save_memory(memory)
            reply = "I'll remember that."
        else:
            reply = "Remember kya karu bhai, bata toh sahi."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return
    
    # ── web search ──
    if tool == "search":
        query = msg_lower.replace("search ", "", 1).strip()
        if query:
            reply = web_search(query)
        else:
            reply = "Kya search karun bhai, bata toh sahi."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return
    
    # ── git commit ──
    if tool == "git":
        message = msg_lower.replace("git commit ", "", 1).strip()
        if message:
            reply = git_commit(message)
        else:
            reply = "Commit message toh de bhai."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return
    
    # ── play music ──
    if tool == "music":
        query = msg_lower.replace("play ", "", 1).strip()
        if query:
            reply = play_on_youtube_music(query)
        else:
            reply = "Kya play karun bhai, bata toh sahi."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return
    
    # ── open website ──
    if tool == "browser":
        site = msg_lower.replace("open ", "", 1).strip()
        reply = open_website(site)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return

    # ── forget ──
    if msg_lower.startswith("forget "):
        to_forget = msg_lower.replace("forget ", "", 1).strip()
        reply, _ = forget_memory(to_forget)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        return

    # ── show history ──
    if msg_lower == "show history":
        print("KOKI: Recent conversations:")
        for item in user_memory.get("chat_history", []):
            if isinstance(item, dict):
                print(f"  You:  {item.get('user', '')}")
                if item.get("koki"):
                    print(f"  KOKI: {item.get('koki', '')}")
            else:
                print("  -", item)
        update_last_reply(user_memory, "Showed history.")
        save_json_memory(user_memory)
        return

    # ── what do you remember ──
    if msg_lower == "what do you remember":
        memories = load_memory()
        if memories:
            print("KOKI: Here's what I remember:")
            for m in memories:
                print("  -", m.strip())
        else:
            print("KOKI: I don't remember anything yet.")
        update_last_reply(user_memory, "Showed memories.")
        save_json_memory(user_memory)
        return
    
    if msg_lower == "version":
       print("KOKI:", VERSION)
       return

    # ── dictionary match ──
    matched_key = find_dictionary_match(msg_lower)
    if matched_key:
        reply = random.choice(RESPONSES[matched_key])
        if "{time}" in reply:
            reply = reply.format(time=get_time())
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        print(f"KOKI: {reply}")
        if conversation_count == 5:
            print(f"KOKI: 5 messages already {name}. I like talking to you.")
        return

    # ── Gemini fallback ──
    gemini_reply = ask_gemini(msg_lower, user_memory)
    update_last_reply(user_memory, gemini_reply)
    save_json_memory(user_memory)
    print(f"KOKI: {gemini_reply}")

# ─── Main Loop ────────────────────────────────────────────────────────────────

def main():
    name    = greet()
    running = True

    while running:
        msg = input("You: ")
        if any(word in msg.lower() for word in EXIT_WORDS):
            print(f"KOKI: Goodbye {name}. See you tomorrow.")
            running = False
        else:
            respond(msg, name)

if __name__ == "__main__":
    main()