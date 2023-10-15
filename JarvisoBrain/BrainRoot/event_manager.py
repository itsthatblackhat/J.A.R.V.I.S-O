import sqlite3
from datetime import datetime
from enum import Enum, auto

# Define Enhanced Event Types
class EventType(Enum):
    NEW_AUDIO_INPUT = auto()
    NEW_VISUAL_INPUT = auto()
    NEW_TEXT_INPUT = auto()
    NEW_SENSORY_INPUT = auto()  # Add this line
    MEMORY_RECALL_REQUEST = auto()
    MEMORY_STORE_REQUEST = auto()
    PROCESSED_DATA_FROM_AUDITORY_CORTEX = auto()
    PROCESSED_DATA_FROM_VISUAL_CORTEX = auto()
    PROCESSED_DATA_FROM_PREFRONTAL_CORTEX = auto()
    # ... add other event types as required


# Enhanced data structure for events
class Event:
    def __init__(self, event_type, data=None, source=None, target=None, timestamp=None):
        self.type = event_type
        self.data = data
        self.source = source
        self.target = target
        self.timestamp = timestamp if timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save_to_db(self, db_path):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS events
                          (timestamp text, source text, target text, event_type text, data_payload text)''')
        cursor.execute("INSERT INTO events VALUES (?,?,?,?,?)",
                       (self.timestamp, self.source, self.target, self.type.value, str(self.data)))
        connection.commit()
        connection.close()


# Enhanced Event Dispatcher
class EventDispatcher:
    def __init__(self, db_path=None):
        self.listeners = {}
        self.db_path = db_path

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unregister_listener(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def dispatch(self, event):
        if self.db_path:  # Save event to DB if db_path is provided
            event.save_to_db(self.db_path)
        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener(event)


# Sample Event Handling
def auditory_cortex_listener(event):
    print(f"Auditory Cortex processing audio data: {event.data}")
    # ... further processing logic ...


if __name__ == "__main__":
    # Initialize the dispatcher with an optional db_path
    dispatcher = EventDispatcher(db_path='path_to_mainbrain.db')

    # Register the listener
    dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, auditory_cortex_listener)

    # Generate and dispatch a sample event
    audio_data_sample = "Hello, JARVISO!"
    event = Event(EventType.NEW_AUDIO_INPUT, audio_data_sample, source="Microphone", target="AuditoryCortex")
    dispatcher.dispatch(event)
