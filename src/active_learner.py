import sqlite3
import random

DATABASE_NAME = "jarviso.db"

class ActiveLearner:
    def __init__(self):
        self.unlabeled_data = []
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS uncertain_interactions (
                user_input TEXT,
                bot_response TEXT,
                confidence_score REAL
            )
        ''')
        self.conn.commit()

    def add_unlabeled_data(self, user_input, bot_response, confidence_score):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO uncertain_interactions (user_input, bot_response, confidence_score)
            VALUES (?, ?, ?)
        ''', (user_input, bot_response, confidence_score))
        self.conn.commit()

    def get_data_for_labeling(self):
        c = self.conn.cursor()
        c.execute('SELECT user_input, bot_response FROM uncertain_interactions ORDER BY RANDOM() LIMIT 1')
        row = c.fetchone()
        if row:
            return row[0], row[1]
        return None

    def receive_label(self, interaction, feedback):
        user_input, bot_response = interaction
        c = self.conn.cursor()
        c.execute('''
            DELETE FROM uncertain_interactions WHERE user_input = ? AND bot_response = ?
        ''', (user_input, bot_response))
        self.conn.commit()

    def close(self):
        self.conn.close()
