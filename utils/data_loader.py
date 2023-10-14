import sqlite3
import pandas as pd

DATABASE_PATH = "jarviso.db"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    except sqlite3.Error as e:
        print(e)
    return conn

def load_data(table_name: str) -> pd.DataFrame:
    """
    Load data from a specified SQLite table into a pandas DataFrame.
    """
    conn = create_connection()
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    conn.close()
    return df

def save_data(data: pd.DataFrame, table_name: str):
    """
    Save data from a pandas DataFrame to a specified SQLite table.
    """
    conn = create_connection()
    data.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def save_feedback_data(feedback_data: list, table_name: str,user_input, jarviso_response, feedback):
    """
    Save feedback data to a specified SQLite table.
    """
    conn = create_connection()
    feedback_df = pd.DataFrame(feedback_data, columns=["User Input", "Jarviso Response", "Feedback"])
    feedback_df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def save_feedback_log(feedback_log: list, table_name: str):
    """
    Save feedback logs to a specified SQLite table.
    """
    conn = create_connection()
    feedback_log_df = pd.DataFrame(feedback_log, columns=["User Input", "Jarviso Response", "Feedback"])
    feedback_log_df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def save_training_data(training_data: list, table_name: str):
    """
    Save training data to a specified SQLite table.
    """
    conn = create_connection()
    training_data_df = pd.DataFrame(training_data, columns=["Embeddings", "Decisions"])
    training_data_df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
