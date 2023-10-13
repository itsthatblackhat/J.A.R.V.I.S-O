import json
import tensorflow_hub as hub
from src.api_handlers.huggingface_api import call_huggingface_bert_api

# Load API keys from json once and cache it.
with open('config/api_keys.json', 'r') as f:
    keys = json.load(f)
    HUGGINGFACE_API_KEY = keys.get("huggingface_api_key")

# Load Universal Sentence Encoder
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")


def get_sentence_embedding(sentence: str) -> list:
    """
    Gets the embedding for a given sentence using the Universal Sentence Encoder.

    Args:
    - sentence: The sentence to be embedded.

    Returns:
    - list: The sentence embedding.
    """
    return embed([str(sentence)])[0].numpy()


def convert_text_to_embedding(text: str) -> list:
    """
    Convert the given text to embeddings using the BERT model from HuggingFace API.

    Args:
    - text: User input text.

    Returns:
    - list: Numeric embeddings of the text.
    """

    # Get BERT embeddings for the text
    embedding = call_huggingface_bert_api(text, HUGGINGFACE_API_KEY)

    if embedding is not None:
        return embedding
    else:
        # Handle cases where embedding fails; for now, we'll log the error and return an empty list.
        print(f"Failed to obtain embeddings for text: {text}")
        return []
