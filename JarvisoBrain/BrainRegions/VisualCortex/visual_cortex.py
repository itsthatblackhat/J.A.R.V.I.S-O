import cv2
import tensorflow as tf
import numpy as np
from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.Neurons.MotorNeurons.motor_neurons import MotorNeuron

dispatcher = EventDispatcher()


class WebcamInterface:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()


class VisualNeuron:
    def __init__(self, neuron_type, initial_state=0):
        self.neuron_type = neuron_type
        self.state = initial_state

    def activate(self, stimulus):
        self.state += stimulus

    def reset(self):
        self.state = 0

    def get_state(self):
        return self.state


class VisualCortex:
    def __init__(self, dispatcher, number_of_neurons=100):
        self.dispatcher = dispatcher
        self.model = tf.keras.models.load_model('path_to_pretrained_model')
        self.neurons = {
            'Simple_cell': [VisualNeuron(neuron_type='Simple_cell') for _ in range(number_of_neurons)],
            'Complex_cell': [VisualNeuron(neuron_type='Complex_cell') for _ in range(number_of_neurons)],
        }
        self.motor_neurons = {
            'webcam': MotorNeuron(neuron_id=1, neuron_type='webcam')
        }

    def detect_and_annotate_objects(self, frame):
        detections = self.model.predict(frame)
        for detection in detections:
            x, y, w, h = detection['bbox']
            label = detection['label']
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return frame

    def receive_visual_input(self, visual_data, neuron_type):
        prediction = self.model.predict(visual_data)
        for neuron, data in zip(self.neurons[neuron_type], prediction):
            neuron.activate(data)

            if neuron.get_state() > 50:
                self.motor_neurons['webcam'].receive_input(20, current_time=0)

        event = Event(EventType.PROCESSED_DATA_FROM_VISUAL_CORTEX, data=prediction)
        self.dispatcher.dispatch(event)

    def receive_realtime_input(self, webcam_interface):
        while True:
            frame = webcam_interface.get_frame()
            annotated_frame = self.detect_and_annotate_objects(frame)
            processed_data = self.preprocess_frame(annotated_frame)
            self.receive_visual_input(processed_data, neuron_type='Simple_cell')

    def get_processed_data(self):
        return [neuron.get_state() for neuron in self.neurons['Simple_cell']]

    def preprocess_frame(self, frame):
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(grayscale_frame, (224, 224))
        normalized_frame = resized_frame / 255.0
        return np.expand_dims(normalized_frame, axis=0)

    def reset_all_neurons(self):
        for neuron_type in self.neurons:
            for neuron in self.neurons[neuron_type]:
                neuron.reset()

    def get_activity(self, neuron_type):
        return [neuron.get_state() for neuron in self.neurons[neuron_type]]


if __name__ == "__main__":
    visual_cortex = VisualCortex(dispatcher)
    webcam = WebcamInterface()
    try:
        visual_cortex.receive_realtime_input(webcam)
    except KeyboardInterrupt:
        webcam.release()
        cv2.destroyAllWindows()
