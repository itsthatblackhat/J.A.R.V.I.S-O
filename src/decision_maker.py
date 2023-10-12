import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def build_model(input_dim):
    """Build a basic neural network model."""
    model = Sequential()
    model.add(Dense(16, input_dim=input_dim, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def train_core_brain(embeddings, decisions):
    """Train the core decision-making brain of Jarviso."""
    # Assuming embeddings is a list of embeddings and decisions is a list of 0s and 1s (0 for bad, 1 for good)
    if not embeddings or not decisions:
        return None

    input_dim = len(embeddings[0])  # Get the size of an embedding
    model = build_model(input_dim)

    # Convert data to numpy arrays for training
    X = np.array(embeddings)
    y = np.array(decisions)

    model.fit(X, y, epochs=10, batch_size=1)

    return model

def predict_decision(model, embedded_input):
    """
    Predict the decision based on the embedded input.

    Args:
    - model: Trained TensorFlow/Keras model.
    - embedded_input: Numpy array of input embeddings.

    Returns:
    - predicted_class: Predicted class label.
    """
    embedded_input = np.array(embedded_input).reshape(1, -1)  # Reshaping to ensure it's 2D
    predicted_class = np.argmax(model.predict(embedded_input), axis=-1)
    return predicted_class[0]
