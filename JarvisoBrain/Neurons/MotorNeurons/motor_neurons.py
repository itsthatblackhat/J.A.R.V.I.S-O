import tensorflow as tf
import numpy as np

class MotorNeuron:
    def __init__(self, neuron_id, neuron_type='alpha', synaptic_weights=None):
        self.neuron_id = neuron_id
        self.neuron_type = neuron_type  # either 'alpha' or 'gamma'
        self.resting_potential = -70  # mV
        self.current_potential = self.resting_potential
        self.threshold = -55  # mV
        self.refractory_period = 2  # ms
        self.last_fired = -np.inf  # Time since last action potential

        # Synaptic connections and weights
        if synaptic_weights is None:
            synaptic_weights = {}
        self.synaptic_weights = synaptic_weights

    def is_activated(self):
        return self.current_potential >= self.threshold

    def perform_action(self):
        if self.is_activated():
            # Placeholder: logic to perform an action
            print(f"Motor Neuron {self.neuron_id} is performing an action!")

    def receive_input(self, input_signal, current_time):
        """
        Receive input from other neurons.
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
        Fire an action potential and activate the corresponding muscle.
        """
        print(f"Motor Neuron {self.neuron_id} is firing an action potential!")
        self.last_fired = current_time
        self.activate_muscle()

    def activate_muscle(self):
        """
        Simulate the activation of a muscle based on the neuron's action potential.
        """
        if self.neuron_type == 'alpha':
            print(f"Motor Neuron {self.neuron_id} is activating skeletal muscle fibers!")
        elif self.neuron_type == 'gamma':
            print(f"Motor Neuron {self.neuron_id} is activating intrafusal muscle fibers!")
        # Here, you can add more complexity such as the degree of muscle contraction, etc.

    def add_synaptic_connection(self, neuron, weight):
        """
        Add a synaptic connection to another neuron with a specified weight.
        """
        self.synaptic_weights[neuron] = weight

    def __str__(self):
        return f"MotorNeuron-{self.neuron_id} | Current Potential: {self.current_potential} mV | Type: {self.neuron_type}"


def get_output(self):
    # For now, return a binary output
    return 1 if self.activation_level > 0.5 else 0



# Sample usage:

if __name__ == "__main__":
    # Create two motor neurons
    neuron1 = MotorNeuron(neuron_id=1, neuron_type='alpha')
    neuron2 = MotorNeuron(neuron_id=2, neuron_type='gamma')

    # Simulate receiving input from other neurons
    neuron1.receive_input(20, current_time=0)  # Intensity of 20 mV at time=0ms
    print(neuron1)

    # Simulate a short time passing
    neuron1.receive_input(10, current_time=1)  # Further input at time=1ms
    print(neuron1)
