from typing import Optional
from .openai_api import call_openai_gpt_api
from .bing_search import bing_search
from .huggingface_api import call_huggingface_api

def search_query(query: str, api_type: str = "openai") -> Optional[str]:
    """
    Search for a query using a specific API type.
    Supported API types: "openai", "bing", "huggingface"
    """
    if api_type == "openai":
        return call_openai_gpt_api(query)
    elif api_type == "bing":
        return bing_search(query)
    elif api_type == "huggingface":
        return call_huggingface_api(query)
    else:
        print(f"Unsupported API type: {api_type}")
        return None
