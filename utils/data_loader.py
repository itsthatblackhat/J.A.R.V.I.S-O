
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def save_data(data, filepath):
    data.to_csv(filepath, index=False)
