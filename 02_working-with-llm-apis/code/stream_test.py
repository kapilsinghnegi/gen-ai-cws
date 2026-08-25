from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api_key)

stream = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="""
    Explain how AI works to a complete beginner with real-life examples and analogies
    """,
    stream=True
)

for event in stream:
    if event.event_type == 'step.delta':
        if event.delta.type == 'text':
            print(event.delta.text, end="", flush=True)