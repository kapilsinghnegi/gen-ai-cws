from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api_key)

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="""
    Explain how AI works in detail.
    """,
    generation_config = {
        "temperature": 1.0,
        "max_output_tokens": 50
    }
)

print(interaction.output_text)