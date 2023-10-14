import sqlite3

DATABASE_NAME = "jarviso.db"

class ContextManager:
    def __init__(self, max_length=5):
        self.context = []
        self.max_length = max_length
        self.initialize_database()

    def initialize_database(self):
        """ Initialize the database connection and tables. """
        try:
            self.conn = sqlite3.connect(DATABASE_NAME)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def create_table(self):
        """ Create the necessary tables if they don't exist. """
        try:
            c = self.conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS conversation_context (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    user_input TEXT,
                    bot_response TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Table creation error: {e}")

    def update_context(self, user_input, bot_response, session_id="default_session"):
        """ Update the context based on user input and bot response. """
        if user_input and bot_response:
            if len(self.context) >= self.max_length:
                self.context.pop(0)
            self.context.append((session_id, user_input, bot_response))
            self.update_database(session_id, user_input, bot_response)

    def update_database(self, session_id, user_input, bot_response):
        """ Update the database with the new context. """
        try:
            c = self.conn.cursor()
            c.execute('''
                INSERT INTO conversation_context (session_id, user_input, bot_response)
                VALUES (?, ?, ?)
            ''', (session_id, user_input, bot_response))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database insertion error: {e}")

    def get_context(self, session_id="default_session"):
        """ Retrieve the context for a specific session. """
        self.retrieve_context_from_db(session_id)
        return [(user_input, bot_response) for _, user_input, bot_response in self.context]

    def retrieve_context_from_db(self, session_id):
        """ Retrieve the context from the database for a specific session. """
        try:
            c = self.conn.cursor()
            c.execute('SELECT user_input, bot_response FROM conversation_context WHERE session_id = ? ORDER BY id DESC LIMIT ?', (session_id, self.max_length,))
            rows = c.fetchall()
            self.context = [(session_id, user_input, bot_response) for user_input, bot_response in rows]
        except sqlite3.Error as e:
            print(f"Database retrieval error: {e}")

    def clear_context(self, session_id):
        """ Clear the context for a specific session. """
        self.context = []
        try:
            c = self.conn.cursor()
            c.execute('DELETE FROM conversation_context WHERE session_id = ?', (session_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database deletion error: {e}")

    def close(self):
        """ Close the database connection. """
        self.conn.close()
