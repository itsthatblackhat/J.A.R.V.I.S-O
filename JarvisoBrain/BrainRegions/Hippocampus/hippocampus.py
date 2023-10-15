import sqlite3
from JarvisoBrain.Neurons.SensoryNeurons.sensory_neurons import SensoryNeuron
from JarvisoBrain.Neurons.Interneurons.interneurons import Interneuron
from JarvisoBrain.Synapses.ExcitatorySynapses.glutamatergic_synapse import GlutamatergicSynapse
from JarvisoBrain.Synapses.InhibitorySynapses.gabaergic_synapse import GABAergicSynapse

class DatabaseInterface:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def write_data(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, list(data.values()))
        self.connection.commit()

    def read_data(self, table_name, conditions=None):
        sql = f"SELECT * FROM {table_name}"
        if conditions:
            sql += " WHERE " + " AND ".join([f"{k} = ?" for k in conditions.keys()])
            return self.cursor.execute(sql, list(conditions.values())).fetchall()
        return self.cursor.execute(sql).fetchall()

    def close(self):
        self.connection.close()

class Hippocampus:
    def __init__(self, db_path):
        self.db_interface = DatabaseInterface(db_path)
        self.sensory_neurons = [SensoryNeuron() for _ in range(50)]
        self.interneurons = [Interneuron() for _ in range(100)]
        self.synapses = []
        self.memory_bank = {}  # This is an in-memory cache. Actual persistent storage would be in the database.

    def create_neural_connections(self):
        for s_neuron in self.sensory_neurons:
            for i_neuron in self.interneurons:
                synapse = GlutamatergicSynapse(s_neuron, i_neuron)
                self.synapses.append(synapse)

    def store_memory(self, memory_data):
        self.db_interface.write_data('memories', memory_data)

    def retrieve_memory(self, conditions):
        return self.db_interface.read_data('memories', conditions)

    def process_input(self, input_data):
        for neuron, datum in zip(self.sensory_neurons, input_data):
            neuron.stimulate(datum)

        if self.is_recognized_pattern(input_data):
            self.store_memory({'memory_label': 'recognized_pattern', 'content': str(input_data)})

    def is_recognized_pattern(self, input_data):
        return sum(input_data) > len(input_data) / 2

    def connect_to_other_regions(self, other_region):
        pass

    def reset(self):
        for neuron in self.sensory_neurons + self.interneurons:
            neuron.reset()
        self.memory_bank = {}

    def close(self):
        self.db_interface.close()

if __name__ == "__main__":
    hippocampus = Hippocampus('path_to_mainbrain.db')
    hippocampus.process_input([1, 2, 3, 4, 5])
    memories = hippocampus.retrieve_memory({'memory_label': 'recognized_pattern'})
    print(memories)
    hippocampus.close()
