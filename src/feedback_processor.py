import sqlite3
from typing import List
import numpy as np
from src.embedding import get_sentence_embedding

DATABASE_NAME = "JarvisoDB.sqlite"


def generate_embeddings(sentences: List[str]) -> np.array:
    """
    Generate embeddings for a list of sentences using the defined embedding method.
    Args:
    - sentences: List of sentences for which embeddings are required.

    Returns:
    - embeddings: A numpy array containing the embeddings.
    """

    embeddings = [get_sentence_embedding(sentence) for sentence in sentences]
    return np.array(embeddings)


def save_feedback_data_to_db(feedback_data: List[tuple]):
    """
    Save feedback data to SQLite database.
    Args:
    - feedback_data: List of feedback data tuples.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    for data in feedback_data:
        cursor.execute('''
        INSERT INTO feedback_data (user_input, jarviso_response, feedback)
        VALUES (?, ?, ?)
        ''', (data[0], data[1], data[2]))

    conn.commit()
    conn.close()


def get_feedback_data_from_db() -> List[tuple]:
    """
    Retrieve feedback data from SQLite database.

    Returns:
    - feedback_data: List of feedback data tuples.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM feedback_data')
    feedback_data = cursor.fetchall()

    conn.close()
    return feedback_data

# ... Any other required functions ...
