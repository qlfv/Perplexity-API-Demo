#!/bin/bash

export PERPLEXITY_API_KEY="VotreCléAPIIci"

curl -X POST \
--url https://api.perplexity.ai/chat/completions \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header "Authorization: Bearer ${PERPLEXITY_API_KEY}" \
--data '{
  "model": "mistral-7b-instruct",
  "messages": [
    {"role": "system", "content": "Soyez précis et concis."},
    {"role": "user", "content": "Quelle est la capitale de la France ?"}
  ],
  "max_tokens": 100,
  "temperature": 0.5
}'
