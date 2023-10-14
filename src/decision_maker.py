import os
import sqlite3
import tempfile

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed
import io

DATABASE_NAME = "jarviso.db"
INTERACTION_THRESHOLD = 100  # Number of interactions before retraining

interaction_counter = 0  # To keep track of the number of interactions

def initialize_tf():
    """
    Initialize TensorFlow threading settings before any other TensorFlow operations.
    """
    if not tf.config.experimental.list_physical_devices('GPU'):
        tf.config.threading.set_inter_op_parallelism_threads(2)
        tf.config.threading.set_intra_op_parallelism_threads(4)

#initialize_tf()  # Call this at the start, before any TensorFlow operations

def create_tables(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS training_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            embedding BLOB,
            decision INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS model_parameters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            parameters BLOB
        )
    ''')
    conn.commit()


def save_training_data(conn, embeddings, decisions):
    c = conn.cursor()
    for embedding, decision in zip(embeddings, decisions):
        c.execute('''
            INSERT INTO training_data (embedding, decision)
            VALUES (?, ?)
        ''', (embedding.tobytes(), decision))
    conn.commit()


def train_core_brain(embeddings, decisions):
    #initialize_tf()  # Initialize TensorFlow settings
    embeddings = np.array(embeddings)
    decisions = np.array(decisions)
    model = build_model(embeddings.shape[1])
    model.fit(embeddings, decisions, epochs=10)
    save_model_parameters(conn, model)
    return model

def load_training_data(conn):
    c = conn.cursor()
    c.execute('SELECT embedding, decision FROM training_data')
    rows = c.fetchall()
    embeddings = [np.frombuffer(row[0], dtype=np.float32) for row in rows]
    decisions = [row[1] for row in rows]
    return embeddings, decisions

def build_model(input_dim):
    #initialize_tf()  # Initialize TensorFlow settings
    model = keras.models.Sequential([
        keras.layers.Dense(128, activation='relu', input_dim=input_dim),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model


def save_model_parameters(conn, model):
    temp_filename = tempfile.mktemp(suffix=".h5")
    model.save(temp_filename)

    with open(temp_filename, "rb") as f:
        model_blob = f.read()

    os.remove(temp_filename)

    c = conn.cursor()
    c.execute('''
        INSERT INTO model_parameters (parameters)
        VALUES (?)
    ''', (model_blob,))
    conn.commit()


def load_model_parameters(conn):
    c = conn.cursor()
    c.execute('SELECT parameters FROM model_parameters ORDER BY id DESC LIMIT 1')
    model_blob = c.fetchone()[0]

    temp_filename = tempfile.mktemp(suffix=".h5")

    with open(temp_filename, "wb") as f:
        f.write(model_blob)

    model = keras.models.load_model(temp_filename)
    os.remove(temp_filename)

    return model


def periodically_train_model():
    global interaction_counter
    interaction_counter += 1
    if interaction_counter >= INTERACTION_THRESHOLD:
        embeddings, decisions = load_training_data(conn)
        if len(embeddings) > 0:  # Only train if there's new data
            train_core_brain(embeddings, decisions)
            interaction_counter = 0  # Reset counter


def build_seq2seq_model(input_dim):
    model = Sequential()
    model.add(LSTM(128, activation='relu', input_shape=(input_dim, 1)))
    model.add(RepeatVector(3))  # Assuming a fixed output sequence length of 3 for demonstration
    model.add(LSTM(128, activation='relu', return_sequences=True))
    model.add(TimeDistributed(Dense(1)))
    model.compile(optimizer='adam', loss='mse')  # Using Mean Squared Error for simplicity
    return model


def train_seq2seq_model():
    # Placeholder function. The training logic for the seq2seq model would go here.
    # You would need a suitable dataset, split into input sequences and target sequences.
    pass


def update_model():
    # Load the most recent training data
    embeddings, decisions = load_training_data(conn)

    # Train the core brain with the new data
    if len(embeddings) > 0:  # Only train if there's new data
        train_core_brain(embeddings, decisions)


# Establish SQLite connection and create tables
conn = sqlite3.connect(DATABASE_NAME)
create_tables(conn)
