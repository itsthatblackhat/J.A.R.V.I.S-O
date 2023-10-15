import tensorflow as tf
import numpy as np

class SensoryNeuron:
    def __init__(self, neuron_id, neuron_type='generic', synaptic_weights=None):
        self.neuron_id = neuron_id
        self.neuron_type = neuron_type
        self.resting_potential = -70  # mV
        self.current_potential = self.resting_potential
        self.threshold = -55  # mV
        self.refractory_period = 2  # ms
        self.last_fired = -np.inf  # Time since last action potential

        # Synaptic connections and weights
        if synaptic_weights is None:
            synaptic_weights = {}
        self.synaptic_weights = synaptic_weights

    def receive_input(self, input_signal, current_time):
        if current_time - self.last_fired > self.refractory_period:
            self.current_potential += input_signal
            self.process_signal(current_time)

    def process_signal(self, current_time):
        if self.current_potential >= self.threshold:
            self.fire_action_potential(current_time)

    def fire_action_potential(self, current_time):
        print(f"Neuron {self.neuron_id} is firing an action potential!")
        self.last_fired = current_time
        for connected_neuron, weight in self.synaptic_weights.items():
            connected_neuron.receive_input(weight * 15, current_time)
        self.current_potential = self.resting_potential

    def add_synaptic_connection(self, neuron, weight):
        self.synaptic_weights[neuron] = weight

    def __str__(self):
        return f"SensoryNeuron-{self.neuron_id} | Current Potential: {self.current_potential} mV | Type: {self.neuron_type}"

# Derived visual neuron class
class VisualNeuron(SensoryNeuron):
    def __init__(self, neuron_id, synaptic_weights=None):
        super().__init__(neuron_id, 'photoreceptor', synaptic_weights)
        # Specific attributes for visual neurons can be added here

# Derived auditory neuron class
class AuditoryNeuron(SensoryNeuron):
    def __init__(self, neuron_id, synaptic_weights=None):
        super().__init__(neuron_id, 'mechanoreceptor', synaptic_weights)
        # Specific attributes for auditory neurons can be added here

# Sample usage
if __name__ == "__main__":
    neuron1 = VisualNeuron(neuron_id=1)
    neuron2 = AuditoryNeuron(neuron_id=2)

    neuron1.add_synaptic_connection(neuron2, weight=0.5)

    neuron1.receive_input(20, current_time=0)
    print(neuron1)
    print(neuron2)

    neuron1.receive_input(10, current_time=1)
    print(neuron1)
    print(neuron2)
