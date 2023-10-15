import sqlite3

from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType, ProcessingDirective
from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher

DATABASE_PATH = "JarvisoBrain/NeuralDatabase/mainbrain.db"
dispatcher = EventDispatcher()


class BasalGangliaNeuron:
    def __init__(self, neuron_type, initial_state=0):
        self.neuron_type = neuron_type  # Could be 'striatal_neuron', 'pallidal_neuron', etc.
        self.state = initial_state

    def activate(self, stimulus):
        self.state += stimulus
        # Additional logic for neuron activation, threshold checks, etc.
        pass

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state

    def propagate_signal(self, connected_neurons):
        for neuron in connected_neurons:
            neuron.activate(self.state)


class BasalGanglia:
    def __init__(self, number_of_neurons):
        self.neurons = [BasalGangliaNeuron(neuron_type='striatal_neuron') for _ in range(number_of_neurons)]
        self._connect_to_database()

    def _connect_to_database(self):
        try:
            self.conn = sqlite3.connect(DATABASE_PATH)
            self.cursor = self.conn.cursor()
            # Create table for basal ganglia neurons if it doesn't exist
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS basal_ganglia_neurons (
                    id INTEGER PRIMARY KEY,
                    neuron_type TEXT NOT NULL,
                    state FLOAT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Exception in _connect_to_database: {e}")

    def _close_database(self):
        try:
            self.conn.close()
        except Exception as e:
            print(f"Exception in _close_database: {e}")

    def process_input(self, input_data):
        try:
            for neuron, data in zip(self.neurons, input_data):
                neuron.activate(data)
            for neuron in self.neurons:
                self.cursor.execute("INSERT INTO basal_ganglia_neurons (neuron_type, state) VALUES (?, ?)",
                                    (neuron.neuron_type, neuron.get_state()))
            self.conn.commit()
        except Exception as e:
            print(f"Exception in process_input: {e}")

    def regulate_movement(self, motor_system):
        for neuron in self.neurons:
            neuron.propagate_signal(motor_system)

    def process_learning(self, learning_data):
        # Logic to handle procedural learning and habit formation
        pass

    def reset_all_neurons(self):
        try:
            for neuron in self.neurons:
                neuron.reset()
            self.cursor.execute("DELETE FROM basal_ganglia_neurons")
            self.conn.commit()
        except Exception as e:
            print(f"Exception in reset_all_neurons: {e}")

    def get_activity(self):
        return [neuron.get_state() for neuron in self.neurons]

    def retrieve_neuron_data_from_db(self):
        try:
            self.cursor.execute("SELECT neuron_type, state FROM basal_ganglia_neurons")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Exception in retrieve_neuron_data_from_db: {e}")

    def __del__(self):
        # Destructor to ensure database connection is closed
        self._close_database()


if __name__ == "__main__":
    basal_ganglia = BasalGanglia(number_of_neurons=100)
    input_data = [1, 2, 3, 4, 5]  # Just an example, real data would be more complex
    basal_ganglia.process_input(input_data)
    basal_ganglia_activity = basal_ganglia.get_activity()
    print(basal_ganglia_activity)
