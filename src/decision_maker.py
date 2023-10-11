import tensorflow as tf
import numpy as np


def build_model(input_dim=768, num_classes=3):
    """
    Build and return a neural network model.

    Args:
    - input_dim: Dimension of the input embeddings.
    - num_classes: Number of output classes.

    Returns:
    - model: Compiled TensorFlow/Keras model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(512, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def train_core_brain(data, labels, epochs=10, validation_data=None):
    """
    Train the core brain neural network.

    Args:
    - data: Numpy array of input embeddings.
    - labels: Numpy array of labels.
    - epochs: Number of training epochs.
    - validation_data: Tuple of (val_data, val_labels) for evaluation.

    Returns:
    - model: Trained TensorFlow/Keras model.
    """
    data = np.array(data)
    labels = np.array(labels)

    model = build_model(input_dim=data.shape[1], num_classes=len(set(labels)))

    if validation_data:
        val_data, val_labels = validation_data
        val_data = np.array(val_data)
        val_labels = np.array(val_labels)
        validation_data = (val_data, val_labels)

    model.fit(data, labels, epochs=epochs, validation_data=validation_data)
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
