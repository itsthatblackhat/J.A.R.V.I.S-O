from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.decision_maker import train_core_brain
from src.active_learner import ActiveLearner
from src.dialogue_manager import DialogueManager
from utils.data_loader import load_data, save_data
from utils.model_loader import load_model, save_model
import os
import json

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]
BING_API_KEY = API_KEYS["bing_api_key"]
BING_ENDPOINT = API_KEYS["bing_endpoint"]

def interact_with_user():
    interactions = []
    feedbacks = []
    previous_user_input = ""
    repeated_question_count = 0
    data_filepath = os.path.join("data", "interactions.csv")
    model_filepath = os.path.join("models", "jarviso_core_brain.h5")

    # Initialize Active Learner
    active_learner = ActiveLearner()

    # Load existing model if available
    local_model = None
    if os.path.exists(model_filepath):
        local_model = load_model(model_filepath)

    # Initialize Dialogue Manager with the local model
    dialogue_manager = DialogueManager(bing_api_key=BING_API_KEY, bing_endpoint=BING_ENDPOINT, local_model=local_model)

    # Load existing data if available
    if os.path.exists(data_filepath):
        df = load_data(data_filepath)
        interactions.extend(df.values.tolist())

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
            # Get response from Dialogue Manager
            gpt_response = dialogue_manager.respond(user_input)

        # Ask for feedback
        feedback = input(f"Jarviso: {gpt_response}\nFeedback (good/bad): ").lower()
        feedbacks.append(feedback)

        # Log the interaction
        interactions.append([user_input, gpt_response, feedback])

        # If the feedback indicates the response was unsatisfactory, add it to the active learner's unlabeled data
        if feedback == "bad":
            active_learner.add_unlabeled_data((user_input, gpt_response))

        # Every 10 interactions, query the user for feedback on a specific uncertain interaction
        if len(interactions) % 10 == 0:
            uncertain_interaction = active_learner.get_data_for_labeling()
            if uncertain_interaction:
                print(f"We're uncertain about this interaction: User: {uncertain_interaction[0]} Jarviso: {uncertain_interaction[1]}")
                feedback_for_uncertain = input("Feedback (good/bad): ").lower()
                active_learner.receive_label(uncertain_interaction, feedback_for_uncertain)

                # Update interactions and feedback lists
                interactions.append(list(uncertain_interaction))
                feedbacks.append(feedback_for_uncertain)

            # Training decision maker
            embeddings = generate_embeddings([i[0] for i in interactions[-10:]])  # Last 10 user inputs
            decisions = [1 if f == "good" else 0 for f in feedbacks[-10:]]  # Last 10 feedbacks
            local_model = train_core_brain(embeddings, decisions)
            dialogue_manager.local_model = local_model  # Update the model in dialogue manager

            # Save the updated model
            save_model(local_model, model_filepath)

        # Save interactions to file for future reference
        save_data(interactions, data_filepath)
