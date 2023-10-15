from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, ProcessingDirective

class SomatoNeuron:
    def __init__(self, neuron_type, sensory_region, initial_state=0):
        self.neuron_type = neuron_type  # e.g., 'touch', 'temperature'
        self.sensory_region = sensory_region  # e.g., 'hand', 'foot', 'face'
        self.state = initial_state

    def activate(self, sensory_input, region, intensity):
        # Activation based on sensory input, its region, and intensity
        if self.sensory_region == region and self.neuron_type == sensory_input:
            self.state += intensity

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state


class SomatosensoryCortex:
    def __init__(self, dispatcher, number_of_neurons, db_path=None):
        self.neurons = {
            'hand': [SomatoNeuron(neuron_type='touch', sensory_region='hand') for _ in range(number_of_neurons)],
            'foot': [SomatoNeuron(neuron_type='touch', sensory_region='foot') for _ in range(number_of_neurons)],
            # Add more sensory regions and types as necessary
        }
        self.db_path = db_path
        self.dispatcher = dispatcher
        self.register_to_dispatcher()

    def process_sensory_input(self, sensory_type, region, intensity=1):
        # Distribute the sensory data to neurons based on their type, region, and intensity
        for neuron in self.neurons.get(region, []):
            neuron.activate(sensory_type, region, intensity)

        # Create a message to log this processing
        message = BrainMessage(
            db_path=self.db_path,
            message_type=EventType.PROCESSED_SENSORY_DATA,
            data_payload={"type": sensory_type, "region": region, "intensity": intensity},
            processing_directive=ProcessingDirective.STORE,
            source="SomatosensoryCortex",
            destination="MemoryManager"
        )
        message.save_to_db()
        message.close()

    def get_activity_map(self):
        return {region: [neuron.get_state() for neuron in self.neurons[region]] for region in self.neurons}

    def reset_all_neurons(self):
        for region in self.neurons:
            for neuron in self.neurons[region]:
                neuron.reset()

    def handle_event(self, event):
        if event.event_type == EventType.NEW_SENSORY_INPUT:
            sensory_data = event.data
            self.process_sensory_input(sensory_data['type'], sensory_data['region'], sensory_data.get('intensity', 1))

    def register_to_dispatcher(self):
        self.dispatcher.register_listener(EventType.NEW_SENSORY_INPUT, self.handle_event)


if __name__ == "__main__":
    dispatcher = EventDispatcher(db_path='path_to_mainbrain.db')
    somatosensory_cortex = SomatosensoryCortex(dispatcher=dispatcher, number_of_neurons=100, db_path='path_to_mainbrain.db')
    sample_sensory_data = {
        'type': 'touch',
        'region': 'hand',
        'intensity': 1.5  # Placeholder for the intensity of sensory data
    }
    event = Event(EventType.NEW_SENSORY_INPUT, sample_sensory_data, source="SensoryOrgan", target="SomatosensoryCortex")
    dispatcher.dispatch(event)
    activity_map = somatosensory_cortex.get_activity_map()
    print(activity_map)
