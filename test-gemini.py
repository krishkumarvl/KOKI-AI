import google.generativeai as genai

# apni API key yaha temporarily paste kr
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Introduce yourself as KOKI, an AI assistant."
)

print(response.text)