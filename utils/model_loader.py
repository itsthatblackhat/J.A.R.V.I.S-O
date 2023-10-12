import tensorflow as tf
import os


def load_model(filepath):
    if not os.path.exists(filepath):
        print(f"Model file not found: {filepath}")
        return None

    try:
        return tf.keras.models.load_model(filepath)
    except Exception as e:
        print(f"Error loading model from {filepath}: {e}")
        return None


def save_model(model, filepath):
    if not isinstance(model, tf.keras.Model):
        print("Invalid model object.")
        return

    try:
        model.save(filepath)
        print(f"Model saved to {filepath}.")
    except Exception as e:
        print(f"Error saving model to {filepath}: {e}")

