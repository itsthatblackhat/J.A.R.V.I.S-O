import sqlite3
import json
import os
import sys
from src.browser_app import BrowserApp
from src.api_handlers.openai_api import call_openai_gpt_api
from src.feedback_processor import generate_embeddings
from src.decision_maker import train_core_brain, periodically_train_model
from src.active_learner import ActiveLearner
from src.dialogue_manager import DialogueManager
from src.context_manager import ContextManager
from src.knowledge_processor import DATABASE_NAME
from utils.data_loader import load_data, save_data, save_feedback_data, save_feedback_log, save_training_data
from utils.model_loader import load_model, save_model
from src.training_manager import TrainingManager
from src.test_manager import TestManager
from utils.wordnet_utils import get_definitions, get_synonyms, get_hypernyms



# Load API keys from the config file
with open("config/api_keys.json", "r") as file:
    API_KEYS = json.load(file)

OPENAI_API_KEY = API_KEYS["openai_api_key"]
DB_PATH = os.path.join("data", "jarviso.db")


# Automated conversation to train Jarviso
def automated_training(jarviso_instance):
    training_phrases = [
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me grammar and how to speak and have conversation",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about math",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about science",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about programming",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about geography",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about advanced mathematics",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about politics",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about machine learning",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about humans",
        "Hello I'm Jarvis and I'm training my neural network .h5 file, have a conversation with me to assist me with building my knowledge, teach me to talk about anything"
    ]

    print("Initiating automated training conversation...")
    for phrase in training_phrases:
        response = call_openai_gpt_api(phrase)
        jarviso_instance.collect_feedback_and_train(phrase, response)
    print("Automated training completed!")


class Jarviso:
    def __init__(self):
        self.interaction_count = 0
        # Initialize the OpenAI API key
        with open("config/api_keys.json", "r") as file:
            self.OPENAI_API_KEY = json.load(file).get("openai_api_key", "")

        # Model Initialization
        self.model_filepath = os.path.join("models", "jarviso_core_brain.h5")
        if os.path.exists(self.model_filepath):
            self.local_model = load_model(self.model_filepath)
            print("Model loaded successfully!")
        else:
            self.local_model = None
            print(f"Model not found at {self.model_filepath}")
            # If model doesn't exist, initiate automated training
            print("Initiating automated training...")
            automated_training(self)
            # Reload the model after training
            if os.path.exists(self.model_filepath):
                self.local_model = load_model(self.model_filepath)
                print("Model loaded successfully after training!")

        # Initialize Context Manager and retrieve previous context from the database
        self.context_manager = ContextManager(max_length=5)
        self.context_manager.retrieve_context_from_db(session_id="default_session")

        # Initialize Active Learner
        self.active_learner = ActiveLearner()

        # Initialize Dialogue Manager
        self.dialogue_manager = DialogueManager(local_model=self.local_model, context_manager=self.context_manager)

    def train_with_new_data(self, existing_data_path, new_data_path, output_path):
        training_manager = TrainingManager(existing_data_path, new_data_path)
        training_manager.run(output_path)

    def test_performance(self, test_data_path):
        test_manager = TestManager(test_data_path, self.dialogue_manager)
        accuracy = test_manager.run_tests()
        print(f"Jarviso's performance accuracy: {accuracy*100:.2f}%")

    def open_browser(self):
        self.browser.show()

    def navigate_to(self, url):
        self.browser.url_input.setText(url)
        self.browser.navigate_to_url()

    def get_page_content(self):
        # Placeholder. Implementation using PyQt5 to extract content will be added later.
        pass

    def collect_feedback_and_train(self, user_input, gpt_response):
        # Ask for feedback
        feedback = input(f"Jarviso: {gpt_response}\nFeedback (good/bad): ").lower()

        # Construct the feedback data for saving
        feedback_list = [(user_input, gpt_response, feedback)]
        table_name = "feedback_data"
        save_feedback_data(feedback_list, table_name, user_input, gpt_response, feedback)

        embeddings = generate_embeddings([user_input])
        decisions = [1 if feedback == "good" else 0]
        self.local_model = train_core_brain(embeddings, decisions)
        save_model(self.local_model, self.model_filepath)

    def refine_response_with_wordnet(self, response):
        # Tokenize the response to get words/phrases
        words = response.split()
        for word in words:
            # Use WordNet to get synonyms
            synonyms = get_synonyms(word)
            if synonyms:
                # Replace word with a synonym (for demonstration, we'll just pick the first one)
                response = response.replace(word, synonyms[0])
        return response

    def respond(self, user_input):
        self.interaction_count += 1

        # If user input is empty
        if not user_input.strip():
            return "I didn't catch that. Please say something!"

        # Use Dialogue Manager to get response
        gpt_response, is_from_local_model, confidence = self.dialogue_manager.respond(user_input)

        # Refine the response using WordNet
        refined_response = self.refine_response_with_wordnet(gpt_response)

        # If the confidence is below a certain threshold, fall back to GPT's response
        if confidence < 0.5:
            try:
                gpt_response = call_openai_gpt_api(user_input)
                refined_response = self.refine_response_with_wordnet(gpt_response)
            except Exception as e:
                print(f"Error calling OpenAI API: {e}")
                refined_response = "Sorry, I couldn't process that request."
            finally:
                # Update the context even if there's an error
                self.context_manager.update_context(user_input, refined_response)

        # Periodically train the model
        if self.interaction_count % 10 == 0:
            periodically_train_model()

        return refined_response


def initialize_database():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS conversation_context 
                      (user_input TEXT, bot_response TEXT, session_id TEXT DEFAULT 'default_session')''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS interactions (user_input TEXT, jarviso_response TEXT)''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS feedback_data (user_input TEXT, jarviso_response TEXT, feedback TEXT)''')
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS feedback_log (user_input TEXT, jarviso_response TEXT, feedback TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS training_data (data BLOB)''')
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
    jarviso_instance = Jarviso()
    if not check_db_connection():
        print("Error: Cannot establish a connection to the database. Exiting.")
        return

    initialize_database()
    print("Starting interaction...")

    while True:
        user_input = input("User: ").strip()
        if not user_input:
            print("Jarviso: I didn't catch that. Please say something!")
            continue

        if user_input.lower() in ["exit", "end", "quit"]:
            print("Thank you for interacting with Jarviso. Have a great day!")
            break
        jarviso_response = jarviso_instance.respond(user_input)
        print(f"Jarviso: {jarviso_response}")
        feedback = input("Feedback (good/bad): ").lower()
        # You can store feedback and interactions here as needed
        # Rest of your interact_with_user logic can be added here...


if __name__ == "__main__":
    jarviso = Jarviso()

    action = input("Choose an action: [interact/test/train/exit]: ").lower()

    while action != "exit":
        if action == "interact":
            user_input = input("User: ")
            gpt_response = jarviso.respond(user_input)
            jarviso.collect_feedback_and_train(user_input, gpt_response)
        elif action == "test":
            test_data_path = "path_to_test_data.json"
            jarviso.test_performance(test_data_path)
        elif action == "train":
            existing_data_path = 'path_to_existing_data.json'
            new_data_path = 'path_to_new_data.json'
            output_path = 'path_to_save_combined_data.json'
            jarviso.train_with_new_data(existing_data_path, new_data_path, output_path)
        else:
            print("Invalid choice. Please choose from [interact/test/train/exit].")

        action = input("Choose an action: [interact/test/train/exit]: ").lower()

    print("Thank you for interacting with Jarviso. Have a great day!")