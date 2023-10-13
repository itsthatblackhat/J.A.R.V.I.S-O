import sqlite3
import json
import os

from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.decision_maker import train_core_brain
from src.active_learner import ActiveLearner
from src.dialogue_manager import DialogueManager
from src.context_manager import ContextManager
from src.knowledge_processor import DATABASE_NAME
from utils.data_loader import load_data, save_data, save_feedback_data, save_feedback_log, save_training_data
from utils.model_loader import load_model, save_model

# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]

DB_PATH = os.path.join("data", "jarviso.db")


def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS interactions
                     (user_input TEXT, jarviso_response TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback_data
                     (user_input TEXT, jarviso_response TEXT, feedback TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback_log
                     (user_input TEXT, jarviso_response TEXT, feedback TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS training_data
                     (data BLOB)''')

    conn.commit()
    conn.close()


def check_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.close()
        return True
    except sqlite3.Error:
        return False


def save_to_db(table, data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if table == "interactions":
        cursor.executemany("INSERT INTO interactions (user_input, jarviso_response) VALUES (?,?)", data)
    elif table == "feedback_data":
        cursor.executemany("INSERT INTO feedback_data (user_input, jarviso_response, feedback) VALUES (?,?,?)", data)
    elif table == "feedback_log":
        cursor.executemany("INSERT INTO feedback_log (user_input, jarviso_response, feedback) VALUES (?,?,?)", data)
    elif table == "training_data":
        cursor.executemany("INSERT INTO training_data (data) VALUES (?)", data)

    conn.commit()
    conn.close()


def interact_with_user():
    if not check_db_connection():
        print("Error: Cannot establish a connection to the database. Exiting.")
        return

    initialize_database()

    print("Starting interaction...")

    interactions = []
    feedback_data = []
    feedback_log = []

    # Initialize Active Learner
    active_learner = ActiveLearner()

    # Load existing model if available
    local_model = None
    model_filepath = os.path.join("models", "jarviso_core_brain.h5")

    if os.path.exists(model_filepath):
        local_model = load_model(model_filepath)
    else:
        # If the model file does not exist but we have some initial data
        # Load the initial data
        user_inputs = [...]  # Load your list of user inputs
        bot_responses = [...]  # Load corresponding list of bot responses
        feedbacks = [...]  # Load corresponding list of feedbacks ("good" or "bad")

        if user_inputs and bot_responses and feedbacks:  # Check if data lists are populated
            # Generate embeddings
            embeddings = generate_embeddings(user_inputs)
            # Convert feedback to binary labels
            decisions = [1 if feedback == "good" else 0 for feedback in feedbacks]
            # Train and save the model
            local_model = train_core_brain(embeddings, decisions)

    # Check again if we have a model
    if not local_model:
        print("Error: No local model available for prediction!")
        return

    # Initialize Context Manager and load previous context from DB
    context_manager = ContextManager(max_length=5)
    context_manager.retrieve_context_from_db()

    # Initialize Dialogue Manager with the local model and context_manager
    dialogue_manager = DialogueManager(local_model=local_model, context_manager=context_manager)

    while True:
        user_input = input("User: ")

        # Get response from Dialogue Manager
        gpt_response, is_from_local_model = dialogue_manager.respond(user_input)

        # If response is not from local model and OpenAI API is accessible
        if not is_from_local_model and OPENAI_API_KEY:
            try:
                gpt_response = call_openai_gpt_api(user_input)
            except Exception as e:
                print(f"Error calling OpenAI API: {e}")

        # Update context
        context_manager.update_context(user_input=user_input, bot_response=gpt_response)

        # Ask for feedback
        feedback = input(f"Jarviso: {gpt_response}\nFeedback (good/bad): ").lower()
        feedback_data.append((user_input, gpt_response, feedback))

        # After receiving feedback
        embeddings = generate_embeddings([user_input])
        decisions = [1 if feedback == "good" else 0]
        local_model = train_core_brain(embeddings, decisions)
        dialogue_manager.local_model = local_model  # Update the model in dialogue manager

        # Save interactions for each loop
        interactions.append((user_input, gpt_response))
        save_to_db("interactions", interactions)

        # Exit conditions
        if user_input.lower() in ["exit", "end", "quit"]:
            print("Thank you for interacting with Jarviso. Have a great day!")
            break


if __name__ == "__main__":
    interact_with_user()