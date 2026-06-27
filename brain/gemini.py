# brain/gemini.py — Project KOKI
import json
import time
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL, CONTEXT_FILE

if not GEMINI_API_KEY:
    print("KOKI: GEMINI_API_KEY .env me nahi mili. Gemini fallback off rahega.")

_client = genai.Client(api_key=GEMINI_API_KEY)

def _load_context():
    try:
        with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def _build_prompt(question, user_memory):
    project_context = _load_context()

    memory_summary = {
        "name":      user_memory.get("name", ""),
        "interests": user_memory.get("interests", [])
    }
    memory_context = json.dumps(memory_summary, indent=4, ensure_ascii=False)

    recent_history = user_memory.get("chat_history", [])[-6:-1]
    conv_window    = ""
    for turn in recent_history:
        if isinstance(turn, dict):
            conv_window += f"User: {turn.get('user', '')}\n"
            if turn.get("koki"):
                conv_window += f"KOKI: {turn.get('koki', '')}\n"

    name       = user_memory.get("name", "")
    user_ctx   = f"Current User Name: {name}" if name else ""
    conv_block = conv_window if conv_window else "No previous conversation this session."

    return f"""
{project_context}

------------------------

User Profile

{memory_context}

------------------------

{user_ctx}

------------------------

Recent Conversation (last 5 turns):

{conv_block}

------------------------

Current User Question:

{question}

------------------------

Instructions:

- You are KOKI.
- Never say you are Gemini.
- Never mention Google.
- Never mention context files.
- Don't introduce yourself unless asked.
- Don't greet in every response.
- Keep answers short unless the user asks for detail.
- If you already know the user's name, don't repeat it unnecessarily.
- Use the recent conversation above to understand follow-up questions.
- Behave like a personal AI assistant.
"""

def ask_gemini(question, user_memory, retries=2, delay=3):
    prompt = _build_prompt(question, user_memory)

    for attempt in range(retries + 1):
        try:
            response = _client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )
            return response.text.strip()

        except Exception as e:
            error = str(type(e).__name__)
            if "ResourceExhausted" in error:
                if attempt < retries:
                    print(f"KOKI: Rate limit aa gaya, {delay}s baad retry karunga...")
                    time.sleep(delay)
                else:
                    return "Sorry bhai, Gemini ka rate limit aa gaya. Thodi der baad try karo."
            elif "ServiceUnavailable" in error:
                return "Sorry bhai, Gemini abhi available nahi hai."
            elif "InvalidArgument" in error:
                return "Kuch toh gadbad hai — shayad API key galat hai?"
            else:
                return f"Sorry bhai, kuch unexpected ho gaya — {error}."