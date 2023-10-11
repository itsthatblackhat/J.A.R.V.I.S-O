import pandas as pd
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def save_data(data, filepath):
    df = pd.DataFrame(data, columns=['User Input', 'Jarviso Response', 'Feedback'])
    df.to_csv(filepath, index=False)
