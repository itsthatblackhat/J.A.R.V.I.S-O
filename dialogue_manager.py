import numpy as np
import json
import random

from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.knowledge_helpers import get_answer_from_knowledge_base, google_search
from src.decision_maker import train_core_brain, load_model_parameters

# Load API keys directly from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]

class DialogueManager:
    def __init__(self, local_model, context_manager):
        self.context_manager = context_manager
        self.local_model = local_model
        self.recent_questions = []

    def respond(self, user_input):
        # Handle empty user input
        if not user_input.strip():
            return "I'm not sure how to respond to that.", False

        # Check if question is repeated
        if user_input in self.recent_questions:
            return "It seems you've asked this before. Can I assist you with another query?", False

        # Update recent questions
        self.recent_questions.append(user_input)
        if len(self.recent_questions) > 5:  # Storing only last 5 questions for simplicity
            self.recent_questions.pop(0)

        # Commands recognition
        if user_input.lower() in ["exit", "end", "quit"]:
            return "Goodbye! Have a great day!", False

        # Implementing curiosity feature with improved conditions
        if random.random() < 0.1 and "?" in user_input:  # 10% chance and if user input contains a '?'
            return "I'm curious! Can you tell me more about that?", False

        # 1. Check Knowledge Base
        kb_response = get_answer_from_knowledge_base(user_input, self.context_manager.get_context())
        if kb_response:
            self.context_manager.update_context(user_input, kb_response)
            return kb_response, False

        # 2. Local Neural Network
        context = ' '.join([str(item[1]) for item in self.context_manager.get_context()])
        local_nn_response = self.local_neural_network_predict(user_input, context)
        if local_nn_response:
            self.context_manager.update_context(user_input, local_nn_response)
            return local_nn_response, True

        # 3. GPT (OpenAI)
        try:
            gpt_response = call_openai_gpt_api(user_input)
            if gpt_response:
                self.context_manager.update_context(user_input, gpt_response)
                return gpt_response, False
        except Exception as e:
            print(f"OpenAI API Error: {e}")

        # 4. Browser Search using Selenium
        snippet = google_search(user_input)
        if snippet:
            response = f"Here's what I found about '{user_input}': {snippet}. Would you like to explore more on this topic or provide information on it?"
            self.context_manager.update_context(user_input, response)
            return response, False

        # 5. Default generic response
        generic_resp = self.generic_response(user_input)
        self.context_manager.update_context(user_input, generic_resp)
        return generic_resp, False

    def local_neural_network_predict(self, user_input, context):
        if not user_input:  # Check for empty input
            return "I'm not sure how to respond to that."

        # Generate embedding for the input
        input_embedding = generate_embeddings(user_input)  # assuming this function returns a numpy array

        # Since the input embedding might be a sequence, we should flatten it
        input_embedding = np.reshape(input_embedding, (-1, 512))

        # Predict
        predicted_prob = self.local_model.predict(input_embedding)[0][0]

        # Convert probability to class (0 or 1)
        predicted_class = 1 if predicted_prob > 0.5 else 0

        return predicted_class

    def generic_response(self, user_input):
        return "I'm sorry, I don't know the answer to that."
