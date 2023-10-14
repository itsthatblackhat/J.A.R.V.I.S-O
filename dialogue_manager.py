import numpy as np
import json
import random
from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.knowledge_helpers import get_answer_from_knowledge_base, google_search
from src.decision_maker import train_core_brain, load_model_parameters
from .context_manager import ContextManager
from src.logic_checker import LogicAndConsistencyChecker
from src.regularization import regularize_output
from src.post_processor import PostProcessor  # <-- Importing the new post-processor

class DialogueManager:
    def __init__(self, local_model, context_manager):
        self.context_manager = context_manager
        self.local_model = local_model
        self.recent_questions = []
        self.training_data = []
        self.logic_checker = LogicAndConsistencyChecker()
        self.post_processor = PostProcessor()  # <-- Instantiating the post-processor

    def store_training_data(self, user_input, gpt_response):
        self.training_data.append((user_input, gpt_response))

    def respond(self, user_input):
        # First, fetch a response from the knowledge base
        kb_response = get_answer_from_knowledge_base(user_input, self.context_manager.get_context())
        if kb_response:
            self.context_manager.update_context(user_input, kb_response)
            return kb_response, False, 0.0

        # If not found in the knowledge base, try the local neural network
        embedding = generate_embeddings([user_input])
        prediction = self.local_model.predict(embedding)
        if prediction[0] >= 0.8:
            local_nn_response = "Some response from local model."
            self.context_manager.update_context(user_input, local_nn_response)
            return local_nn_response, True, 1.0

        # If neither, fall back to GPT-3
        try:
            gpt_response = call_openai_gpt_api(user_input)

            # Logic and consistency check
            if not self.logic_checker.check(gpt_response):
                gpt_response = "I apologize, my response earlier wasn't appropriate. Let me try again."
                gpt_response = call_openai_gpt_api(user_input)

            # Regularize the response
            gpt_response = regularize_output(gpt_response)

            # Post-process the response
            gpt_response = self.post_processor.process(gpt_response)  # <-- Using the post-processor

            if gpt_response:
                self.context_manager.update_context(user_input, gpt_response)
                return gpt_response, False, 0.0
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            error_response = "Sorry, I couldn't process that request."
            return error_response, False, 0.0

    def local_neural_network_predict(self, user_input, context):
        if not user_input:
            return "I'm not sure how to respond to that.", 0
        input_embedding = generate_embeddings(user_input)
        input_embedding = np.reshape(input_embedding, (-1, 512))
        predicted_prob = self.local_model.predict(input_embedding)[0][0]
        predicted_class = 1 if predicted_prob > 0.5 else 0
        return predicted_class, predicted_prob

    def generic_response(self, user_input):
        return "I'm sorry, I don't know the answer to that."
