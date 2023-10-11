from src.api_handlers.huggingface_api import call_huggingface_bert_api
import numpy as np
import json

def generate_embeddings(interactions, fallback_embedding=None):
    """
    Given a list of interactions (questions and responses), generate embeddings for each interaction using BERT.
    Returns a numpy array of embeddings.
    """
    embeddings = []

    # Load API keys from json
    with open('config/api_keys.json', 'r') as f:
        keys = json.load(f)
        huggingface_api_key = keys.get("huggingface_api_key")

    for interaction in interactions:
        # For the purpose of this example, we're just embedding the user input.
        # Depending on the use case, you might want to embed the response or both.
        text = interaction[0]

        # Get BERT embeddings for the text
        embedding = call_huggingface_bert_api(text, huggingface_api_key)

        if embedding is not None:
            embeddings.append(embedding)
        elif fallback_embedding is not None:
            embeddings.append(fallback_embedding)
        else:
            # Handle failed embeddings (e.g., by using a zero vector or skipping)
            embeddings.append(np.zeros((768,)))

    return np.array(embeddings)
