# Perplexity API Demo 🚀

Ce dépôt présente comment utiliser l'API de Perplexity AI pour interagir avec des modèles de langage avancés.

## Fonctionnalités :
- 🌐 Envoi de requêtes REST à l'API Perplexity
- 🤖 Utilisation des derniers modèles :
  - `llama-3.1-sonar-small-128k-online`
  - `llama-3.1-sonar-huge-128k-online`
  - `llama-3.1-sonar-large-128k-online`
- 📄 Gestion des citations dans les réponses
- 🔄 Support du streaming pour les réponses en temps réel
- ⚙️ Paramètres avancés :
  - Temperature
  - Top-p sampling
  - Presence penalty
  - Frequency penalty

## Exemples :
- `python_example.py` : Exemple de base avec les derniers modèles
- `streaming_example.py` : Démonstration du streaming
- `curl_example.sh` : Exemple avec cURL

---

## Prérequis :
- Python 3.8 ou supérieur.
- Une clé API valide pour Perplexity AI.

---

## Installation :

1. Clonez ce dépôt :

```
git clone https://github.com/Wiminds/Perplexity-API-Demo.git cd Perplexity-API-Demo
```

2. Installez les dépendances Python :

```
pip install -r requirements.txt
```


3. Configurez vos variables d'environnement :
- Créez un fichier `.env` à partir du modèle `.env.example`.
- Ajoutez votre clé API :
  ```
  PERPLEXITY_API_KEY=VotreCléAPIIci
  ```

---

## Ressources supplémentaires :
- [Documentation officielle de l'API Perplexity](https://docs.perplexity.ai)
- [Liste des modèles supportés](https://docs.perplexity.ai/docs/model-cards)

---

## Contribution :
Les contributions sont les bienvenues ! Ouvrez une issue ou soumettez une pull request.

## Licence :
Ce projet est sous licence MIT.
