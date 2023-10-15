import cv2
from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.Neurons.MotorNeurons.motor_neurons import MotorNeuron

dispatcher = EventDispatcher()


class WebcamInterface:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # 0 indicates default webcam

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()


class VisualNeuron:
    def __init__(self, neuron_type, initial_state=0):
        self.neuron_type = neuron_type  # Could be 'Simple_cell', 'Complex_cell', etc.
        self.state = initial_state

    def activate(self, stimulus):
        """Activate the neuron based on visual stimulus."""
        self.state += stimulus

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state


class VisualCortex:
    def __init__(self, dispatcher, number_of_neurons=100):
        self.dispatcher = dispatcher
        self.neurons = {
            'Simple_cell': [VisualNeuron(neuron_type='Simple_cell') for _ in range(number_of_neurons)],
            'Complex_cell': [VisualNeuron(neuron_type='Complex_cell') for _ in range(number_of_neurons)],
        }
        self.motor_neurons = {
            'webcam': MotorNeuron(neuron_id=1, neuron_type='webcam')
        }

    def receive_visual_input(self, visual_data, neuron_type):
        """Receive and process visual input for specific neuron types."""
        for neuron, data in zip(self.neurons[neuron_type], visual_data):
            neuron.activate(data)

            # Check conditions for activating motor actions
            if neuron.get_state() > 50:  # Define the threshold value as per requirement
                self.motor_neurons['webcam'].receive_input(20, current_time=0)  # Placeholder values

        # Dispatch processed visual data
        event = Event(EventType.PROCESSED_DATA_FROM_VISUAL_CORTEX, data=visual_data)
        self.dispatcher.dispatch(event)

    def receive_realtime_input(self, webcam_interface):
        while True:  # Continuous loop for real-time feed
            frame = webcam_interface.get_frame()
            processed_data = self.preprocess_frame(frame)
            self.receive_visual_input(processed_data, neuron_type='Simple_cell')

    def get_processed_data(self):
        # This method can be customized to your needs. For now, it returns a list of states from 'Simple_cell' neurons.
        return [neuron.get_state() for neuron in self.neurons['Simple_cell']]

    def preprocess_frame(self, frame):
        """Process and interpret raw frames."""
        # For demonstration, convert the frame to grayscale as a basic preprocessing step.
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return grayscale_frame

    def reset_all_neurons(self):
        for neuron_type in self.neurons:
            for neuron in self.neurons[neuron_type]:
                neuron.reset()

    def get_activity(self, neuron_type):
        """Retrieve activity levels of specified neuron type."""
        return [neuron.get_state() for neuron in self.neurons[neuron_type]]


if __name__ == "__main__":
    visual_cortex = VisualCortex(dispatcher, number_of_neurons=100)
    webcam = WebcamInterface()
    try:
        visual_cortex.receive_realtime_input(webcam)
    except KeyboardInterrupt:
        webcam.release()
        cv2.destroyAllWindows()
