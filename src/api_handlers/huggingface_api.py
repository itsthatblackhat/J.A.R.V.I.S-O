import requests
import json
from typing import Optional

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

HUGGINGFACE_API_KEY = API_KEYS["huggingface_api_key"]
HUGGINGFACE_ENDPOINT = "https://api-inference.huggingface.co/models/gpt-2.5-turbo"  # Modify this if you're using a different model



def call_huggingface_bert_api(query, api_key):
    """
    Call the HuggingFace BERT API with a given query.
    :param query: The text query for the API.
    :param api_key: The API key for HuggingFace.
    :return: The API's response.
    """
    # TODO: Implement the actual API call using the provided api_key and processing.
    return "Response from HuggingFace BERT API for query: " + query


# huggingface_api.py
def call_huggingface_api(query: str) -> Optional[str]:
    """
    Call the HuggingFace API with a specific query and return the result.
    """
    # Your API calling code here
    # For example:
    response = ...  # Call to HuggingFace API
    return response


def huggingface_response(prompt: str) -> Optional[str]:
    """Function to get a response from HuggingFace's model."""
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    data = {
        "inputs": prompt
    }
    try:
        response = requests.post(HUGGINGFACE_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        content = response.json()
        return content.get('generated_text', None)
    except Exception as e:
        print(f"Error in huggingface_response: {e}")
        return None
