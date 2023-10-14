# Jarviso Development Notes - Ultra Comprehensive

## Introduction

Jarviso, an embodiment of the moniker "JARVISO" (Jarvis - Official), is our ambitious venture that amalgamates the intricacies of neural networks, the vast reservoir of WordNet, and the unmatched capabilities of OpenAI's GPT. Conceptualized as a personal AI assistant, it is in a perpetual state of evolution, striving for more context-aware and insightful interactions.

---

## Main Structure

### 1. **Main Modules**:

- **`main.py`**:
  - **Purpose**: The springboard into Jarviso's realm.
  - **Main Function**: 
    - `interact_with_user()`: Kindles the primary user interaction loop.
  
- **`jarviso.py`**:
  - **Purpose**: Serves as the main orchestrator of interactions and command definitions.
  - **Main Function**: 
    - `interact_with_user()`: Chooses between different response generation strategies.

- **`dialogue_manager.py`**:
  - **Attributes**: 
    - `recent_questions`: A cache of recent user queries.
    - `local_model`: Instance of the neural network.
    - `context_manager`: Stewards the conversation context.
  - **Key Methods**: 
    - `respond()`: Arbitrates the optimal response avenue.
    - `local_neural_network_predict()`: Leverages the neural network for predictions.
    - `generic_response()`: Provides fallback responses.
  
- **`context_manager.py`**:
  - **Attributes**: 
    - `context`: Safeguards the conversation lineage.
    - `max_context_length`: Defines the ceiling for stored interactions.
  - **Key Methods**: 
    - `update_context()`: Refreshes the conversation history.
    - `get_context()`: Fetches the existing context.

### 2. **Subdirectories**:

- **`api_handlers`**: Interfaces for external service communications.
  - **`openai_api.py`**:
    - **Function**: 
      - `call_openai_gpt_api()`: Brokers interactions with the OpenAI GPT API, crafting responses.

- **`knowledge_helpers`**: Curators of the internal knowledge sanctum and web search utilities.
  - **Functions**: 
    - `get_answer_from_knowledge_base()`: Matches queries against a repository of predefined answers.
    - `google_search()`: Deploys Selenium to glean answers from the web.

- **`model`**: Houses the neural network models and affiliated utilities.
  - **`core_brain.py`**:
    - **Class `CoreBrain`**:
      - **Attributes**: 
        - `model`: The TensorFlow model instance.
      - **Methods**: 
        - `train()`: Refines the neural architecture.
        - `predict()`: Forges predictions.
        - `save()`: Persists model parameters.
        - `load()`: Resurrects a saved model.
    
- **`src`**: The nucleus of source code and utilities.
  - **`feedback_processor.py`**: Manages user feedback.
    - **Function**: 
      - `generate_embeddings()`: Transforms textual input into numerical embeddings.
  
  - **`decision_maker.py`**: Oversees neural network training and model configurations.
    - **Functions**: 
      - `train_core_brain()`: Directs the training regime.
      - `load_model_parameters()`: Retrieves archived model parameters.

---

## Neural Network Paradigm

Jarviso's neural architecture, embodied in `CoreBrain`, is envisaged as a binary classifier. It discerns whether a query should be addressed using indigenous knowledge or if it demands a more intricate resolution pathway.

- **Architecture**: 
  - **Input Layer**: Accepts embeddings.
  - **Dense Layers**: Process the data.
  - **Output Layer**: Renders a binary output.

- **Training Ritual**: 
  - **Embeddings**: Textual user queries transformed into numerical vectors.
  - **Decisions**: The canonical answers.

---

## SQLite Database

- **Purpose**: Offers a nimble, localized storage solution.
- **Usage**: Archives user interactions, feedback, and mission-critical system data.
- **Interactions**: A plethora of modules/functions engage in reading/writing to this database.

---

## Interdependencies and Workflow

1. **`main.py`**:
  - Fires up `interact_with_user()` from `jarviso.py`.

2. **`jarviso.py`**:
  - Leans on `dialogue_manager.py` for crafting responses.
  - Employs `context_manager.py` to glean/update conversation history.

3. **`dialogue_manager.py`**:
  - Engages `model/core_brain.py` for localized neural predictions.
  - Taps into `api_handlers` to glean responses from the external cosmos.
  - Engages `knowledge_helpers` for indigenous knowledge checks and web-oriented inquisitions.

4. **`context_manager.py`**:
  - Serves context, ensuring relevance in interactions.
  - Influences various modules by dispensing historical data.

---

## Conclusion

This dossier offers a meticulous exploration into Jarviso, capturing the essence and weaving the narrative of each module, directory, and function. It is the touchstone for developers and contributors
