import numpy as np
import tensorflow as tf


class Interneuron:
    def __init__(self, neuron_id, neuron_type='projection'):
        self.neuron_id = neuron_id
        self.neuron_type = neuron_type  # Can be 'local' or 'projection'
        self.activation = 0.0
        self.threshold = -55.0  # Activation threshold, you might adjust this based on experiments
        self.connections = []  # List of connected neurons (could be other interneurons, sensory, or motor neurons)

    def add_connection(self, neuron):
        """Connect another neuron to this interneuron."""
        self.connections.append(neuron)

    def receive_signal(self, signal_strength):
        """Receive an input signal."""
        self.activation += signal_strength

    def fire(self):
        """Fire the neuron if activation exceeds the threshold."""
        if self.activation > self.threshold:
            self.send_signal()
            self.activation = 0.0  # Reset activation after firing

    def send_signal(self):
        """Send a signal to all connected neurons."""
        for neuron in self.connections:
            neuron.receive_signal(self.activation)  # This is a simplistic signal propagation. You might want to adjust.

    def reset(self):
        """Reset neuron activation."""
        self.activation = 0.0

# Example usage:
# neuron1 = Interneuron(neuron_id=1, neuron_type='projection')
# neuron2 = Interneuron(neuron_id=2, neuron_type='local')
# neuron1.add_connection(neuron2)
# neuron1.receive_signal(56.0)
# neuron1.fire()
