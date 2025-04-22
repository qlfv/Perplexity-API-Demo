import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("PERPLEXITY_API_KEY")

url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Exemple avec tous les paramètres avancés
payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {"role": "system", "content": "Tu es un expert en intelligence artificielle. Réponds de manière technique mais accessible."},
        {"role": "user", "content": "Explique-moi la différence entre l'apprentissage supervisé et non supervisé."}
    ],
    "max_tokens": 1000,
    "temperature": 0.8,  # Plus créatif
    "top_p": 0.95,      # Plus diversifié
    "presence_penalty": 0.5,  # Encourage la diversité des sujets
    "frequency_penalty": 0.5,  # Réduit la répétition
    "stream": False
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
    
    result = response.json()
    print("Réponse de l'IA :\n")
    print(result["choices"][0]["message"]["content"])
    
    if "citations" in result:
        print("\nCitations utilisées :")
        for citation in result["citations"]:
            if isinstance(citation, str):
                print(f"- {citation}")
            else:
                print(f"- {citation.get('title', 'Sans titre')}: {citation.get('url', 'URL non disponible')}")
                
except requests.exceptions.RequestException as e:
    print(f"Erreur de requête : {e}")
except json.JSONDecodeError as e:
    print(f"Erreur de décodage JSON : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}") 