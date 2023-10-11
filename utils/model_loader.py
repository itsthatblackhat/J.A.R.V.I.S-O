
import tensorflow as tf

def load_model(filepath):
    return tf.keras.models.load_model(filepath)

def save_model(model, filepath):
    model.save(filepath)
