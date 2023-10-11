
from api_handlers.openai_api import call_openai_gpt_api
from decision_maker import train_core_brain, predict_decision
from utils.data_loader import load_data, save_data
from utils.model_loader import load_model, save_model
import numpy as np
import os

API_KEY = "YOUR_OPENAI_API_KEY"  # Placeholder, replace with your key

def interact_with_user():
    interactions = []
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
        if user_input.lower() == "exit":
            # Save interactions and model before exiting
            save_data(interactions, data_filepath)
            if model:
                save_model(model, model_filepath)
            break

        # Get response from GPT
        gpt_response = call_openai_gpt_api(user_input, API_KEY)
        
        # Log the interaction
        interactions.append((user_input, gpt_response))
        
        # Every 10 interactions, train the decision maker
        if len(interactions) % 10 == 0:
            # Placeholder: using random embeddings for now
            embeddings = np.random.rand(len(interactions), 768)
            decisions = [0] * len(interactions)  # Placeholder decisions
            model = train_core_brain(embeddings, decisions)
        
        print(f"Jarviso: {gpt_response}")
