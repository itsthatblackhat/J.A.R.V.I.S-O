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
 
 


 
### Basal Ganglia (`basalganglia.py`)

#### **Class `BasalGangliaNeuron`**:

- Represents individual neurons within the basal ganglia.
  
- **Attributes**:
  - **neuron_type**: Type of neuron (e.g., 'striatal_neuron'). Different types could represent different parts of the basal ganglia.
  - **state**: Current activation state of the neuron.
  
- **Functions**:
  - **activate**: Activates the neuron based on a stimulus.
  - **reset**: Resets the neuron's state.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `BasalGanglia`**:

- Represents the basal ganglia containing multiple basal ganglia neurons.
  
- **Attributes**:
  - **neurons**: List of basal ganglia neurons.
  - **conn**: Connection object for the SQLite database.
  - **cursor**: Cursor object for executing database queries.
  
- **Functions**:
  - **_connect_to_database**: Establishes a connection to the SQLite database and sets up the table for basal ganglia neurons if it doesn't exist.
  - **_close_database**: Closes the database connection.
  - **process_input**: Activates neurons based on input data and logs their states to the database.
  - **regulate_movement**: Propagates signals from the basal ganglia neurons to a motor system.
  - **process_learning**: Placeholder for handling procedural learning and habit formation.
  - **reset_all_neurons**: Resets all neurons' states and deletes their records from the database.
  - **get_activity**: Returns the current state of all neurons.
  - **retrieve_neuron_data_from_db**: Fetches neuron data from the database.

The `if __name__ == "__main__":` section provides a simple example of how the `BasalGanglia` class can be instantiated, how it processes inputs, and how to retrieve the activity of the basal ganglia.
 
 
  
### Brainstem (`brainstem.py`)

#### **Class `BrainstemNeuron`**:

- Represents individual neurons within the brainstem.

- **Attributes**:
  - **neuron_type**: Type of neuron, which could be 'autonomic_neuron', 'relay_neuron', etc.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus. Contains logic for neuron activation, threshold checks, etc.
  - **reset**: Resets the neuron's state to its default.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `Brainstem`**:

- Represents the brainstem containing multiple brainstem neurons.

- **Attributes**:
  - **neurons**: List of brainstem neurons.

- **Functions**:
  - **process_input**: Processes input data and activates corresponding neurons.
  - **integrate_information**: Integrates information with other brain regions.
  - **reset_all_neurons**: Resets the state of all neurons in the brainstem.
  - **get_activity**: Retrieves the current activity (state) of all neurons.

The `if __name__ == "__main__":` section provides a simple example of how the `Brainstem` class can be instantiated, how it processes inputs, and how to retrieve the activity of the brainstem.





### Cerebellum (`cerebellum.py`)

#### **Class `CerebellarNeuron`**:

- Represents individual neurons within the cerebellum.

- **Attributes**:
  - **neuron_type**: Type of neuron. Examples include 'Purkinje cell', 'Granule cell', etc.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus. Contains placeholder for additional logic for neuron activation, threshold checks, etc.
  - **reset**: Resets the neuron's state to its default.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `Cerebellum`**:

- Represents the cerebellum containing multiple cerebellar neurons.

- **Attributes**:
  - **neurons**: List of cerebellar neurons, specifically 'Purkinje cells' in this implementation.

- **Functions**:
  - **receive_input**: Processes the input and activates corresponding neurons.
  - **send_output**: Propagates the signals to motor neurons.
  - **reset_all_neurons**: Resets the state of all neurons in the cerebellum.
  - **get_activity**: Retrieves the current activity (state) of all neurons.

The `if __name__ == "__main__":` section provides a simple example of how the `Cerebellum` class can be instantiated, how it processes inputs, and how to retrieve the activity of the cerebellum.





### Hippocampus (`hippocampus.py`)

#### **Class `DatabaseInterface`**:

- Provides methods for database interactions.

- **Attributes**:
  - **connection**: SQLite3 database connection object.
  - **cursor**: Cursor object for executing database operations.

- **Functions**:
  - **write_data**: Writes data to the specified table in the database.
  - **read_data**: Reads data from the specified table with optional conditions.
  - **close**: Closes the database connection.

#### **Class `Hippocampus`**:

- Represents the hippocampus with its neurons and memory storage capabilities.

