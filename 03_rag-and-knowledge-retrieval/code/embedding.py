from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("ERROR: API Key not found")

client = genai.Client(api_key=gemini_api_key)

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents='Refund requests are allowed witin 7 days.'
)

# print(result.embeddings)
vector = result.embeddings[0].values
print(vector)