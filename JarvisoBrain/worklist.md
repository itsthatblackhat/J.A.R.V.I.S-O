# JarvisoBrain Development Notes

## Table of Contents

- [Introduction](#introduction)
- [Root Directory Files](#root-directory-files)
  - [main_brain.py](#main_brainpy)
- [Brain Regions](#brain-regions)
  - [Auditory Cortex](#auditory-cortex)
  - [Basal Ganglia](#basal-ganglia)
  - [Brainstem](#brainstem)
  - [Cerebellum](#cerebellum)
  - [Hippocampus](#hippocampus)
  - [Hypothalamus](#hypothalamus)
  - [Prefrontal Cortex](#prefrontal-cortex)
  - [Somatosensory Cortex](#somatosensory-cortex)
  - [Thalamus](#thalamus)
  - [Visual Cortex](#visual-cortex)
- [Brain Root](#brain-root)
- [Neural Database](#neural-database)
- [Neuromodulatory Systems](#neuromodulatory-systems)
- [Neurons](#neurons)
  - [Interneurons](#interneurons)
  - [Motor Neurons](#motor-neurons)
  - [Sensory Neurons](#sensory-neurons)
- [Synapses](#synapses)
  - [Excitatory Synapses](#excitatory-synapses)
  - [Inhibitory Synapses](#inhibitory-synapses)
  - [Neuromodulatory Synapses](#neuromodulatory-synapses)
- [Utilities (Utils)](#utilities-utils)

## Introduction

Details about the main purpose and overview of the JarvisoBrain project.

# Root Directory Files

## main_brain.py

The `main_brain.py` file serves as the central orchestrator for the JarvisoBrain project.

#### Initialization (`__init__`):

- **Event Dispatcher**: Manages and dispatches various event types within the brain.
- **Sensory Neurons**: Initialized with a list of sensory neurons.
- **Motor Neurons**: Initialized with a list of motor neurons.
- **Interneurons**: Handle communication between sensory and motor neurons.
- **Brain Regions (Cortices)**:
  - **Auditory Cortex**: Processes auditory inputs.
  - **Visual Cortex**: Processes visual inputs.
  - **Prefrontal Cortex**: Crucial for decision-making and more complex cognitive processes.
  - **Somatosensory Cortex**: Processes sensory inputs related to touch and body position.

#### Receiving Input (`receive_input`):

- Creates a new event based on the input type and data received.
- Dispatches the event to the relevant cortex.
- Logs the event to the database.

#### Processing (`process`):

- Collects and processes sensory data from various cortices.
- Executes decision-making processes in the Prefrontal Cortex.
- Translates the decisions to motor commands.

#### Collecting Sensory Data (`collect_sensory_data`):

- Gathers processed data from the Auditory, Visual, and Somatosensory Cortices.
- Combines this data into a single dictionary.

#### Executing Actions (`execute_actions`):

- Activates specific motor neurons based on the processed decisions.

The `if __name__ == "__main__":` section provides a simple example of how the JarvisoBrain class can be instantiated and utilized.

# Brain Regions

### Auditory Cortex (`auditory_cortex.py`)

#### **Class `AuditoryNeuron`**:
- Represents individual auditory neurons within the auditory cortex.
- **Attributes**:
  - **neuron_type**: Type of neuron (default is 'primary_neuron').
  - **state**: Current activation state of the neuron (default is 0).
- **Functions**:
  - **activate**: Activates the neuron based on an auditory signal input.
  - **reset**: Resets the neuron's state to 0.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `AuditoryCortex`**:
- Represents the auditory cortex containing multiple auditory neurons.
- **Attributes**:
  - **neurons**: List of auditory neurons.
  - **dispatcher**: Event dispatcher for managing brain events.
  - **db_path**: Path to the database.
  - **model**: TensorFlow model used for processing auditory data.
- **Functions**:
  - **capture_audio**: Captures audio data for a specified duration using `sounddevice`.
  - **preprocess_audio**: Preprocesses raw audio data (averages stereo channels).
  - **process_audio_input**: Processes auditory inputs using the pre-trained model, activates neurons based on predictions, and sends the processed data to memory storage.
  - **reset_all_neurons**: Resets all the neurons in the auditory cortex.
  - **get_processed_data**: Retrieves the processed auditory data from all neurons.

The `if __name__ == "__main__":` section provides a simple example of how the `AuditoryCortex` class can be instantiated and utilized.


# Brain Root

Insights about the core architecture and functionalities of the JarvisoBrain project.

# Neural Database

Information about the database structures and CRUD operations.

# Neuromodulatory Systems

Details about the neuromodulatory systems and their functionalities.

# Neurons

Analysis of the different types of neurons and their implementation.

# Synapses

Details about the synapses, their types, and functionalities.

# Utilities (Utils)

Insights about the utility modules and their roles in the project.