- **Attributes**:
  - **db_interface**: An instance of `DatabaseInterface` to handle database operations.
  - **sensory_neurons**: List of sensory neurons in the hippocampus.
  - **interneurons**: List of interneurons in the hippocampus.
  - **synapses**: List of synapses connecting sensory neurons to interneurons.
  - **memory_bank**: An in-memory cache for storing memory data. (Note: Actual persistent storage is in the database.)

- **Functions**:
  - **create_neural_connections**: Creates connections between sensory neurons and interneurons using glutamatergic synapses.
  - **store_memory**: Stores memory data in the database.
  - **retrieve_memory**: Retrieves memory data from the database based on conditions.
  - **process_input**: Processes input data, stimulates sensory neurons, and stores recognized patterns.
  - **is_recognized_pattern**: Determines if the given input data represents a recognized pattern.
  - **connect_to_other_regions**: Placeholder for connecting the hippocampus to other brain regions.
  - **reset**: Resets the state of all neurons and clears the memory bank.
  - **close**: Closes the database interface.

The `if __name__ == "__main__":` section provides a simple example of how the `Hippocampus` class can be instantiated, how it processes inputs, and how to retrieve stored memories.




### Hypothalamus (`hypothalamus.py`)

#### **Class `HypothalamicNeuron`**:

- Represents individual neurons within the hypothalamus.

- **Attributes**:
  - **neuron_type**: Type of the neuron, which can indicate its function within the hypothalamus, such as 'thermoregulatory_neuron' or 'circadian_neuron'.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus.
  - **reset**: Resets the neuron's state.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `Hypothalamus`**:

- Represents the hypothalamus with its distinct neurons.

- **Attributes**:
  - **neurons**: Dictionary containing lists of various neuron types. Currently, it has 'thermoregulatory_neuron' and 'circadian_neuron'.

- **Functions**:
  - **receive_input**: Processes input for specific neuron types and activates the corresponding neurons.
  - **reset_all_neurons**: Resets the state of all neurons in the hypothalamus.
  - **get_activity**: Retrieves activity levels of a specified neuron type.







### Prefrontal Cortex (`prefrontal_cortex.py`)

#### **Class `PrefrontalNeuron`**:

- Represents individual neurons within the prefrontal cortex.

- **Attributes**:
  - **neuron_type**: Type of the neuron, which can be 'sensory', 'motor', or 'interneuron'.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus.
  - **reset**: Resets the neuron's state.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `PrefrontalCortex`**:

- Represents the prefrontal cortex, responsible for processing sensory input, executing decision-making, and handling feedback.

- **Attributes**:
  - **sensory_neurons**: List of sensory neurons.
  - **motor_neurons**: List of motor neurons.
  - **interneurons**: List of interneurons.
  - **dispatcher**: An event dispatcher for handling events.
  - **activity_log**: List that logs neural activity.
  - **database_path**: Path to the SQLite database for storing and retrieving historical data.

- **Functions**:
  - **process_input**: Processes input events which can be sensory inputs or feedback.
  - **process_sensory_input**: Processes sensory input by activating sensory neurons.
  - **execute_decision_making**: Based on sensory neuron activity and historical data, it makes a decision.
  - **plan_and_execute_task**: Depending on the decision made, it activates specific motor neurons to execute tasks.
  - **retrieve_historical_data**: Fetches historical data from the SQLite database.
  - **log_activity**: Logs the current activity of sensory neurons and also stores this activity in the SQLite database.
  - **receive_feedback**: Placeholder function to handle feedback data and potentially adjust weights or relationships based on feedback.





### Somatosensory Cortex (`somatosensory_cortex.py`)

#### **Class `SomatoNeuron`**:

- Represents individual neurons within the somatosensory cortex.

- **Attributes**:
  - **neuron_type**: Type of the neuron, which can indicate its function, such as 'touch' or 'temperature'.
  - **sensory_region**: Region of the sensory neuron, such as 'hand', 'foot', or 'face'.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given sensory input, region, and intensity.
  - **reset**: Resets the neuron's state to its default.
  - **get_state**: Returns the current state of the neuron.

#### **Class `SomatosensoryCortex`**:

- Represents the somatosensory cortex with its distinct neurons.

