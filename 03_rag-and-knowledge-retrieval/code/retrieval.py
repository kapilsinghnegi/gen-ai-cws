from google import genai
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("ERROR: API Key not found")

client = genai.Client(api_key=gemini_api_key)
documents = [
    "Refund requests are allowed within 7 days.",
    "Python classes happen monday to friday",
    "Students get at least 3 interview opportunities",
    "Course access is available for 6 months",
]

question = "What is the duration of course availability?"

document_vector = []

for document in documents:
    result = client.models.embed_content(model="gemini-embedding-2", contents=document)

    vector = result.embeddings[0].values
    document_vector.append(vector)

question_result = client.models.embed_content(
    model="gemini-embedding-2", contents=question
)

question_vector = question_result.embeddings[0].values


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


scores = []

for document, vector in zip(documents, document_vector):
    score = cosine_similarity(question_vector, vector)
    scores.append(score)

best_index = np.argmax(scores)
best_doc = documents[best_index]

print(best_doc)
