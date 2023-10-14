import requests
import json
from typing import Optional

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]
OPENAI_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"  # Modify this if you're using a different model or endpoint

def call_openai_gpt_api(prompt: str) -> Optional[str]:
    """Function to get a response from OpenAI's GPT-3 model."""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150  # Limiting response length for demo purposes; you can adjust this
    }
    try:
        response = requests.post(OPENAI_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()
        return content.get('choices', [{}])[0].get('text', '').strip()
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None
