import requests
import json

def split_text_into_chunks(text, max_length=512):
    """
    Splits a long text into smaller chunks each of max_length. Assumes an average token length of 5 for simplicity.
    """
    avg_token_length = 5
    max_chars = max_length * avg_token_length
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

def call_huggingface_bert_api(text, api_key):
    API_ENDPOINT = "https://api-inference.huggingface.co/models/bert-base-uncased"
    HEADERS = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Split the text into chunks if it's too long
    chunks = split_text_into_chunks(text)
    embeddings = []

    response = None  # Initialize the response variable outside the loop

    for chunk in chunks:
        DATA = {
            "inputs": chunk
        }

        try:
            response = requests.post(API_ENDPOINT, headers=HEADERS, json=DATA)
            response.raise_for_status()

            # Extracting embeddings or processed output from the response.
            chunk_embedding = response.json()["embedding"]
            embeddings.append(chunk_embedding)

        except requests.RequestException as e:
            print(f"Error in API call for chunk '{chunk[:50]}...': {e}")
            if response:
                print(f"API Response: {response.content.decode('utf-8')}")
            return None

    # If multiple chunks, concatenate embeddings
    if len(embeddings) > 1:
        return [item for sublist in embeddings for item in sublist]
    else:
        return embeddings[0]
