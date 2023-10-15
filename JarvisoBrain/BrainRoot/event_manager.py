from enum import Enum, auto


# Step 1: Define Enhanced Event Types
class EventType(Enum):
    NEW_AUDIO_INPUT = auto()
    NEW_VISUAL_INPUT = auto()
    NEW_TEXT_INPUT = auto()
    MEMORY_RECALL_REQUEST = auto()
    MEMORY_STORE_REQUEST = auto()
    PROCESSED_DATA_FROM_AUDITORY_CORTEX = auto()
    PROCESSED_DATA_FROM_VISUAL_CORTEX = auto()
    PROCESSED_DATA_FROM_PREFRONTAL_CORTEX = auto()
    # Add more event types as your project grows


# Data structure for events
class Event:
    def __init__(self, event_type, data=None, source=None, target=None):
        self.type = event_type
        self.data = data
        self.source = source  # e.g., 'AuditoryCortex'
        self.target = target  # e.g., 'Hippocampus'


# Step 2: Implement the Enhanced Event Dispatcher
class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unregister_listener(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def dispatch(self, event):
        if event.type in self.listeners:
            for listener in self.listeners[event.type]:
                listener(event)


# Step 3: Implement Region-Specific Listeners (Sample)
def auditory_cortex_listener(event):
    print(f"Auditory Cortex processing audio data: {event.data}")
    # Process the audio data, and then:
    # new_event = Event(EventType.PROCESSED_DATA_FROM_AUDITORY_CORTEX, processed_data)
    # dispatcher.dispatch(new_event)


# Example Usage:
if __name__ == "__main__":
    # Initialize the dispatcher
    dispatcher = EventDispatcher()

    # Register a sample listener
    dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, auditory_cortex_listener)

    # Generate a sample event
    audio_data_sample = "Hello, JARVISO!"
    event = Event(EventType.NEW_AUDIO_INPUT, audio_data_sample)
    dispatcher.dispatch(event)
