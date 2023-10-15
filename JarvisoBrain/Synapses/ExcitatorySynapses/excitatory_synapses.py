import tensorflow as tf

class InhibitorySynapse:
    def __init__(self, pre_neuron, post_neuron):
        self.pre_neuron = pre_neuron
        self.post_neuron = post_neuron
        self.weight = 1.0  # Initial weight

    def transmit_signal(self):
        signal_strength = -self.pre_neuron.potential * self.weight  # Negative value to inhibit
        self.post_neuron.receive_signal(signal_strength)
