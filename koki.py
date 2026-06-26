# Project KOKI — Week 2, Day 8 (core stabilized)
# Dictionary brain + session memory + file memory
   #random isiliye use kra taki thoda robotic feel na aaye....
from datetime import datetime
import random
import re
import json
import os
from google import genai
MEMORY_FILE = "memory.txt"
JSON_MEMORY_FILE = "koki_memory.json"
# Gemini Setup
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("KOKI: GEMINI_API_KEY .env me nahi mili. Gemini fallback off rahega.")

client = genai.Client(api_key=GEMINI_API_KEY)
GEMINI_MODEL = "gemini-2.5-flash"

# KOKI ki personality — har Gemini call ko yeh context milta hai
# taki fallback answers bhi KOKI jaise lage, generic Gemini jaise nahi
KOKI_PERSONA = (
    "You are KOKI, a personal AI assistant being built by Krish (Kanishk) "
    "under his company Kryphix. You speak in a warm, casual Hinglish mix — "
    "direct and honest, never robotic or overly formal. Keep replies short, "
    "like a friend who happens to be an AI."
)

responses = { #bahut se random responses daal diye ab ek word pr iske pass 3 alag alag response ho skte hai for exam hello type krne pr hi there bhi aa skta hai aur kya haal hai bhi...{aage dikkat nhi aani chahiye}
    "hello": ["Hey! Good to see you.", "Hello! Kya haal hai?", "Hi there!"],
    "how are you": ["Getting smarter every day!", "Learning and growing!"],
    "motivate me": ["Har mushkil ek naya lesson hai.", "Tu kar sakta hai bhai.", "Keep going. KOKI believes in you."],
    "good morning": ["Good morning! Aaj bhi ek naya chance hai."],
    "good night": ["Good night! Kal phir milte hain."],
    "army": ["Indian Army — ek legacy, ek commitment. Jai Hind."],
    "koki": ["Haan bhai, main hoon. KOKI. Tera apna AI."],
    "bye": ["Goodbye! See you tomorrow."],
    "cricket": ["Cricket is a popular sport in India. Who is your favorite cricketer?"],
    "rohit": ["Rohit Sharma is a great cricketer! He is known for his powerful batting and has many records to his name."],
    "virat": ["Virat Kohli is one of the best cricketers in the world! He is known for his aggressive batting style and has been a key player for India."],
    "ms dhoni": ["MS Dhoni is a legendary cricketer! He is known for his calm demeanor and excellent leadership skills. He has led India to many victories."],
    "how's the josh": ["high, sir! hmesha ready...uri ka yeh dialogue aur vicky ki performance dono kya hi acha experience thi!"],
    "help": ["Sure! I can chat with you, tell jokes, motivate you, and even talk about cricket. Just type something and I'll do my best to respond!"],
    "who are you": ["i am KOKI, your friendly AI companion. I'm here to chat, share jokes, motivate you, and talk about cricket. Let's have some fun together!"],
    "what can you do": ["I can chat with you, tell jokes, motivate you, and even talk about cricket. Just type something and I'll do my best to respond!"],
    "ek joke suna": ["ek baar ki baat hai, paanch dost manali ki trip ka plan bna rhe the."],
    "phir aagay kya hua": ["aagey kya hota bas plan hi bnate reh gye."],
    "time": ["The current time is {time}."],

    }

conversation_count = 0

def find_dictionary_match(msg):
    # word-boundary match — "time" ab "sometimes" ke andar trigger nahi hoga
    for key in responses:
        pattern = r'\b' + re.escape(key) + r'\b'
        if re.search(pattern, msg):
            return key
    return None

# KOKI ko band krne ke multiple commands
exit_words = [
    "bye",
    "exit",
    "quit",
    "band ho ja",
    "goodbye"
]
        # def function iska response decide krega based on use input 
        #sabse pehle memory functions yeh store krenge aur fir dictionary based responses denge
        #========memory functions=========

