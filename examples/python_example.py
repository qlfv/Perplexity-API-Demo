import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PERPLEXITY_API_KEY")

url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mistral-7b-instruct",
    "messages": [
        {"role": "system", "content": "Soyez précis et concis."},
        {"role": "user", "content": "Donne moi le prix actuel du bitcoin ?"}
    ],
    "max_tokens": 500,
    "temperature": 0.5,
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Réponse de l'IA :", response.json())
else:
    print("Erreur :", response.status_code, response.text)
