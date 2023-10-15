class NorepinephrineNeuron:
    def __init__(self, initial_state=0):
        self.state = initial_state

    def activate(self, stimulus):
        self.state += stimulus
        # Additional logic for neuron activation, threshold checks, etc.
        pass

    def reset(self):
        self.state = 0

    def release_norepinephrine(self, amount):
        # Logic for releasing norepinephrine
        return amount * self.state

    def get_state(self):
        return self.state

    def propagate_signal(self, connected_neurons):
        for neuron in connected_neurons:
            # Logic to propagate the signal to connected neurons
            neuron.activate(self.state)


class NorepinephrineSystem:
    def __init__(self, number_of_neurons):
        self.neurons = [NorepinephrineNeuron() for _ in range(number_of_neurons)]

    def receive_input(self, input_data):
        # Logic to process the input and activate corresponding neurons
        for neuron, data in zip(self.neurons, input_data):
            neuron.activate(data)

    def release_norepinephrine_to_brain(self):
        total_norepinephrine = sum([neuron.release_norepinephrine(amount=1) for neuron in self.neurons])
        return total_norepinephrine

    def reset_all_neurons(self):
        for neuron in self.neurons:
            neuron.reset()

    def get_activity(self):
        return [neuron.get_state() for neuron in self.neurons]


if __name__ == "__main__":
    ne_system = NorepinephrineSystem(number_of_neurons=100)
    input_data = [1, 2, 3, 4, 5]  # Just an example, real data would be more complex
    ne_system.receive_input(input_data)
    norepinephrine_level = ne_system.release_norepinephrine_to_brain()
    print(f"Total Norepinephrine Released: {norepinephrine_level}")
