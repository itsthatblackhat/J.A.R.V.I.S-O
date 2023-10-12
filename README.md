# Jarviso

Jarviso is an intelligent assistant inspired by JARVIS from the Iron Man movies. It simulates human-like interactions, learns from them, and provides relevant responses.

## Features

- **Core Brain**:
  - Based on a neural network implemented using TensorFlow.
  - Makes decisions based on user input embeddings.
- **Active Learning**:
  - Uses an active learning approach.
  - Queries the user for feedback on uncertain interactions every 10 interactions to refine its responses.
- **Dynamic Curiosity**:
  - Proactively asks questions.
  - Leverages OpenAI's GPT-3 to generate curious questions based on topics frequently inquired about by the user.
- **User Feedback Loop**:
  - Collects feedback after each interaction.
  - Feedback is critical for continuous learning.
- **Bing Search Integration**:
  - Searches Bing for relevant information if Jarviso doesn't have an answer.
- **User Context**:
  - Maintains a context of user interactions, including user preferences and frequently asked questions.

## File Structure and Descriptions

- **config**: Contains configuration files.
- **data**: Stores data used by the project.
- **database**: Contains database-related files or scripts.
- **logs**: Used for logging information.
- **models**: Contains pre-trained models or model architectures.
- **src**: The heart of the project, containing:
  - `active_learner.py`: Handles the active learning approach.
  - `api_handlers`: Contains scripts for various API interactions.
  - `context_manager.py`: Manages the context of user interactions.
  - `decision_maker.py`: Contains logic for decision-making based on user input.
  - `dialogue_manager.py`: Manages the dialogue flow and interactions.
  - `embedding.py`: Responsible for generating embeddings from user input.
  - `feedback_processor.py`: Handles user feedback.
  - `knowledge_processor.py`: Handles knowledge retrieval and processing.
  - `jarviso.py`: The primary interface for interacting with Jarviso.
- **utils**: Contains utility scripts or helper functions.

## Usage

Interact with Jarviso using the provided Python code snippet:

```python
from src.jarviso import interact_with_user
interact_with_user()
```

## Future Enhancements

- Incorporate more data sources.
- Integrate advanced NLP techniques.
- Use reinforcement learning based on user feedback.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
"""
