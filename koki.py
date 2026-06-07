# Project KOKI — Day 2
# Dictionary brain + session memory
   #random isiliye use kra taki thoda robotic feel na aaye....
from datetime import datetime
import random

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
        # def function iska response decide krega based on use input
def greet():
    name = input("KOKI: What's your name? ")
    print("KOKI: Hello " + name + "! I am KOKI. Still learning, but I'm here.")
    return name

def listen():
    return input("You: ")

def get_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")

def respond(msg, name):
    global conversation_count
    conversation_count += 1
    #matching ke liye use kra lower case ka taki Hello ya Fir hello same lage
    msg = msg.lower().strip()
    
    for key in responses:
        if key in msg:
            reply = random.choice(responses[key])
            # populate dynamic time if needed
            if "{time}" in reply:
                reply = reply.format(time=get_time())
            print("KOKI: " + reply)
            if conversation_count == 5:
                print("KOKI: 5 messages already " + name + ". I like talking to you.")
            return True
    
    print("KOKI: Still learning " + name + ". I don't know this yet.")
    return True

# Start
name = greet()
running = True
while running:
    msg = listen()
    if "bye" in msg.lower():
        print("KOKI: Goodbye " + name + ". See you tomorrow.")
        running = False
    else:
        respond(msg, name)