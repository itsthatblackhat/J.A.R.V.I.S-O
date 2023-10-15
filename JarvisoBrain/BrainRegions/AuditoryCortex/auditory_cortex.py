import sounddevice as sd
import numpy as np

from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType, ProcessingDirective

dispatcher = EventDispatcher()

class AuditoryNeuron:
    def __init__(self, neuron_type='primary_neuron', initial_state=0):
        self.neuron_type = neuron_type
        self.state = initial_state

    def activate(self, auditory_signal):
        """Activate the neuron based on the auditory signal."""
        self.state += auditory_signal
        # You might want to add additional logic here like threshold checks.

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state

    def propagate_signal(self, connected_neurons):
        """Propagate the neuron's current state to connected neurons."""
        for neuron in connected_neurons:
            neuron.activate(self.state)

class AuditoryCortex:
    def __init__(self, number_of_neurons=100, db_path='path_to_db'):
        self.neurons = [AuditoryNeuron() for _ in range(number_of_neurons)]
        self.dispatcher = dispatcher
        self.db_path = db_path
        dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, self.process_audio_input)

    def capture_audio(self, duration=5):
        """Capture audio from the default microphone."""
        samplerate = 44100  # Standard sampling rate for audio
        audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='float64')
        sd.wait()
        return audio

    def preprocess_audio(self, audio):
        """Preprocess the captured audio."""
        # For this example, we'll take the mean value of the audio as a representation.
        return np.mean(audio, axis=1)

    def process_audio_input(self, event):
        """Process the auditory input."""
        # The data is extracted from the event and passed to the neurons for activation.
        audio_data = event.data['data_payload']
        for neuron in self.neurons:
            neuron.activate(audio_data)

        # After processing, store the neuron states or further process them.
        processed_data = [neuron.get_state() for neuron in self.neurons]

        # Send the processed data to another part of the brain or store it.
        # This is just a placeholder and can be expanded based on your requirements.
        message = BrainMessage(
            db_path=self.db_path,
            message_type=MessageType.PROCESSED_DATA,
            data_payload=processed_data,
            processing_directive=ProcessingDirective.STORE,
            source="AuditoryCortex",
            destination="MemoryStorage"
        )
        event = Event(EventType.MEMORY_STORE_REQUEST, message)
        dispatcher.dispatch(event)

    def reset_all_neurons(self):
        for neuron in self.neurons:
            neuron.reset()

if __name__ == "__main__":
    auditory_cortex = AuditoryCortex()

    # Capture and preprocess audio
    raw_audio = auditory_cortex.capture_audio()
    processed_audio = auditory_cortex.preprocess_audio(raw_audio)

    # Dispatch an event with the processed audio for the auditory cortex to process
    message = BrainMessage(
        db_path=auditory_cortex.db_path,
        message_type=MessageType.SENSORY_DATA,
        data_payload=processed_audio,
        processing_directive=ProcessingDirective.IMMEDIATE,
        source="Microphone",
        destination="AuditoryCortex"
    )
    event = Event(EventType.NEW_AUDIO_INPUT, message)
    dispatcher.dispatch(event)
