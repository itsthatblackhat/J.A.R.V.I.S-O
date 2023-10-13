# Jarviso Development Notes - In-Depth

## Introduction
Jarviso is designed to serve as a sophisticated dialogue system, integrating several techniques and services.

---

## Structure Overview

1. **Main Files**:
    - `main.py`: The entry point of the application.
    - `jarviso.py`: Houses the primary logic for interacting with the user.
    - `dialogue_manager.py`: Decides the best approach for generating a response.
  
2. **Helper Directories**:
    - `api_handlers`: Contains utilities for external APIs.
    - `knowledge_helpers`: Manages the internal knowledge base and web searching.
    - `model`: Contains the neural network model for decision making.
    - `src`: The primary source directory.

---

## Detailed Breakdown

### `main.py`

- **Functions**:
    - `interact_with_user()`: Main loop for user interaction. Handles errors and gracefully terminates the program.

### `jarviso.py`

- **Functions**:
    - `interact_with_user()`: Orchestrates the interaction process, deciding between various response mechanisms.

### `dialogue_manager.py`

- **Attributes**:
    - `recent_questions`: Keeps track of the recent questions asked to avoid redundancy.
    - `local_model`: The neural network model instance.
    - `context_manager`: Instance of `ContextManager` to manage the conversation context.

- **Methods**:
    - `respond()`: Determines how to respond based on user input.
    - `local_neural_network_predict()`: Uses the local neural network to generate a prediction.
    - `generic_response()`: Provides a default response when no other methods succeed.

### `context_manager.py`

- **Attributes**:
    - `context`: A deque that stores the conversation history.
    - `max_context_length`: Maximum number of interactions to remember.

- **Methods**:
    - `update_context()`: Adds a new user-system interaction to the context.
    - `get_context()`: Retrieves the current context.

### `decision_maker.py`

- **Functions**:
    - `train_core_brain()`: Trains the neural network with new feedback.
    - `load_model_parameters()`: Loads an existing neural network model.

### `api_handlers/openai_api.py`

- **Functions**:
    - `call_openai_gpt_api()`: Sends a request to the OpenAI GPT API.

### `knowledge_helpers`

- **Functions**:
    - `get_answer_from_knowledge_base()`: Checks if the user's query matches any predefined responses.
    - `google_search()`: Searches the web for answers using Selenium.

### `model/core_brain.py`

- **Classes**:
    - `CoreBrain`: Represents the neural network model.
        - **Attributes**: 
            - `model`: TensorFlow neural network model.
        - **Methods**: 
            - `train()`: Trains the model using embeddings and decisions.
            - `predict()`: Makes a prediction based on input embeddings.
            - `save()`: Saves the model parameters.
            - `load()`: Loads saved model parameters.

---

## Neural Network Overview

- **Model Architecture**: 
    - Input Layer: Accepts embeddings.
    - Dense Layers: Process the embeddings.
    - Output Layer: Binary classification.

- **Training Process**: Embeddings and decisions are used to fine-tune the model. 

---

## Database

- We are utilizing SQLite for local storage.
- The database is designed to store user interactions, feedback, and other important data.
- Various components of the system will query or update the database as necessary.

---

## Interdependencies

- `jarviso.py` relies heavily on `dialogue_manager.py` to generate responses.
- `dialogue_manager.py` accesses:
    - Local neural network (`model/core_brain.py`)
    - External APIs (`api_handlers`)
    - Knowledge base (`knowledge_helpers`)
- `context_manager.py` is used across the system to maintain context.

---

This note aims to provide an exhaustive breakdown of Jarviso's project structure, detailing its functionalities, methodologies, and interdependencies. The project integrates local knowledge, neural networks, external APIs, and user feedback to offer an advanced dialogue system.
