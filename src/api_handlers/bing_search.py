import json

import requests
from typing import Optional, List, Dict

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

BING_API_KEY = API_KEYS["bing_api_key"]
BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"


def bing_search(query: str) -> Optional[List[str]]:
    """Function to search Bing and retrieve search results."""
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {
        "q": query,
        "count": 5,  # Number of results to retrieve
        "offset": 0,
        "mkt": "en-US"
    }
    try:
        response = requests.get(BING_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        return [result['name'] for result in search_results['webPages']['value']]
    except Exception as e:
        print(f"Error in bing_search: {e}")
        return None
