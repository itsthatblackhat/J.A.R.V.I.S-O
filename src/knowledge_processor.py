import sqlite3
import numpy as np
from typing import List

DATABASE_NAME = 'data/jarviso.db'  # Updated SQLite database path

def initialize_database():
    """Initialize the SQLite database and create the embeddings table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Create the embeddings table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS embeddings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL UNIQUE,
        embedding TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

def check_db_connection():
    """
    Checks if a connection to the database can be established.

    Returns:
    - True if the connection is successful; False otherwise.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.close()
        return True
    except sqlite3.Error:
        return False

def generate_embeddings(text: str) -> List[float]:
    """Generate dummy embeddings for the provided text."""
    return [len(text) * 0.1] * 300

def store_embedding_in_db(text: str, embedding: List[float]):
    """Store embeddings in the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    embedding_str = ','.join(map(str, embedding))

    try:
        cursor.execute('INSERT OR REPLACE INTO embeddings (text, embedding) VALUES (?, ?)', (text, embedding_str))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def retrieve_embedding_from_db(text: str) -> List[float]:
    """Retrieve embeddings from the SQLite database based on text."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT embedding FROM embeddings WHERE text = ?', (text,))
    embedding_str = cursor.fetchone()

    conn.close()

    if embedding_str:
        return list(map(float, embedding_str[0].split(',')))
    else:
        return []

if __name__ == "__main__":
    initialize_database()  # Initialize the database and create tables

    text_sample = "Hello Jarviso"
    embedding_sample = generate_embeddings(text_sample)
    store_embedding_in_db(text_sample, embedding_sample)
    retrieved_embedding = retrieve_embedding_from_db(text_sample)
    print(retrieved_embedding)
