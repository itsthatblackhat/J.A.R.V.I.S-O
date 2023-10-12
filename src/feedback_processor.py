from src.embedding import convert_text_to_embedding
import numpy as np


def generate_embeddings(interactions):
    """
    Given a list of interactions (questions and responses), generate embeddings for each interaction using BERT.
    Returns a numpy array of embeddings.
    """
    embeddings = []

    for interaction in interactions:
        # Ensure interaction is a valid tuple or list before processing
        if not isinstance(interaction, (tuple, list)):
            print(f"Invalid interaction format: {interaction}")
            continue

        # For the purpose of this example, we're just embedding the user input.
        # Depending on the use case, you might want to embed the response or both.
        text = interaction[0]

        # Get BERT embeddings for the text using the refactored function
        embedding = convert_text_to_embedding(text)

        if embedding is not None:
            embeddings.append(embedding)
        else:
            # Handle failed embeddings (e.g., by using a zero vector or skipping)
            embeddings.append(np.zeros((768,)))

    return np.array(embeddings)
