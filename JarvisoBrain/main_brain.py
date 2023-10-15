from JarvisoBrain.BrainRegions.AuditoryCortex.auditory_cortex import AuditoryCortex
from JarvisoBrain.BrainRegions.VisualCortex.visual_cortex import VisualCortex
from JarvisoBrain.BrainRegions.PrefrontalCortex.prefrontal_cortex import PrefrontalCortex
from JarvisoBrain.BrainRegions.SomatosensoryCortex.somatosensory_cortex import SomatosensoryCortex
from JarvisoBrain.Neurons.MotorNeurons.motor_neurons import MotorNeuron
from JarvisoBrain.BrainRoot.event_manager import EventDispatcher, EventType, Event
from JarvisoBrain.BrainRoot.brain_message import BrainMessage


class JarvisoBrain:
    def __init__(self, db_path):
        # Initialize components
        self.db_path = db_path
        self.dispatcher = EventDispatcher()


        # Initialize the different cortices with the event dispatcher and the database path
        self.auditory_cortex = AuditoryCortex(self.dispatcher, self.db_path)
        self.visual_cortex = VisualCortex(self.dispatcher, self.db_path)
        self.prefrontal_cortex = PrefrontalCortex(self.dispatcher, self.db_path)
        self.somatosensory_cortex = SomatosensoryCortex(self.dispatcher, self.db_path)

        self.motor_neurons = [MotorNeuron(i) for i in range(100)]  # Sample initialization

        # Register event listeners
        self.dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, self.auditory_cortex.process_audio_input)
        self.dispatcher.register_listener(EventType.NEW_VISUAL_INPUT, self.visual_cortex.receive_visual_input)
        # ... Register other event listeners as needed

    def receive_input(self, event_type, data, source="External", target="Brain"):
        event = Event(event_type, data, source, target)
        self.dispatcher.dispatch(event)

        # Logging the event
        message = BrainMessage(self.db_path, event_type, data, "Immediate", source, target)
        message.save_to_db()
        message.close()

    def process(self):
        # Advanced Brain processing logic
        # 1. Process sensory data
        sensory_data = self.collect_sensory_data()
        self.prefrontal_cortex.process_input(sensory_data)

        # 2. Execute decision-making
        decision = self.prefrontal_cortex.execute_decision_making()

        # 3. Translate decision to motor commands
        for neuron in self.motor_neurons:
            # Some logic to determine which motor neuron to activate based on decision
            # For example, if decision involves a specific action, activate relevant motor neurons
            pass

    def collect_sensory_data(self):
        # Aggregate data from various sensory cortices
        auditory_data = self.auditory_cortex.get_processed_data()
        visual_data = self.visual_cortex.get_processed_data()
        somatosensory_data = self.somatosensory_cortex.get_activity_map()

        # Combine them into a unified sensory data structure
        combined_data = {
            "auditory": auditory_data,
            "visual": visual_data,
            "somatosensory": somatosensory_data
        }

        return combined_data

    def execute_actions(self):
        # Execute actions based on brain processing
        # This can be based on motor neuron activations, or other internal logic
        for neuron in self.motor_neurons:
            if neuron.is_activated():
                neuron.perform_action()

    # ... Other utility methods as needed

if __name__ == "__main__":
    brain = JarvisoBrain(db_path="path_to_mainbrain.db")
    # Sample usage
    brain.receive_input(EventType.NEW_AUDIO_INPUT, "Hello, JARVISO!")
    brain.process()
    brain.execute_actions()
