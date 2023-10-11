import requests
import json

def call_huggingface_bert_api(text, api_key):
    API_ENDPOINT = "https://api-inference.huggingface.co/models/bert-base-uncased"
    HEADERS = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    DATA = {
        "inputs": text
    }

    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, json=DATA)
        response.raise_for_status()

        # Extracting embeddings or processed output from the response.
        # This step might vary based on the model's output structure.
        # For this example, I'm assuming the embedding is returned in a key called "embedding".
        # You might need to adjust this based on the actual API response.
        return response.json()["embedding"]

    except requests.RequestException as e:
        print(f"Error in API call: {e}")
        return None
