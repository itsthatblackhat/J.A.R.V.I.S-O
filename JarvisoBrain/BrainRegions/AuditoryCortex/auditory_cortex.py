import sounddevice as sd

from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType, ProcessingDirective

dispatcher = EventDispatcher()


db_path='JarvisoBrain/NeuralDatabase/mainbrain.db'

class AuditoryNeuron:
    def __init__(self, neuron_type, initial_state=0):
        self.neuron_type = neuron_type  # Could be 'primary_neuron', 'secondary_neuron', etc.
        self.state = initial_state

    def activate(self, auditory_signal):
        self.state += auditory_signal
        # Additional logic for neuron activation, threshold checks, etc.
        pass

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state

    def propagate_signal(self, connected_neurons):
        for neuron in connected_neurons:
            # Logic to propagate the signal to connected neurons
            neuron.activate(self.state)


class AuditoryCortex:
    def __init__(self, number_of_neurons, db_path):
        self.neurons = [AuditoryNeuron(neuron_type='primary_neuron') for _ in range(number_of_neurons)]
        self.db_path = db_path
        self.dispatcher = dispatcher
        self.db_path = db_path
        # Register the listener with the dispatcher
        dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, self.receive_auditory_signal)

    def capture_audio(self, duration=5):
        """Capture audio from the default microphone for a specified duration."""
        samplerate = 44100  # Standard sampling rate for audio
        audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='float64')
        sd.wait()
        return audio

    def preprocess_audio(self, audio):
        """Placeholder for audio preprocessing logic."""
        # Convert raw audio data into a format or extract features suitable for the neurons
        # For simplicity, we'll just take the mean for now
        return audio.mean(axis=1)

    def receive_auditory_signal(self, event):
        auditory_data = event.data.data_payload  # Extract auditory data from the event's BrainMessage
        # Logic to process the auditory data and activate corresponding neurons
        for neuron, data in zip(self.neurons, auditory_data):
            neuron.activate(data)

        # After processing, generate new event (for example, storing in memory or passing to another region)
        processed_data = self.get_activity()
        new_event = Event(EventType.PROCESSED_DATA_FROM_AUDITORY_CORTEX, processed_data)
        dispatcher.dispatch(new_event)

    def process_signal(self):
        # Logic to further process the auditory signal for higher-level tasks
        pass

    def process_audio_input(self, event):
        # Placeholder: processing logic
        print(f"Processing audio data: {event.data}")

    def get_processed_data(self):
        # Placeholder: return processed audio data
        return "Processed audio data"

    def reset_all_neurons(self):
        for neuron in self.neurons:
            neuron.reset()

    def get_activity(self):
        return [neuron.get_state() for neuron in self.neurons]


if __name__ == "__main__":
    auditory_cortex = AuditoryCortex(number_of_neurons=100, db_path='JarvisoBrain/NeuralDatabase/mainbrain.db')

    # Capture and preprocess audio from the microphone
    raw_audio = auditory_cortex.capture_audio()
    processed_audio = auditory_cortex.preprocess_audio(raw_audio)

    # Create a BrainMessage and dispatch it
    audio_brain_message = BrainMessage(
        db_path=auditory_cortex.db_path,
        message_type=MessageType.SENSORY_DATA,
        data_payload=processed_audio,
        processing_directive=ProcessingDirective.IMMEDIATE,
        source="Microphone",
        destination="AuditoryCortex"
    )

    audio_data_event = Event(EventType.NEW_AUDIO_INPUT, audio_brain_message)
    dispatcher.dispatch(audio_data_event)
