import sqlite3
from typing import List, Tuple
import numpy as np
from src.embedding import get_sentence_embedding

DATABASE_NAME = "data/jarviso.db"

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

def save_feedback_data_to_db(feedback_data: List[Tuple[str, str, str]]):
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

def get_feedback_data_from_db() -> List[Tuple[str, str, str]]:
    """
    Retrieve feedback data from SQLite database.

    Returns:
    - feedback_data: List of feedback data tuples.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT user_input, jarviso_response, feedback FROM feedback_data')
    feedback_data = cursor.fetchall()

    conn.close()
    return feedback_data

def save_training_data_to_db(training_data: List[Tuple[str, str]]):
    """
    Save training data (questions and GPT responses) to SQLite database.
    Args:
    - training_data: List of training data tuples.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    for data in training_data:
        cursor.execute('''
        INSERT INTO training_data (user_input, gpt_response)
        VALUES (?, ?)
        ''', (data[0], data[1]))

    conn.commit()
    conn.close()

def get_training_data_from_db() -> List[Tuple[str, str]]:
    """
    Retrieve training data (questions and GPT responses) from SQLite database.

    Returns:
    - training_data: List of training data tuples.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT user_input, gpt_response FROM training_data')
    training_data = cursor.fetchall()

    conn.close()
    return training_data
