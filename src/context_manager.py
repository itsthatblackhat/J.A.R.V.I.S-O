import sqlite3

DATABASE_NAME = "jarviso.db"

class ContextManager:
    def __init__(self, max_length=5):
        self.context = []
        self.max_length = max_length
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS conversation_context (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                bot_response TEXT
            )
        ''')
        self.conn.commit()

    def update_context(self, user_input, bot_response):
        # Ensure neither user_input nor bot_response are None before proceeding
        if user_input and bot_response:
            # Update in-memory list
            if len(self.context) >= self.max_length:
                self.context.pop(0)
            self.context.append((user_input, bot_response))

            # Update database
            c = self.conn.cursor()
            c.execute('''
                INSERT INTO conversation_context (user_input, bot_response)
                VALUES (?, ?)
            ''', (user_input, bot_response))
            self.conn.commit()

    def get_context(self):
        # Filter out any None values
        return [item for item in self.context if item[0] and item[1]]

    def retrieve_context_from_db(self):
        c = self.conn.cursor()
        c.execute('SELECT user_input, bot_response FROM conversation_context ORDER BY id DESC LIMIT ?', (self.max_length,))
        rows = c.fetchall()
        self.context = [tuple(row) for row in rows if row[0] and row[1]]  # filtering out None

    def clear_context(self):
        self.context = []
        c = self.conn.cursor()
        c.execute('DELETE FROM conversation_context')
        self.conn.commit()

    def close(self):
        self.conn.close()
