import pandas as pd
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    try:
        return pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        print(f"Data file {filepath} is empty.")
        return None
    except Exception as e:
        print(f"Error loading data from {filepath}: {e}")
        return None


def save_data(data, filepath):
    if not isinstance(data, list) or not all(isinstance(row, (list, tuple)) for row in data):
        print("Invalid data format. Expected a list of lists or tuples.")
        return

    df = pd.DataFrame(data, columns=['User Input', 'Jarviso Response', 'Feedback'])

    try:
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}.")
    except Exception as e:
        print(f"Error saving data to {filepath}: {e}")

