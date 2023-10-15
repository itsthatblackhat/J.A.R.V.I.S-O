import numpy as np
from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher


class Interneuron:
    def __init__(self, neuron_id, neuron_type='projection', dispatcher=None):
        self.neuron_id = neuron_id
        self.neuron_type = neuron_type  # Can be 'local' or 'projection'
        self.activation = 0.0
        self.threshold = -55.0  # Activation threshold, might adjust based on experiments
        self.connections = []  # List of connected neurons (could be other interneurons, sensory, or motor neurons)
        self.dispatcher = dispatcher  # The event dispatcher for broadcasting events

    def process(self):
        """
        Process the current activation state of the neuron,
        determining if it should fire based on its threshold.
        """
        if self.activation > self.threshold:
            self.fire()

    def add_connection(self, neuron):
        """Connect another neuron to this interneuron."""
        self.connections.append(neuron)

    def receive_signal(self, signal_strength):
        """Receive an input signal."""
        self.activation += signal_strength
        if self.activation > self.threshold:
            self.fire()

    def fire(self):
        """Fire the neuron if activation exceeds the threshold."""
        self.send_signal()
        self.activation = 0.0  # Reset activation after firing

    def send_signal(self):
        """Send a signal to all connected neurons."""
        for neuron in self.connections:
            neuron.receive_signal(self.activation)  # Simplistic signal propagation; might adjust
        if self.dispatcher:
            # Inform the larger system that this neuron has fired
            event = Event(event_type=EventType.NEURAL_UPDATE, data={"neuron_id": self.neuron_id, "activation": self.activation})
            self.dispatcher.dispatch(event)

    def reset(self):
        """Reset neuron activation."""
        self.activation = 0.0


if __name__ == "__main__":
    from JarvisoBrain.BrainRoot.event_manager import EventDispatcher

    def neuron_activity_listener(event):
        """Sample listener to demonstrate how other parts of the system can react to neuron activity."""
        print(f"Neuron {event.data['neuron_id']} has fired with activation {event.data['activation']}.")

    # Example usage:
    dispatcher = EventDispatcher()

    # Register the listener
    dispatcher.register_listener(EventType.NEURAL_UPDATE, neuron_activity_listener)

    neuron1 = Interneuron(neuron_id=1, neuron_type='projection', dispatcher=dispatcher)
    neuron2 = Interneuron(neuron_id=2, neuron_type='local', dispatcher=dispatcher)

    neuron1.add_connection(neuron2)
    neuron1.receive_signal(56.0)  # This will cause neuron1 to fire and the listener will be triggered
