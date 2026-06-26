from google import genai

# apni API key yaha temporarily paste kr
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Introduce yourself as KOKI, an AI assistant."
)

print(response.text)