# app.py — KOKI Web UI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# KOKI core imports
from config import RESPONSES, EXIT_WORDS
from brain.browser import open_website
from brain.calculator import calculate
from brain.gemini import ask_gemini
from brain.music import play_on_youtube_music
from brain.git_tool import git_commit
from brain.search_tool import web_search
from memory.manager import (
    load_json_memory, save_json_memory,
    load_memory, save_memory,
    forget_memory,
    detect_interest, add_interest,
    append_turn, update_last_reply,
)
import random
from datetime import datetime

# ─── Setup ────────────────────────────────────────────────────────────────────
app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")
user_memory = load_json_memory()

# ─── Request Model ────────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    message: str

# ─── Helper ───────────────────────────────────────────────────────────────────
def get_time():
    return datetime.now().strftime("%I:%M %p")

# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    name = user_memory.get("name", "")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "name": name
        }
    )
@app.post("/chat")
async def chat(req: ChatRequest):
    msg = req.message.strip().lower()
    
    if not msg:
        return JSONResponse({"reply": "Kuch toh likh bhai!"})

    append_turn(user_memory, msg)

    # Interest detection
    interest = detect_interest(msg)
    if interest:
        added = add_interest(user_memory, interest)
        reply = f"Noted! I know you like {interest} now." if added else f"Haan haan, pata hai mujhe!"
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    # Commands
    if msg == "what do you know about me":
        name = user_memory.get("name", "")
        interests = ", ".join(user_memory.get("interests", []))
        notes = load_memory()
        reply = f"Name: {name}\nInterests: {interests}\nNotes: {chr(10).join(notes)}"
        return JSONResponse({"reply": reply})

    if msg.startswith("remember "):
        memory = msg.replace("remember ", "", 1).strip()
        save_memory(memory)
        reply = "I'll remember that."
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg.startswith("forget "):
        to_forget = msg.replace("forget ", "", 1).strip()
        reply, _ = forget_memory(to_forget)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg.startswith("play "):
        query = msg.replace("play ", "", 1).strip()
        reply = play_on_youtube_music(query)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg.startswith("search "):
        query = msg.replace("search ", "", 1).strip()
        reply = web_search(query)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg.startswith("git commit "):
        message = msg.replace("git commit ", "", 1).strip()
        reply = git_commit(message)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg == "time":
        reply = f"Current time is {get_time()}"
        return JSONResponse({"reply": reply})
    if msg.startswith("open "):
        site = msg.replace("open ", "", 1).strip()
        reply = open_website(site)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    if msg.startswith("calculate "):
        expression = msg.replace("calculate ", "", 1).strip()
        reply = calculate(expression)
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    # Dictionary match
    if msg in RESPONSES:
        reply = random.choice(RESPONSES[msg])
        update_last_reply(user_memory, reply)
        save_json_memory(user_memory)
        return JSONResponse({"reply": reply})

    # Gemini fallback
    reply = ask_gemini(msg, user_memory)
    update_last_reply(user_memory, reply)
    save_json_memory(user_memory)
    return JSONResponse({"reply": reply})

@app.post("/set-name")
async def set_name(req: dict):
    name = req.get("name", "").strip()
    if name:
        user_memory["name"] = name
        save_json_memory(user_memory)
        return JSONResponse({"status": "ok", "name": name})
    return JSONResponse({"status": "error"})