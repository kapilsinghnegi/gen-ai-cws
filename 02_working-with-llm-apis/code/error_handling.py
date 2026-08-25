from google import genai
from google.genai import errors 
from dotenv import load_dotenv
import os 

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Explain AI in 20-30 words."
    )
    print(response.text)
    
except errors.APIError as e:
    print("Gemini API Error: ", e.code)
    print(e.message)