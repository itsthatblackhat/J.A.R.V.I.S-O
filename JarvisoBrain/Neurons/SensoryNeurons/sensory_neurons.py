import tensorflow as tf
import numpy as np

class SensoryNeuron:
    def __init__(self, neuron_id, neuron_type='generic', synaptic_weights=None):
        self.neuron_id = neuron_id
        self.neuron_type = neuron_type  # e.g., 'photoreceptor', 'mechanoreceptor'
        self.resting_potential = -70  # mV
        self.current_potential = self.resting_potential
        self.threshold = -55  # mV
        self.refractory_period = 2  # ms
        self.last_fired = -np.inf  # Time since last action potential

        # Synaptic connections and weights
        if synaptic_weights is None:
            synaptic_weights = {}
        self.synaptic_weights = synaptic_weights  # Dictionary of connected neuron IDs and their weights

    def receive_input(self, input_signal, current_time):
        """
        Receive external sensory input.
        """
        if current_time - self.last_fired > self.refractory_period:
            self.current_potential += input_signal
            self.process_signal(current_time)

    def process_signal(self, current_time):
        """
        Process the current signal, and determine if the neuron should activate.
        """
        if self.current_potential >= self.threshold:
            self.fire_action_potential(current_time)

    def fire_action_potential(self, current_time):
        """
        Fire an action potential and reset the neuron's potential.
        """
        print(f"Neuron {self.neuron_id} is firing an action potential!")
        self.last_fired = current_time
        # Propagate the action potential to connected neurons
        # This is a simplified representation. In reality, we'd need to consider the type of synapse, neurotransmitter, etc.
        for connected_neuron, weight in self.synaptic_weights.items():
            connected_neuron.receive_input(weight * 15, current_time)  # Propagate a fraction of the max potential
        self.current_potential = self.resting_potential

    def add_synaptic_connection(self, neuron, weight):
        """
        Add a synaptic connection to another neuron with a specified weight.
        """
        self.synaptic_weights[neuron] = weight

    def __str__(self):
        return f"SensoryNeuron-{self.neuron_id} | Current Potential: {self.current_potential} mV | Type: {self.neuron_type}"


# Sample usage:

if __name__ == "__main__":
    # Create two sensory neurons
    neuron1 = SensoryNeuron(neuron_id=1, neuron_type='photoreceptor')
    neuron2 = SensoryNeuron(neuron_id=2, neuron_type='mechanoreceptor')

    # Connect neuron1 to neuron2
    neuron1.add_synaptic_connection(neuron2, weight=0.5)

    # Simulate receiving external sensory input
    neuron1.receive_input(20, current_time=0)  # Intensity of 20 mV at time=0ms
    print(neuron1)
    print(neuron2)

    # Simulate a short time passing
    neuron1.receive_input(10, current_time=1)  # Further input at time=1ms
    print(neuron1)
    print(neuron2)
