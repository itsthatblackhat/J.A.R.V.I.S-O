from JarvisoBrain.BrainRegions.AuditoryCortex.auditory_cortex import AuditoryCortex
from JarvisoBrain.BrainRegions.VisualCortex.visual_cortex import VisualCortex
from JarvisoBrain.BrainRegions.PrefrontalCortex.prefrontal_cortex import PrefrontalCortex
from JarvisoBrain.BrainRegions.SomatosensoryCortex.somatosensory_cortex import SomatosensoryCortex
from JarvisoBrain.Neurons.MotorNeurons.motor_neurons import MotorNeuron
from JarvisoBrain.Neurons.SensoryNeurons.sensory_neurons import SensoryNeuron, VisualNeuron, AuditoryNeuron  # Assuming these are defined
from JarvisoBrain.Neurons.Interneurons.interneurons import Interneuron
from JarvisoBrain.BrainRoot.event_manager import EventDispatcher, EventType, Event
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType  # Import MessageType as well


class JarvisoBrain:
    def __init__(self, db_path):
        # Initialize components
        self.db_path = db_path
        self.dispatcher = EventDispatcher()

        # Initialize sensory neurons, motor neurons, and interneurons
        self.sensory_neurons = [SensoryNeuron(i) for i in range(100)]
        self.motor_neurons = [MotorNeuron(i) for i in range(100)]
        self.interneurons = [Interneuron(i) for i in range(100)]

        # Initialize the different cortices with the event dispatcher and the database path
        self.auditory_cortex = AuditoryCortex(self.dispatcher)
        self.visual_cortex = VisualCortex(self.dispatcher)
        self.prefrontal_cortex = PrefrontalCortex(
            sensory_neurons=self.sensory_neurons,
            motor_neurons=self.motor_neurons,
            interneurons=self.interneurons,
            dispatcher=self.dispatcher,  # Provide the dispatcher here
            database_path=self.db_path)
        self.somatosensory_cortex = SomatosensoryCortex(dispatcher=self.dispatcher, number_of_neurons=100)  # Example

        # Register event listeners
        self.dispatcher.register_listener(EventType.NEW_AUDIO_INPUT, self.auditory_cortex.process_audio_input)
        self.dispatcher.register_listener(EventType.NEW_VISUAL_INPUT, self.visual_cortex.receive_visual_input)
        # Add other event listeners as required

    def receive_input(self, event_type, data, source="External", target="Brain"):
        event = Event(event_type, data, source, target)
        self.dispatcher.dispatch(event)

        # Logging the event, use MessageType.SENSORY_DATA instead of event_type
        message = BrainMessage(self.db_path, MessageType.SENSORY_DATA, data, "Immediate", source, target)
        message.save_to_db()
        message.close()

    def process(self):
        # 1. Process sensory data
        sensory_data_dict = self.collect_sensory_data()
        sensory_event = Event(event_type=EventType.PROCESSED_SENSORY_DATA, data=sensory_data_dict)
        self.prefrontal_cortex.process_input(sensory_event)

        # 2. Execute decision-making
        decision = self.prefrontal_cortex.execute_decision_making()

        # 3. Translate decision to motor commands
        for neuron in self.motor_neurons:
            # Here, you need the logic to determine which motor neuron to activate based on the decision.
            pass

    def collect_sensory_data(self):
        auditory_data = self.auditory_cortex.get_processed_data()  # Ensure the method exists in AuditoryCortex
        visual_data = self.visual_cortex.get_processed_data()
        somatosensory_data = self.somatosensory_cortex.get_activity_map()

        combined_data = {
            "auditory": auditory_data,
            "visual": visual_data,
            "somatosensory": somatosensory_data
        }

        return combined_data
    def execute_actions(self):
        for neuron in self.motor_neurons:
            if neuron.is_activated():
                neuron.perform_action()

if __name__ == "__main__":
    brain = JarvisoBrain(db_path="JarvisoBrain/NeuralDatabase/mainbrain.db")
    brain.receive_input(EventType.NEW_AUDIO_INPUT, "Hello, JARVISO!")
    brain.process()
    brain.execute_actions()
