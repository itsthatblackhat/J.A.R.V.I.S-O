import requests
import json

def call_openai_gpt_api(user_input, api_key):
    API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"
    HEADERS = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Jarviso"
    }
    DATA = {
        "prompt": f"User: {user_input}\nJarviso:",
        "max_tokens": 150,
        "temperature": 0.6
    }

    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(DATA))
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()["choices"][0]["text"].strip()
    except requests.RequestException as e:
        print(f"Error in API call: {e}")
        return "Sorry, I couldn't process that request."
