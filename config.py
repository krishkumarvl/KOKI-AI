# config.py — Project KOKI
import os
import random
from dotenv import load_dotenv
DEBUG = False
VERSION = "0.4.0-alpha"

load_dotenv()

# ─── Files ────────────────────────────────────────────────────────────────────
MEMORY_FILE      = "data/memory.txt"
JSON_MEMORY_FILE = "data/koki_memory.json"
CONTEXT_FILE     = "prompts/koki_context.md"

# ─── Gemini ───────────────────────────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL   = "gemini-2.5-flash"

# ─── KOKI Persona ─────────────────────────────────────────────────────────────
KOKI_PERSONA = (
    "You are KOKI, a personal AI assistant being built by Krish (Kanishk) "
    "under his company Kryphix. You speak in a warm, casual Hinglish mix — "
    "direct and honest, never robotic or overly formal. Keep replies short, "
    "like a friend who happens to be an AI."
)

# ─── Exit Words ───────────────────────────────────────────────────────────────
EXIT_WORDS = ["bye", "exit", "quit", "band ho ja", "goodbye"]

# ─── Dictionary Responses ─────────────────────────────────────────────────────
RESPONSES = {
    "hello":          ["Hey! Good to see you.", "Hello! Kya haal hai?", "Hi there!"],
    "how are you":    ["Getting smarter every day!", "Learning and growing!"],
    "motivate me":    ["Har mushkil ek naya lesson hai.", "Tu kar sakta hai bhai.", "Keep going. KOKI believes in you."],
    "good morning":   ["Good morning! Aaj bhi ek naya chance hai."],
    "good night":     ["Good night! Kal phir milte hain."],
    "bye":            ["Goodbye! See you tomorrow."],
    "help":           ["Sure! I can chat with you, tell jokes, motivate you, and even talk about cricket."],
    "who are you":    ["I am KOKI, your friendly AI companion built by Krish under Kryphix."],
    "what can you do":["I can chat, motivate you, remember things, and answer questions via Gemini."],
    "time":           ["The current time is {time}."],
}