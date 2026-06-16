# Project KOKI — Day 4
# Dictionary brain + session memory + file memory
   #random isiliye use kra taki thoda robotic feel na aaye....
from datetime import datetime
import random
import google.generativeai as genai
MEMORY_FILE = "memory.txt"
# Gemini Setup
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

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
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return file.readline().strip()
    except FileNotFoundError:
        return ""

def save_memory(text):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        file.write(text + "\n")

        #=========main functions =========

def greet():
    print("=" * 40)
    print("   KOKI v1 - Your Personal AI")
    print("   Built by Krish Kumar")
    print("=" * 40)
    name = input("KOKI: What's your name? ")
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

def ask_gemini(question):

    try:

        response = model.generate_content(question)

        return response.text

    except Exception as e:

        return "Sorry bhai, Gemini se connect nahi ho pa raha."

def respond(msg, name):
    global conversation_count
    conversation_count += 1
    #matching ke liye use kra lower case ka taki Hello ya Fir hello same lage
    msg = msg.lower().strip()

    #======remember commands========
    #agar user ne koi aisi baat kahi jo KOKI ko yaad rakhni chahiye, toh usko identify karke memory me save krna hoga
    if msg.startswith("remember "):
        memory = msg.replace("remember ", "")

        with open(MEMORY_FILE, "a") as file:
            file.write(memory + "\n")

        print("KOKI: I'll remember that.")
        return True
    
    #=========Recall Memory========
    #agar user ne koi aisi baat kahi jo KOKI ko yaad karni chahiye, toh usko identify karke memory se recall krna hoga
    if msg == "what do you remember":
        try:
            with open(MEMORY_FILE, "r") as file:
                memories = file.readlines()

            print("KOKI: Here's what I remember:")

            for memory in memories[1:]:
                print("- " + memory.strip())

        except:
            print("KOKI: I don't remember anything yet.")

        return True
    
    matched = False

    # dictionary matching
    # user ke message me keyword dhundho
    # fir us keyword ka random response do

    for key in responses:
        if key in msg:

            reply = random.choice(responses[key])

            # populate dynamic time if needed
            if "{time}" in reply:
                reply = reply.format(time=get_time())

            print("KOKI: " + reply)

            matched = True

            if conversation_count == 5:
                print("KOKI: 5 messages already " + name + ". I like talking to you.")

            break

    if not matched:
          print("KOKI: Hmm... mujhe ye dictionary me nahi mila.")
    print("KOKI: Gemini se puch raha hoon...")

    gemini_reply = ask_gemini(msg)

    print("KOKI:", gemini_reply)


    return True

# Start
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