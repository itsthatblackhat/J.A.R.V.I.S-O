# Jarviso Project Detailed Analysis

## Directory Structure

```
Jarviso
│
├── config
│   ├── api_keys.json
│   ├── curious_questions.json
│   ├── knowledge_base.json
│   └── __init__.py
│
├── data
│   ├── english-wordnet.xml
│   └── jarviso.db
│
├── logs
│   └── interaction_logs.txt
│
├── models
│   └── jarviso_core_brain.h5
│
├── src
│   ├── active_learner.py
│   ├── browser_app.py
│   ├── context_manager.py
│   ├── data_collector.py
│   ├── decision_maker.py
│   ├── dialogue_manager.py
│   ├── embedding.py
│   ├── feedback_processor.py
│   ├── file_parser.py
│   ├── jarviso.py
│   ├── knowledge_helpers.py
│   ├── knowledge_processor.py
│   ├── logic_checker.py
│   ├── post_processor.py
│   ├── regularization.py
│   ├── test_manager.py
│   ├── tf_init.py
│   ├── training_manager.py
│   └── __init__.py
│
└── utils
    ├── data_loader.py
    ├── model_loader.py
    └── wordnet_utils.py
```

## File Details:

### Config:

#### api_keys.json:

- Contains API keys for various services.
  - Key: OPENAI_API_KEY - Used for OpenAI's GPT API.
  - Key: HUGGINGFACE_API_KEY - Used for HuggingFace's API.

#### curious_questions.json:
- Stores a list of questions that might be used for training or interaction purposes.

#### knowledge_base.json:
- Contains a structured representation of knowledge, likely used for answering user queries.

### Data:

#### english-wordnet.xml:
- XML-based representation of the English WordNet.
  - Used for fetching:
    - Definitions
    - Synonyms
    - Hypernyms

#### jarviso.db:
- SQLite database storing:
  - Conversation contexts
  - Feedback data
  - Interactions

### Logs:

#### interaction_logs.txt:
- Logs each interaction:
  - User input
  - Jarviso's response

### Models:

#### jarviso_core_brain.h5:
- TensorFlow/Keras model.
  - Handles natural language processing tasks.
  - Decision-making processes for Jarviso.

### Src:

#### active_learner.py:
- Contains the ActiveLearner class.
  - Uses a strategy where the model determines the data it learns from.

#### browser_app.py:
- Handles web browsing functionalities.
  - Contains BrowserApp class which likely interfaces with a web browser.

#### context_manager.py:
- Contains the ContextManager class.
  - Manages conversation context for continuity.
  - Methods:
    - retrieve_context_from_db
    - update_context

#### data_collector.py:
- Handles data collection.
  - Likely for training or logging purposes.

#### decision_maker.py:
- Contains functions/methods for making decisions.
  - train_core_brain: Trains the core brain of Jarviso.
  - periodically_train_model: Trains the model periodically.

#### dialogue_manager.py:
- Contains the DialogueManager class.
  - Manages dialogues between the user and Jarviso.
  - Determines which source to use for generating a response.

#### embedding.py:
- Contains functions related to word embeddings.
  - Converts words to vectors.

#### feedback_processor.py:
- Contains functions related to processing user feedback.
  - generate_embeddings: Generates embeddings for user input.

#### file_parser.py:
- Contains utility functions for parsing different file types.

#### jarviso.py:

- Primary script for Jarviso.
  - Initializes the assistant: Initializes models, API keys, and other essential components.
  - Handles interactions: Manages user interactions and provides responses.
  - Contains main loop: Takes user input and generates responses.
  - Contains methods and functionalities:
    - `train_with_new_data`: Trains the model with a combination of existing and new data.
    - `test_performance`: Evaluates the performance of Jarviso using a set test data.
    - `respond`: Generates a response based on user input.
    - `collect_feedback_and_train`: Collects user feedback on responses and trains the model accordingly.
    - `refine_response_with_wordnet`: Refines the generated response using WordNet to enhance the vocabulary.
    - Automated training: Uses predefined training phrases to train Jarviso.

#### knowledge_helpers.py:

- Contains utility functions related to managing and processing knowledge.
  - Functions to search, retrieve, and manipulate knowledge from various sources.

#### knowledge_processor.py:

- Manages the knowledge base.
  - Contains functionalities related to storing, retrieving, and querying the knowledge base.
  - Interacts with the `DATABASE_NAME` to perform operations.

#### logic_checker.py:

- Contains functionalities to validate certain operations or inputs.
  - Might be used to ensure the accuracy or relevance of certain responses or operations.

#### post_processor.py:

- Processes the output after an initial response.
  - Refines or modifies the generated response as needed.
  - Can be used to improve the fluency, grammar, or relevance of a response.

#### regularization.py:

- Contains functions or classes related to regularization.
  - Regularization prevents overfitting in machine learning models.
  - Ensures the model generalizes well to new, unseen data.

#### test_manager.py:

- Manages testing operations.
  - Evaluates the performance of Jarviso.
  - Contains methods such as:
    - `run_tests`: Runs tests and returns performance metrics.

#### tf_init.py:

- Initializes TensorFlow configurations.
  - Sets up any necessary parameters or configurations for TensorFlow to run optimally.

#### training_manager.py:

- Manages training operations for Jarviso.
  - Contains methods and functionalities for training the core model of Jarviso with new data.

### Utils:

#### data_loader.py:

- Contains utility functions related to data operations.
  - Methods include:
    - `load_data`: Loads data from a specified source.
    - `save_data`: Saves data to a specified destination.
    - `save_feedback_data`: Saves feedback data to enhance training.
    - `save_feedback_log`: Logs feedback for auditing or review purposes.
    - `save_training_data`: Saves data specifically used for training.

#### model_loader.py:

- Contains functions for model operations.
  - Methods include:
    - `load_model`: Loads a TensorFlow/Keras model from a specified path.
    - `save_model`: Saves a TensorFlow/Keras model to a specified path.

#### wordnet_utils.py:

- Contains utility functions for WordNet operations.
  - Interacts with the WordNet lexical database to fetch:
    - Definitions: Provides definitions of words.
    - Synonyms: Provides synonyms for words.
    - Hypernyms: Provides hypernyms (broader terms) for words.

