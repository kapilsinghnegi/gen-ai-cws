from google import genai
from dotenv import load_dotenv
import os 
import numpy as np

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("ERROR: API Key not found")

client = genai.Client(api_key=gemini_api_key)
text1 = "Refund requests are allowed within 7 days."
text2 = "Can I get my money back after 5 days?"

result1 = client.models.embed_content(
    model="gemini-embedding-2",
    contents = text1
)

result2 = client.models.embed_content(
    model="gemini-embedding-2",
    contents = text2
)

vector1 = result1.embeddings[0].values
# print(len(vector1))
vector2 = result2.embeddings[0].values
# print(len(vector2))

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

score = cosine_similarity(vector1, vector2)
print(score)