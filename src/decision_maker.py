import os
import sqlite3
import tempfile

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
import io

DATABASE_NAME = "jarviso.db"


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


def load_training_data(conn):
    c = conn.cursor()
    c.execute('SELECT embedding, decision FROM training_data')
    rows = c.fetchall()
    embeddings = [np.frombuffer(row[0], dtype=np.float32) for row in rows]
    decisions = [row[1] for row in rows]
    return embeddings, decisions


def train_core_brain(embeddings, decisions):
    embeddings = np.array(embeddings)
    decisions = np.array(decisions)

    print(f"Embeddings shape: {embeddings.shape}")
    print(f"Decisions shape: {decisions.shape}")
    print(f"Sample embeddings: {embeddings[:5]}")  # print first 5 embeddings
    print(f"Sample decisions: {decisions[:5]}")  # print first 5 decisions

    model = build_model(embeddings.shape[1])

    # Train the model without validation_split
    model.fit(embeddings, decisions, epochs=10)

    # Save the model parameters to the SQLite database
    save_model_parameters(conn, model)

    return model


def build_model(input_dim):
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


# Establish SQLite connection and create tables
conn = sqlite3.connect(DATABASE_NAME)
create_tables(conn)
