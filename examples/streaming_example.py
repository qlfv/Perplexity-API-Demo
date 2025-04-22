import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PERPLEXITY_API_KEY")

url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Accept": "text/event-stream"  # Important pour le streaming
}

payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [
        {"role": "system", "content": "Soyez précis et concis."},
        {"role": "user", "content": "Explique-moi le concept de l'apprentissage automatique en 3 points."}
    ],
    "max_tokens": 500,
    "temperature": 0.7,
    "stream": True,
    "top_p": 0.9
}

try:
    # Envoi de la requête avec streaming
    with requests.post(url, json=payload, headers=headers, stream=True) as response:
        if response.status_code == 200:
            print("Réponse en streaming :\n")
            for line in response.iter_lines():
                if line:
                    try:
                        # Suppression du préfixe 'data: ' si présent
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            line = line[6:]
                        
                        # Ignorer les lignes vides ou [DONE]
                        if line.strip() == '' or line.strip() == '[DONE]':
                            continue
                            
                        data = json.loads(line)
                        if "choices" in data and len(data["choices"]) > 0:
                            content = data["choices"][0].get("delta", {}).get("content", "")
                            if content:
                                print(content, end="", flush=True)
                    except json.JSONDecodeError as e:
                        print(f"\nErreur de décodage JSON: {e}")
                        continue
                    except Exception as e:
                        print(f"\nErreur inattendue: {e}")
                        continue
            print("\n\nFin du streaming")
        else:
            print(f"Erreur HTTP: {response.status_code}")
            print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Erreur de requête: {e}") 