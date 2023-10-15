import sqlite3
import logging
from datetime import datetime

from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType, ProcessingDirective

class MemoryManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.dispatcher = EventDispatcher(db_path)
        logging.basicConfig(level=logging.INFO)

    def _connect(self):
        """Utility method to establish a connection."""
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {str(e)}")
            return None

    def store_neuron_data(self, neuron_id, neuron_type, resting_potential, current_potential, last_fired, threshold):
        """Store data related to a neuron."""
        query = '''
        INSERT INTO neurons (neuron_id, neuron_type, resting_potential, current_potential, last_fired, threshold)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        try:
            with self._connect() as conn:
                conn.execute(query, (neuron_id, neuron_type, resting_potential, current_potential, last_fired, threshold))
            logging.info(f"Stored data for neuron {neuron_id}")

            message = BrainMessage(
                db_path=self.db_path,
                message_type=MessageType.MEMORY_STORE_REQUEST,
                data_payload={"neuron_id": neuron_id, "type": "neuron"},
                processing_directive=ProcessingDirective.STORE,
                source="MemoryManager",
                destination="ProcessingManager"
            )
            event = Event(EventType.MEMORY_STORE_REQUEST, message)
            self.dispatcher.dispatch(event)

        except sqlite3.Error as e:
            logging.error(f"Error storing data for neuron {neuron_id}: {str(e)}")

    def retrieve_neuron_data(self, neuron_id):
        """Retrieve data related to a neuron."""
        query = '''SELECT * FROM neurons WHERE neuron_id = ?'''
        try:
            with self._connect() as conn:
                cur = conn.cursor()
                cur.execute(query, (neuron_id,))
                data = cur.fetchone()

            message = BrainMessage(
                db_path=self.db_path,
                message_type=MessageType.MEMORY_RECALL_REQUEST,
                data_payload={"neuron_id": neuron_id, "type": "neuron"},
                processing_directive=ProcessingDirective.RECALL,
                source="MemoryManager",
                destination="ProcessingManager"
            )
            event = Event(EventType.MEMORY_RECALL_REQUEST, message)
            self.dispatcher.dispatch(event)

            return data
        except sqlite3.Error as e:
            logging.error(f"Error retrieving data for neuron {neuron_id}: {str(e)}")
            return None

    def log_interaction(self, user_input, jarvis_output):
        # Here, we'll save the interaction to the database.
        # For simplicity, let's assume you have a table named 'interactions' with columns 'user_input' and 'jarvis_output'.

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Ensure the table exists (you may want to move this to the __init__ method or a separate setup method)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                jarvis_output TEXT,
                timestamp TEXT
            )
        ''')

        # Insert the new interaction
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO interactions (user_input, jarvis_output, timestamp) VALUES (?, ?, ?)",
                       (user_input, jarvis_output, timestamp))

        conn.commit()
        conn.close()

    # Additional methods for synaptic data
    # ... (similar structure as the above methods, but for synapses)

    # ... further methods for interaction logs, feedback, batch operations, etc. ...

# Sample usage
if __name__ == "__main__":
    manager = MemoryManager('MainBrain.db')
    manager.store_neuron_data(1, 'sensory', -70, -65, 0, -55)
    print(manager.retrieve_neuron_data(1))
