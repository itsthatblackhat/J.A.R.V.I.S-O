from src.api_handlers.openai_api import call_openai_gpt_api
from src.api_handlers.search_api_handler import call_bing_search_api
from src.feedback_processor import generate_embeddings
from src.knowledge_processor import get_answer_from_knowledge_base
import json
import random

# Load API keys directly from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]


class DialogueManager:
    def __init__(self, bing_api_key, bing_endpoint, local_model):
        self.context = {"previous_questions": [], "preferences": {}}
        self.bing_api_key = bing_api_key
        self.bing_endpoint = bing_endpoint
        self.local_model = local_model
        self.recent_questions = []

    def respond(self, user_input):
        # Check if question is repeated
        if user_input in self.recent_questions:
            return "It seems you've asked this before. Can I assist you with another query?"

        # Update recent questions
        self.recent_questions.append(user_input)
        if len(self.recent_questions) > 5:  # Storing only last 5 questions for simplicity
            self.recent_questions.pop(0)

        # Commands recognition
        if user_input.lower() in ["exit", "end", "quit"]:
            return "Goodbye! Have a great day!"

        # Implementing curiosity feature with improved conditions
        if random.random() < 0.1 and "?" in user_input:  # 10% chance and if user input contains a '?'
            return "I'm curious! Can you tell me more about that?"

        # 1. Check Knowledge Base
        kb_response = get_answer_from_knowledge_base(user_input)
        if kb_response:
            return kb_response

        # 2. Local Neural Network
        local_nn_response = self.local_neural_network_predict(user_input)
        if local_nn_response:
            return local_nn_response

        # 3. GPT (OpenAI)
        gpt_response = call_openai_gpt_api(user_input, OPENAI_API_KEY)
        if gpt_response:
            return gpt_response

        # 4. Bing Search
        snippet = self.search_for_information(user_input)
        if snippet:
            return f"Here's what I found about '{user_input}': {snippet}. Would you like to explore more on this topic or provide information on it?"

        # 5. Default generic response
        return self.generic_response(user_input)

    def local_neural_network_predict(self, user_input):
        if not self.local_model:
            return None

        # Convert user input to embeddings
        input_embeddings = generate_embeddings([user_input])

        # Feed embeddings to the local model
        predicted_class = self.local_model.predict(input_embeddings)

        # Interpret the output
        if predicted_class == 1:
            return "Satisfactory response based on past interactions"  # Placeholder, adjust as needed
        else:
            return None

    def generic_response(self, user_input):
        return "I'm sorry, I don't know the answer to that."

    def search_for_information(self, user_input):
        # Fetch information from Bing Search API
        snippet = call_bing_search_api(user_input, self.bing_api_key, self.bing_endpoint)
        return snippet

    def update_context(self, key, value):
        self.context[key] = value
