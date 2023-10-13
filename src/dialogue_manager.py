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
        self.training_data = []  # To store data for training

    def store_training_data(self, user_input, gpt_response):
        self.training_data.append((user_input, gpt_response))

    def respond(self, user_input):
        """
        Generate a response using knowledge base, local neural network, or GPT-3.

        Args:
        - user_input: The user's input string.

        Returns:
        - response: The generated response.
        - is_from_local_model: Boolean indicating if the response is from the local model.
        - confidence: A confidence score associated with the response. (1.0 for local model, 0.0 for GPT-3 for now)
        """

        # First, try to fetch a response from the knowledge base
        kb_response = get_answer_from_knowledge_base(user_input, self.context_manager.get_context())

        if kb_response:
            self.context_manager.update_context(user_input, kb_response)
            return kb_response, False, 0.0  # Return response, is_from_local_model = False, confidence = 0.0

        # If not found in the knowledge base, try the local neural network
        embedding = generate_embeddings([user_input])
        prediction = self.local_model.predict(embedding)

        # For now, let's assume a prediction close to 1 means we trust the local model's response.
        # This threshold can be adjusted based on how you train your model and the feedback loop.
        if prediction[0] >= 0.8:
            local_nn_response = "Some response from local model."  # This should be replaced with your logic to get a response from the local model.
            self.context_manager.update_context(user_input, local_nn_response)
            return local_nn_response, True, 1.0  # Return response, is_from_local_model = True, confidence = 1.0

        # If neither the knowledge base nor the local model returns a satisfactory answer, fall back to GPT-3
        try:
            gpt_response = call_openai_gpt_api(user_input)
            if gpt_response:
                self.context_manager.update_context(user_input, gpt_response)
                return gpt_response, False, 0.0  # Return response, is_from_local_model = False, confidence = 0.0
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            error_response = "Sorry, I couldn't process that request."
            return error_response, False, 0.0  # Return error response, is_from_local_model = False, confidence = 0.0


    def local_neural_network_predict(self, user_input, context):
        if not user_input:  # Check for empty input
            return "I'm not sure how to respond to that.", 0

        # Generate embedding for the input
        input_embedding = generate_embeddings(user_input)  # assuming this function returns a numpy array

        # Since the input embedding might be a sequence, we should flatten it
        input_embedding = np.reshape(input_embedding, (-1, 512))

        # Predict
        predicted_prob = self.local_model.predict(input_embedding)[0][0]

        # Convert probability to class (0 or 1)
        predicted_class = 1 if predicted_prob > 0.5 else 0

        return predicted_class, predicted_prob  # Return the confidence as well

    def generic_response(self, user_input):
        return "I'm sorry, I don't know the answer to that."
