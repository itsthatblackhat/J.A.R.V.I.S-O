import sqlite3
import numpy as np

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
    # Dummy training logic
    # Replace this with your training code
    model = "dummy_model"

    # Store the model parameters in the SQLite database
    save_model_parameters(conn, model)
    return model


def save_model_parameters(conn, model):
    # Convert your model into a storable format
    # Here, I'm assuming a dummy model which is a string
    model_blob = model.encode('utf-8')
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
    model = model_blob.decode('utf-8')
    return model


# Establish SQLite connection and create tables
conn = sqlite3.connect(DATABASE_NAME)
create_tables(conn)
