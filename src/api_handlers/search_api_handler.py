import requests
import json

def call_bing_search_api(query, api_key, endpoint):

    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    params = {
        "q": query,
        "count": 1,  # We want only the most relevant result
        "offset": 0,
        "mkt": "en-US",
        "safesearch": "Strict"
    }

    full_url = f"{endpoint}?q={query}&count=1&offset=0&mkt=en-US&safesearch=Strict"
    print(f"Constructed URL: {full_url}")

    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    search_results = response.json()
    snippet = search_results["webPages"]["value"][0]["snippet"]  # Extracting the snippet from the most relevant result

    return snippet
