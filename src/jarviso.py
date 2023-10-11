from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.decision_maker import train_core_brain
from utils.data_loader import load_data, save_data
from utils.model_loader import load_model, save_model
import os
import json

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]

def interact_with_user():
    interactions = []
    feedbacks = []
    previous_user_input = ""
    repeated_question_count = 0
    data_filepath = os.path.join("data", "interactions.csv")
    model_filepath = os.path.join("models", "jarviso_core_brain.h5")

    # Load existing data if available
    if os.path.exists(data_filepath):
        df = load_data(data_filepath)
        interactions = df.values.tolist()

    # Load existing model if available
    model = None
    if os.path.exists(model_filepath):
        model = load_model(model_filepath)

    while True:
        user_input = input("User: ")

        # Check for repeated questions
        if user_input == previous_user_input:
            repeated_question_count += 1
        else:
            repeated_question_count = 0
        previous_user_input = user_input

        # Handle repeated questions
        if repeated_question_count > 2:
            gpt_response = "It seems you're asking about the same topic. Unfortunately, my answer remains the same. Would you like to ask about something else?"
        else:
            # Get response from GPT
            gpt_response = call_openai_gpt_api(user_input, OPENAI_API_KEY)

        # Ask for feedback
        feedback = input(f"Jarviso: {gpt_response}\nFeedback (good/bad): ").lower()
        feedbacks.append(feedback)

        # Log the interaction
        interactions.append((user_input, gpt_response, feedback))

        # Every 10 interactions, train the decision maker
        if len(interactions) % 10 == 0:
            embeddings = generate_embeddings([i[0] for i in interactions[-10:]])  # Last 10 user inputs
            decisions = [1 if f == "good" else 0 for f in feedbacks[-10:]]  # Last 10 feedbacks
            model = train_core_brain(embeddings, decisions)
