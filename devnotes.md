# Jarviso Development Notes - Ultra Comprehensive

## Introduction

Jarviso is a project that emulates capabilities similar to JARVIS, branded as "JARVISO" (Jarvis - Official). It integrates a neural network, multiple API services, and an SQLite database to construct a dialogue system.

---

## Main Structure

### 1. **Main Modules**:

   - **`main.py`**:
     - **Purpose**: The entry point of Jarviso.
     - **Main Function**: `interact_with_user()`: Engages the primary user interaction loop.
   
   - **`jarviso.py`**:
     - **Purpose**: Handles interactions and defines user commands.
     - **Main Function**: `interact_with_user()`: Orchestrates interaction deciding between different response sources.

   - **`dialogue_manager.py`**:
     - **Attributes**:
       - `recent_questions`: Retains recent user queries.
       - `local_model`: Instance of the neural network.
       - `context_manager`: Manages conversation context.
     - **Key Methods**:
       - `respond()`: Determines best response source.
       - `local_neural_network_predict()`: Uses the neural network for predictions.
       - `generic_response()`: Generic answers for failed methods.
   
   - **`context_manager.py`**:
     - **Attributes**:
       - `context`: Retains conversation history.
       - `max_context_length`: Maximum stored interactions.
     - **Key Methods**:
       - `update_context()`: Updates conversation history.
       - `get_context()`: Retrieves current context.

### 2. **Subdirectories**:

   - **`api_handlers`**: Interfaces with external services.
     - **`openai_api.py`**:
       - **Function**: `call_openai_gpt_api()`: Interfaces with the OpenAI GPT API for generating responses.

   - **`knowledge_helpers`**: Houses internal knowledge base and web search utilities.
     - **Functions**:
       - `get_answer_from_knowledge_base()`: Matches queries with predefined answers.
       - `google_search()`: Utilizes Selenium to search the web for answers.

   - **`model`**: Contains neural network models and related utilities.
     - **`core_brain.py`**:
       - **Class `CoreBrain`**:
         - **Attributes**:
           - `model`: The TensorFlow model instance.
         - **Methods**:
           - `train()`: Refines the model.
           - `predict()`: Generates a prediction.
           - `save()`: Saves model's parameters.
           - `load()`: Loads a saved model.
   
   - **`src`**: Core source code and utilities.
     - **`feedback_processor.py`**: Manages user feedback.
       - **Function**: `generate_embeddings()`: Converts text input into numerical embeddings.

     - **`decision_maker.py`**: Manages neural network training and model parameters.
       - **Functions**:
         - `train_core_brain()`: Orchestrates the training process.
         - `load_model_parameters()`: Retrieves saved model parameters.

---

## Neural Network Overview

Jarviso's neural network (`CoreBrain`) is a binary classifier that predicts if a query should be answered using local knowledge or escalated to a more complex mechanism.

- **Architecture**:
  - **Input Layer**: Accepts embeddings.
  - **Dense Layers**: Process data.
  - **Output Layer**: Returns 0 or 1.

- **Training**:
  - **Embeddings**: Represent user queries.
  - **Decisions**: Represent correct answers.

---

## SQLite Database

- **Purpose**: Offers lightweight, local storage.
- **Usage**: Retains user interactions, feedback, and critical system data.
- **Interactions**: Many modules/functions read/write to this database.

---

## Interdependencies and Flow

1. **`main.py`**:
   - Engages `interact_with_user()` from `jarviso.py`.

2. **`jarviso.py`**:
   - Relies on `dialogue_manager.py` for generating responses.
   - Uses `context_manager.py` to fetch/update conversation history.

3. **`dialogue_manager.py`**:
   - Utilizes `model/core_brain.py` for local neural network predictions.
   - Engages `api_handlers` to get responses from external sources.
   - Leverages `knowledge_helpers` for internal knowledge checks and web searches.

4. **`context_manager.py`**:
   - Provides context for relevant responses.
   - Influences other modules by offering historical data.

---

## Conclusion

This document offers an in-depth architectural overview of Jarviso, capturing the essence and intricacies of every module, directory, and function. It should serve as a crucial reference for all developers and contributors.
