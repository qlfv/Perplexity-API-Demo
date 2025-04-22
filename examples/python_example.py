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

# Exemple avec le modèle sonar-small
payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {"role": "system", "content": "Soyez précis et concis."},
        {"role": "user", "content": "Donne moi le prix actuel du bitcoin ?"}
    ],
    "max_tokens": 500,
    "temperature": 0.7,
    "stream": False,  # Option pour activer le streaming
    "top_p": 0.9,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Réponse de l'IA :", result["choices"][0]["message"]["content"])
    if "citations" in result:
        print("\nCitations utilisées :")
        for citation in result["citations"]:
            if isinstance(citation, str):
                print(f"- {citation}")
            else:
                print(f"- {citation.get('title', 'Sans titre')}: {citation.get('url', 'URL non disponible')}")
else:
    print("Erreur :", response.status_code, response.text)
