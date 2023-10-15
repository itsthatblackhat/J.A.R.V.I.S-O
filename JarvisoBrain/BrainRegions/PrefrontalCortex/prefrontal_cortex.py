import numpy as np
from JarvisoBrain.BrainRoot.event_manager import Event, EventType
from JarvisoBrain.Neurons.MotorNeurons.motor_neurons import MotorNeuron
import sqlite3

class PrefrontalCortex:
    def __init__(self, sensory_neurons, motor_neurons, interneurons, dispatcher, database_path="JarvisoBrain/NeuralDatabase/mainbrain.db"):
        self.sensory_neurons = sensory_neurons
        self.motor_neurons = motor_neurons
        self.interneurons = interneurons
        self.dispatcher = dispatcher
        self.activity_log = []
        self.database_path = database_path

    def process_input(self, event: Event):
        if event.event_type == EventType.SENSORY_INPUT:
            self.process_sensory_input(event.data)
        elif event.event_type == EventType.FEEDBACK:
            self.receive_feedback(event.data)
        # ... handle other event types as needed

    def process_sensory_input(self, input_data):
        for neuron in self.sensory_neurons:
            neuron.receive_input(input_data)

        self.execute_decision_making()

    def execute_decision_making(self):
        historical_data = self.retrieve_historical_data()
        avg_activity = np.mean([neuron.get_activity() for neuron in self.sensory_neurons])
        threshold = 0.7

        if avg_activity > 0.5 and historical_data["some_metric"] > threshold:
            decision = 'Decision_A'
        else:
            decision = 'Decision_B'

        self.plan_and_execute_task(decision)

    def plan_and_execute_task(self, decision):
        if decision == 'Decision_A':
            for motor_neuron in self.motor_neurons:
                if motor_neuron.neuron_type == 'alpha':
                    motor_neuron.receive_input(50, current_time=0)
        elif decision == 'Decision_B':
            # Some other logic
            pass

        self.log_activity()

    def retrieve_historical_data(self):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT some_metric FROM some_table ORDER BY timestamp DESC LIMIT 1")
        data = cursor.fetchone()
        conn.close()
        if data:
            return {"some_metric": data[0]}
        return {"some_metric": 0.6}

    def log_activity(self):
        current_activity = [neuron.get_activity() for neuron in self.sensory_neurons]
        self.activity_log.append(current_activity)

        # Store the activity into the database as well
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activity_log (activity) VALUES (?)", (str(current_activity),))
        conn.commit()
        conn.close()

    def receive_feedback(self, feedback_data):
        # Logic to process feedback, maybe adjust weights or relationships in the cortex based on feedback
        pass

    # ... Additional methods for the PrefrontalCortex

