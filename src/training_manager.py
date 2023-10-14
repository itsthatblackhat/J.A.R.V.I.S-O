import os
import json
import sqlite3

DATABASE_NAME = "data/jarviso.db"

class TrainingManager:
    def __init__(self, existing_data_path, new_data_path):
        self.existing_data_path = existing_data_path
        self.new_data_path = new_data_path
        self.combined_data = []

    def load_existing_data(self):
        if os.path.exists(self.existing_data_path):
            with open(self.existing_data_path, 'r') as file:
                self.existing_data = json.load(file)
        else:
            self.existing_data = []

    def load_feedback_data(self):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT user_input, jarviso_response, feedback FROM feedback_data')
        feedback_data = cursor.fetchall()
        conn.close()
        return feedback_data

    def integrate_new_data(self):
        if os.path.exists(self.new_data_path):
            with open(self.new_data_path, 'r') as file:
                self.new_data = json.load(file)
            self.combined_data = self.existing_data + self.new_data

        # Integrate feedback data
        feedback_data = self.load_feedback_data()
        self.combined_data += feedback_data

    def preprocess_data(self):
        # Assuming the data is in a list of tuples format: [(input, output), ...]
        # You can add any additional preprocessing steps as required.
        self.combined_data = [(item[0].strip(), item[1].strip()) for item in self.combined_data]

    def save_combined_data(self, output_path):
        with open(output_path, 'w') as file:
            json.dump(self.combined_data, file)

    def run(self, output_path):
        self.load_existing_data()
        self.integrate_new_data()
        self.preprocess_data()
        self.save_combined_data(output_path)

if __name__ == '__main__':
    existing_data_path = 'data/existing_training_data.json'
    new_data_path = 'data/recent_interactions.json'
    output_path = 'data/combined_training_data.json'

    manager = TrainingManager(existing_data_path, new_data_path)
    manager.run(output_path)