- **Attributes**:
  - **neurons**: Dictionary containing lists of various neuron types grouped by sensory region (e.g., 'hand', 'foot').
  - **db_path**: Path to the SQLite database for storing and retrieving historical data.
  - **dispatcher**: An event dispatcher for handling events.

- **Functions**:
  - **process_sensory_input**: Processes sensory input by distributing the data to neurons based on their type, region, and intensity.
  - **get_activity_map**: Returns the current activity state of all neurons in the cortex, grouped by region.
  - **reset_all_neurons**: Resets the state of all neurons in the somatosensory cortex.
  - **handle_event**: Processes events of type `NEW_SENSORY_INPUT` by processing the sensory data.
  - **register_to_dispatcher**: Registers the somatosensory cortex to listen for certain events from the event dispatcher.

The `if __name__ == "__main__":` section provides a demonstration of how the `SomatosensoryCortex` class can be instantiated, how it processes inputs, and how to retrieve the activity of the cortex.





### Thalamus (`thalamus.py`)

#### **Class `ThalamicNeuron`**:

- Represents individual neurons within the thalamus.

- **Attributes**:
  - **neuron_type**: Type of the neuron, which can indicate its function, such as 'relay_neuron' or 'interneuron'.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus.
  - **reset**: Resets the neuron's state to its default.
  - **get_state**: Returns the current state of the neuron.
  - **propagate_signal**: Propagates the neuron's signal to connected neurons.

#### **Class `Thalamus`**:

- Represents the thalamus with its distinct neurons.

- **Attributes**:
  - **neurons**: List containing instances of `ThalamicNeuron`.

- **Functions**:
  - **receive_input**: Processes input data by activating the corresponding neurons.
  - **relay_to_cortex**: Propagates the signals from the thalamic neurons to the cortical neurons.
  - **reset_all_neurons**: Resets the state of all neurons in the thalamus.
  - **get_activity**: Retrieves the current activity state of all neurons in the thalamus.

The `if __name__ == "__main__":` section provides a demonstration of how the `Thalamus` class can be instantiated, how it processes inputs, and how to retrieve the activity of the thalamus.




### Visual Cortex (`visual_cortex.py`)

#### **Dependencies**:
- **cv2**: OpenCV library used for computer vision tasks.
- **tensorflow**: TensorFlow library used for machine learning.
- **numpy**: Used for numerical operations.

#### **Class `WebcamInterface`**:

- Provides an interface to access the computer's webcam.

- **Attributes**:
  - **cap**: Video capture object from OpenCV.

- **Functions**:
  - **get_frame**: Retrieves the current frame from the webcam.
  - **release**: Releases the webcam resource.

#### **Class `VisualNeuron`**:

- Represents individual neurons within the visual cortex.

- **Attributes**:
  - **neuron_type**: Type of the neuron.
  - **state**: Current activation state of the neuron.

- **Functions**:
  - **activate**: Activates the neuron based on a given stimulus.
  - **reset**: Resets the neuron's state to its default.
  - **get_state**: Returns the current state of the neuron.

#### **Class `VisualCortex`**:

- Represents the visual cortex with its distinct neurons.

- **Attributes**:
  - **dispatcher**: An event dispatcher for handling events.
  - **model**: A TensorFlow model for object detection.
  - **neurons**: Dictionary containing lists of neurons by type, such as 'Simple_cell' or 'Complex_cell'.
  - **motor_neurons**: Dictionary containing motor neurons, such as the 'webcam'.

- **Functions**:
  - **detect_and_annotate_objects**: Detects objects in a given frame using the pretrained model and annotates them.
  - **receive_visual_input**: Processes visual data and activates the corresponding neurons based on the prediction from the model.
  - **receive_realtime_input**: Continuously captures frames from the webcam, detects and annotates objects, and processes the visual data.
  - **get_processed_data**: Returns the processed data from the 'Simple_cell' neurons.
  - **preprocess_frame**: Converts a frame to grayscale, resizes, and normalizes it.
  - **reset_all_neurons**: Resets the state of all neurons in the visual cortex.
  - **get_activity**: Retrieves the current activity state of the neurons based on their type.

The `if __name__ == "__main__":` section provides a demonstration of how the `VisualCortex` class can be instantiated, how it processes real-time inputs from the webcam, and how to handle interruptions.




















----------------------------------------------------------------------------

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

