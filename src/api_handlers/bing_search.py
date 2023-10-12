import requests
import json


def call_bing_search_api(query, api_key, endpoint):
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    params = {
        "q": query,
        "count": 10,
        "offset": 0,
        "mkt": "en-US",
        "safesearch": "Moderate"
    }

    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    search_results = response.json()
    return search_results

