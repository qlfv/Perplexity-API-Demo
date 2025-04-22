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

# Initialisation de l'historique de conversation
conversation_history = [
    {"role": "system", "content": "Tu es un assistant utile et amical. Réponds de manière concise."}
]

def send_message(message):
    # Ajout du message de l'utilisateur à l'historique
    conversation_history.append({"role": "user", "content": message})
    
    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": conversation_history,
        "max_tokens": 500,
        "temperature": 0.7,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        assistant_message = result["choices"][0]["message"]["content"]
        
        # Ajout de la réponse de l'assistant à l'historique
        conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

# Exemple de conversation
print("Début de la conversation (tapez 'quit' pour terminer)")
while True:
    user_input = input("\nVous: ")
    if user_input.lower() == 'quit':
        break
        
    response = send_message(user_input)
    if response:
        print(f"\nAssistant: {response}") 