def load_memory():
    # ab yeh saari remembered lines return karta hai, sirf pehli line nahi
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_memory(text):
    # "a" mode — purani memories overwrite nahi hongi, naya append hoga
    try:
        with open(MEMORY_FILE, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except OSError as e:
        print(f"KOKI: Memory file me likhne me dikkat aa gayi — {e}")

        #========= JSON Memory =========
# important user information yaha store hogi
def load_json_memory():
    if not os.path.exists(JSON_MEMORY_FILE):
        return {}
    try:
        with open(JSON_MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as e:
        print(f"KOKI: Memory file corrupt ya unreadable lag rahi hai ({e}). Fresh start kar raha hoon.")
        return {}

def save_json_memory(memory_data):
    try:
        with open(JSON_MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memory_data, file, indent=4)
    except OSError as e:
        print(f"KOKI: Memory save fail ho gaya — {e}")

user_memory = load_json_memory()

        #=========main functions =========

def greet():
    print("=" * 40)
    print("   KOKI v1 - Your Personal AI")
    print("   Built by Krish Kumar")
    print("=" * 40)
    # agar pehle se naam save hai
    if "name" in user_memory:
        name = user_memory["name"]
        print(f"KOKI: Welcome back {name}!")
    else:
        name = input("KOKI: What's your name? ")
        user_memory["name"] = name
        save_json_memory(user_memory)
        print("KOKI: Nice to meet you " + name + "!")
        print("KOKI: Hello " + name + "! I am KOKI.")
        print("KOKI: I understand " + str(len(responses)) + " topics right now.")
        print("KOKI: And I'm learning more every day.")

    return name

def listen():
    return input("You: ")

def get_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")
#========= Gemini Function =========
# agar dictionary ko answer nahi pata hoga
# to KOKI Gemini se puchega

def ask_gemini(question, name=None):

    try:
        context = f"The user's name is {name}. " if name else ""
        prompt = f"{KOKI_PERSONA}\n{context}\nUser: {question}\nKOKI:"

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return "Sorry bhai, Gemini se connect nahi ho pa raha. Thodi der baad try karna."

def respond(msg, name):
    global conversation_count
    #matching ke liye use kra lower case ka taki Hello ya Fir hello same lage
    msg = msg.lower().strip()

    if not msg:
        print("KOKI: Kuch toh likh bhai, main padhu kya?")
        return True

    conversation_count += 1
    if "chat_history" not in user_memory:
        user_memory["chat_history"] = []

    user_memory["chat_history"].append(msg)

    user_memory["chat_history"] = user_memory["chat_history"][-20:]

    save_json_memory(user_memory)
    #========= Interest Memory =========
# user ki pasand yaad rakho
    if msg.startswith("i like"):

        interest = msg.replace("i like", "").strip()

        if interest:

            if "interests" not in user_memory:
                user_memory["interests"] = []

            if interest not in user_memory["interests"]:
                user_memory["interests"].append(interest)
                save_json_memory(user_memory)

            print(f"KOKI: Noted! I know you like {interest} now.")

        else:
            print("KOKI: Like kya karta hai bata toh sahi bhai.")

        return True
    
    #========= User Profile =========

    if msg == "what do you know about me":

        print("KOKI: Here's what I know about you:")

        if "name" in user_memory:

            print("- Name:", user_memory["name"])

        if "interests" in user_memory:

            print("- Interests:", ", ".join(user_memory["interests"]))

        return True

    #======remember commands========
    #agar user ne koi aisi baat kahi jo KOKI ko yaad rakhni chahiye, toh usko identify karke memory me save krna hoga
    if msg.startswith("remember "):
        memory = msg.replace("remember ", "", 1).strip()

        if memory:
            save_memory(memory)
            print("KOKI: I'll remember that.")
        else:
            print("KOKI: Remember kya karu bhai, bata toh sahi.")
        return True
    
    if msg == "show history":
        print("KOKI: Recent conversations:")
        for item in user_memory.get("chat_history", []):
            print("-", item)
        return True
    
    #=========Recall Memory========
    #agar user ne koi aisi baat kahi jo KOKI ko yaad karni chahiye, toh usko identify karke memory se recall krna hoga
    if msg == "what do you remember":
        memories = load_memory()

        if memories:
            print("KOKI: Here's what I remember:")
            for memory in memories:
                print("- " + memory.strip())
        else:
            print("KOKI: I don't remember anything yet.")

        return True

    #========= Dictionary Matching =========
    # user ke message me keyword dhundho (ab word-boundary safe)
    matched_key = find_dictionary_match(msg)

    if matched_key:
        reply = random.choice(responses[matched_key])

        # dynamic time replace karne ke liye
        if "{time}" in reply:
            reply = reply.format(time=get_time())

        print("KOKI: " + reply)

        if conversation_count == 5:
            print("KOKI: 5 messages already " + name + ". I like talking to you.")

        return True

    #========= Gemini Fallback =========
    # agar dictionary me answer nahi mila
    # to Gemini se pucho
    print("KOKI: Hmm... mujhe ye dictionary me nahi mila.")
    print("KOKI: Gemini se puch raha hoon...")

    gemini_reply = ask_gemini(msg, name)

    print("KOKI:", gemini_reply)

    return True

# Start
def main():
    name = greet()
    running = True

    while running:
        msg = listen()

        # agar user kisi bhi exit word ka use kre
        # to KOKI band ho jayega

        if any(word in msg.lower() for word in exit_words):

            print("KOKI: Goodbye " + name + ". See you tomorrow.")
            running = False

        else:
            respond(msg, name)

if __name__ == "__main__":
    main()