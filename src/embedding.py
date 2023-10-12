from src.api_handlers.huggingface_api import call_huggingface_bert_api
import json


def convert_text_to_embedding(text):
    """
    Convert the given text to embeddings.

    Args:
    - text: User input text.

    Returns:
    - embeddings: Numeric embeddings of the text.
    """

    # Load API keys from json
    with open('config/api_keys.json', 'r') as f:
        keys = json.load(f)
        huggingface_api_key = keys.get("huggingface_api_key")

    # Get BERT embeddings for the text
    embedding = call_huggingface_bert_api(text, huggingface_api_key)

    if embedding is not None:
        return embedding
    else:
        # Handle cases where embedding fails, for now, let's return None
        return None
