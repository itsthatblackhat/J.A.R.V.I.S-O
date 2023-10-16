# JarvisoBrain: A Computational Model of the Human Brain

The JarvisoBrain project is an ambitious endeavor to model the human brain's various components and functionalities digitally. The architecture encompasses different brain regions, neurons, event management, memory storage, and neuromodulatory systems. This README provides a comprehensive overview of its structure, functionalities, and interactions.

## Table of Contents
- [JarvisoBrain](#jarvisobrain)
  - [main_brain.py](#main_brain.py)
  - [BrainRegions](#brainregions)
    - [AuditoryCortex](#auditorycortex)
      - [auditory_cortex.py](#auditory_cortex.py)
    - [BasalGanglia](#basalganglia)
      - [basalganglia.py](#basalganglia.py)
    - [Brainstem](#brainstem)
      - [brainstem.py](#brainstem.py)
    - [Cerebellum](#cerebellum)
      - [cerebellum.py](#cerebellum.py)
    - [Hippocampus](#hippocampus)
      - [hippocampus.py](#hippocampus.py)
    - [Hypothalamus](#hypothalamus)
      - [hypothalamus.py](#hypothalamus.py)
    - [PrefrontalCortex](#prefrontalcortex)
      - [prefrontal_cortex.py](#prefrontal_cortex.py)
    - [SomatosensoryCortex](#somatosensorycortex)
      - [somatosensory_cortex.py](#somatosensory_cortex.py)
    - [Thalamus](#thalamus)
      - [thalamus.py](#thalamus.py)
    - [VisualCortex](#visualcortex)
      - [visual_cortex.py](#visual_cortex.py)
        
  - [BrainRoot](#brainroot)
    - [brain_message.py](#brain_message.py)
    - [controller.py](#controller.py)
    - [event_manager.py](#event_manager.py)
    - [memory_manager.py](#memory_manager.py)
  - [NeuralDatabase](#neuraldatabase)
    - [database.py](#database.py)
  - [NeuromodulatorySystems](#neuromodulatorysystems)
    - [CholinergicSystem](#cholinergicsystem)
      - [cholinergic_system.py](#cholinergic_system.py)
    - [DopamineSystem](#dopaminesystem)
      - [dopamine_system.py](#dopamine_system.py)
    - [NeuromodulatorySystem](#neuromodulatorysystem)
      - [acetylcholine_system.py](#acetylcholine_system.py)
      - [endocannabinoid_system.py](#endocannabinoid_system.py)
      - [norepinephrine_system.py](#norepinephrine_system.py)
    - [NoradrenergicSystem](#noradrenergicsystem)
      - [noradrenergic_system.py](#noradrenergic_system.py)
    - [SerotoninSystem](#serotoninsystem)
      - [serotonin_system.py](#serotonin_system.py)
  - [Neurons](#neurons)
    - [Interneurons](#interneurons)
      - [interneurons.py](#interneurons.py)
    - [MotorNeurons](#motorneurons)
      - [motor_neurons.py](#motor_neurons.py)
    - [SensoryNeurons](#sensoryneurons)
      - [sensory_neurons.py](#sensory_neurons.py)
  - [Synapses](#synapses)
    - [ExcitatorySynapses](#excitatorysynapses)
      - [dopaminergic_synapse.py](#dopaminergic_synapse.py)
      - [excitatory_synapses.py](#excitatory_synapses.py)
      - [glutamatergic_synapse.py](#glutamatergic_synapse.py)
    - [InhibitorySynapses](#inhibitorysynapses)
      - [cholinergic_synapse.py](#cholinergic_synapse.py)
      - [gabaergic_synapse.py](#gabaergic_synapse.py)
      - [glycinergic_synapse.py](#glycinergic_synapse.py)
      - [inhibitory_synapses.py](#inhibitory_synapses.py)
    - [NeuromodulatorySynapses](#neuromodulatorysynapses)
      - [endocannabinoid_synapse.py](#endocannabinoid_synapse.py)
      - [neuromodulatory_synapses.py](#neuromodulatory_synapses.py)
      - [noradrenergic_synapse.py](#noradrenergic_synapse.py)
      - [serotonergic_synapse.py](#serotonergic_synapse.py)
  - [Utilities](#utilities)
    - [data_loader.py](#data_loader.py)
    - [feedback_processor.py](#feedback_processor.py)
    - [signal_processing.py](#signal_processing.py)
    - [visualization.py](#visualization.py)

## BrainRegions

### AuditoryCortex

#### File Path:
`BrainRegions/AuditoryCortex/auditory_cortex.py`

#### Overview:
The `AuditoryCortex` module simulates the auditory cortex of the brain, responsible for processing auditory inputs from sources like the ears and dispatching processed data for further action or storage.

#### Classes:

1. **AuditoryNeuron**:
    - **Purpose**: Represents individual neurons in the auditory cortex that process and propagate auditory signals.
    - **Attributes**:
        - `neuron_type` (string): Defines the type of the neuron (default is 'primary_neuron').
        - `state` (float): Represents the current activation state or level of the neuron.
    - **Methods**:
        - `activate(self, auditory_signal)`: Increases the neuron's state based on an incoming auditory signal.
        - `reset(self)`: Resets the neuron's activation state to its default.
        - `get_state(self)`: Returns the current activation state of the neuron.
        - `propagate_signal(self, connected_neurons)`: Sends the neuron's activation state to other connected neurons.

2. **AuditoryCortex**:
    - **Purpose**: Manages the collection of auditory neurons and orchestrates the processing of auditory signals.
    - **Attributes**:
        - `neurons` (list): Contains instances of AuditoryNeuron.
        - `dispatcher` (EventDispatcher): Manages the flow of events within the system.
        - `db_path` (string): Provides the path to the SQLite database for storage and retrieval of data.
        - `model` (TensorFlow model): A pre-trained model to predict or analyze auditory data.
    - **Methods**:
        - `capture_audio(self, duration)`: Uses the sounddevice library to record audio for the specified duration and returns it.
        - `preprocess_audio(self, audio)`: Converts stereo audio to mono by averaging and returns the processed audio.
        - `process_audio_input(self, event)`: Extracts audio data from an event, predicts using the model, activates neurons based on predictions, and dispatches a new event to store the processed data in the database.
        - `reset_all_neurons(self)`: Resets the activation state of all neurons in the auditory cortex to their defaults.

#### Database Interaction:
The `AuditoryCortex` interacts with an SQLite database, whose path is specified by the `db_path` attribute. The primary purpose of this interaction is to store processed auditory data for later retrieval and analysis. This is facilitated by the `BrainMessage` class and its associated attributes and methods, which package the data and its associated metadata for storage. The `process_audio_input` method in the `AuditoryCortex` class creates a `BrainMessage` instance and dispatches an event to store the data in the database.

#### Main Execution:
When executed as the main script, this module captures a 5-second audio clip, preprocesses the audio, activates neurons based on the preprocessed audio, and then dispatches an event for further action, such as storing the processed data in the database.




### BasalGanglia

#### File Path:
`BrainRegions/BasalGanglia/basalganglia.py`

#### Overview:
The `BasalGanglia` module aims to model the basal ganglia's functionality in the brain. This region plays a vital role in decision making, motor control, and learning. It integrates sensory inputs and cognitive instructions to produce motor outputs.

#### Classes:

1. **BasalNeuron**:
    - **Purpose**: Represents individual neurons in the basal ganglia responsible for processing and propagating signals related to motor control and decision making.
    - **Attributes**:
        - `neuron_type` (string): Defines the neuron type, can be 'D1' or 'D2'.
        - `state` (float): Represents the current activation state of the neuron.
    - **Methods**:
        - `activate(self, signal)`: Modifies the neuron's state based on an incoming signal.
        - `reset(self)`: Resets the neuron's activation state to its default.
        - `get_state(self)`: Returns the current activation state of the neuron.

2. **BasalGanglia**:
    - **Purpose**: Manages the collection of basal neurons and facilitates the processing of signals related to decision making and motor control.
    - **Attributes**:
        - `neurons` (list): Contains instances of BasalNeuron.
        - `dispatcher` (EventDispatcher): Manages the flow of events within the system.
        - `db_path` (string): Provides the path to the SQLite database for storage and retrieval of data.
    - **Methods**:
        - `process_signal(self, event)`: Extracts signal data from an event, processes it, activates the appropriate neurons, and dispatches an event for subsequent actions or storage.
        - `reset_all_neurons(self)`: Resets all neurons in the basal ganglia to their default states.

#### Database Interaction:
The `BasalGanglia` interacts with the SQLite database specified by the `db_path` attribute. The primary interaction involves storing processed signals and the resulting neuron activation states for future analysis. The `process_signal` method is responsible for creating a `BrainMessage` instance and dispatching it for database storage.

#### Main Execution:
If executed as the main script, this module will simulate a signal's processing, activate the appropriate neurons, and dispatch an event to handle the processed data, such as storing it in the database.




### Brainstem

#### File Path:
`BrainRegions/Brainstem/brainstem.py`

#### Overview:
The `Brainstem` module emulates the brainstem's functions, a critical component of the central nervous system connecting the cerebrum with the spinal cord. It plays pivotal roles in autonomic functions, relay of sensory information, and coordination of eye movements.

#### Classes:

1. **BrainstemNeuron**:
    - **Purpose**: Represents individual neurons within the brainstem, responsible for processing sensory information and conducting it to various parts of the brain.
    - **Attributes**:
        - `neuron_id` (int): Unique identifier for each neuron.
        - `activation_threshold` (float): The threshold at which the neuron becomes active.
        - `current_value` (float): Represents the neuron's current value or state.
    - **Methods**:
        - `receive_signal(self, signal)`: Takes in a sensory signal, processes it, and modifies the neuron's current value.
        - `is_active(self)`: Determines if the neuron is active based on its current value.

2. **BrainstemController**:
    - **Purpose**: Oversees the brainstem neurons' collection and manages their interactions with sensory inputs and other brain regions.
    - **Attributes**:
        - `neurons` (list): Contains instances of BrainstemNeuron.
        - `sensory_queue` (queue): A queue that holds incoming sensory signals for processing.
        - `dispatcher` (EventDispatcher): Manages the event-driven architecture of the system.
        - `db_path` (string): Path to the SQLite database for data storage and retrieval.
    - **Methods**:
        - `process_sensory_queue(self)`: Continuously processes sensory signals from the queue and dispatches appropriate responses.
        - `reset_all_neurons(self)`: Resets all neurons in the brainstem to their default states.

#### Database Interaction:
The `Brainstem` module interacts with the SQLite database denoted by the `db_path` attribute. Its primary role is to log sensory signals, neuron activation states, and relayed signals for further processing in other brain regions. The `process_sensory_queue` method generates `BrainMessage` instances and uses the event dispatcher to facilitate this interaction.

#### Main Execution:
When executed as the main script, this module will demonstrate the processing of a sensory signal, activating relevant neurons, and dispatching events for subsequent tasks like database storage or further signal relay to other brain regions.





### Cerebellum

#### File Path:
`BrainRegions/Cerebellum/cerebellum.py`

#### Overview:
The `Cerebellum` module is designed to emulate the cerebellum's functions, a region responsible for motor control, coordination, precision, and accurate timing. It receives input from sensory systems and other parts of the brain and integrates these inputs to fine-tune motor activity.

#### Classes:

1. **CerebellarNeuron**:
    - **Purpose**: Represents individual neurons within the cerebellum, crucial for processing sensory and motor information.
    - **Attributes**:
        - `neuron_id` (int): Unique identifier for each neuron.
        - `activation_threshold` (float): The threshold at which the neuron becomes active.
        - `current_value` (float): Current state or value of the neuron.
    - **Methods**:
        - `receive_signal(self, signal)`: Processes incoming signals and updates the neuron's current value.
        - `is_active(self)`: Determines if the neuron is active based on its current value and threshold.

2. **CerebellarModule**:
    - **Purpose**: Manages a collection of cerebellar neurons, handling their interactions with sensory and motor inputs.
    - **Attributes**:
        - `neurons` (list): Contains instances of CerebellarNeuron.
        - `motor_queue` (queue): A queue that holds incoming motor signals for processing.
        - `dispatcher` (EventDispatcher): Manages the event-driven interactions of the system.
        - `db_path` (string): Path to the SQLite database for data storage and retrieval.
    - **Methods**:
        - `process_motor_queue(self)`: Processes motor signals from the queue and refines motor commands.
        - `reset_all_neurons(self)`: Resets all neurons in the cerebellum to their default states.

#### Database Interaction:
The `Cerebellum` module interacts with the SQLite database through the `db_path` attribute. It logs sensory inputs, neuron activation states, and refined motor commands. The `process_motor_queue` method creates `BrainMessage` instances and utilizes the event dispatcher for this database interaction.

#### Main Execution:
When run as the primary script, this module showcases the refinement of a motor command, neuron activations based on sensory inputs, and event dispatches for tasks like database storage or further signal relay to motor systems.




### Hippocampus

#### File Path:
`BrainRegions/Hippocampus/hippocampus.py`

#### Overview:
The `Hippocampus` module models the functions of the hippocampus, a critical brain region involved in the formation of new memories and connecting emotions and senses, such as smell and sound, to memories. It's pivotal for tasks like navigation, spatial orientation, and emotional responses.

#### Classes:

1. **HippocampalNeuron**:
    - **Purpose**: Represents the individual neurons within the hippocampus, playing a role in memory formation and emotional association.
    - **Attributes**:
        - `neuron_id` (int): Unique identifier for each neuron.
        - `memory_strength` (float): Represents the strength or clarity of a memory associated with this neuron.
        - `associated_emotions` (list): A list of emotions tied to the memory this neuron represents.
    - **Methods**:
        - `store_memory(self, memory, emotions)`: Stores a memory and its associated emotions in the neuron.
        - `retrieve_memory(self)`: Retrieves the memory stored in the neuron.

2. **HippocampalNetwork**:
    - **Purpose**: Manages a network of hippocampal neurons, overseeing the storage and retrieval of memories.
    - **Attributes**:
        - `neurons` (list): Contains instances of HippocampalNeuron.
        - `dispatcher` (EventDispatcher): Manages the event-driven interactions of the system.
        - `db_path` (string): Path to the SQLite database for memory storage and retrieval.
    - **Methods**:
        - `store_to_db(self, memory, emotions)`: Stores a memory and its associated emotions in the database.
        - `retrieve_from_db(self, memory_id)`: Retrieves a specific memory based on its ID from the database.

#### Database Interaction:
The `Hippocampus` interacts with the SQLite database through the `db_path` attribute. It ensures that memories, with their associated emotional context, are stored and can be retrieved efficiently. The `store_to_db` and `retrieve_from_db` methods facilitate this interaction.

#### Main Execution:
When run as the primary script, this module demonstrates the storage of a new memory with its emotional context, the activation of hippocampal neurons, and the process of memory retrieval based on specific cues or triggers.





### Hypothalamus

#### File Path:
`BrainRegions/Hypothalamus/hypothalamus.py`

#### Overview:
The `Hypothalamus` module emulates the functions of the hypothalamus, a vital region of the brain responsible for numerous vital functions, including the release of hormones, regulation of body temperature, and maintenance of daily physiological cycles.

#### Classes:

1. **HypothalamicNucleus**:
    - **Purpose**: Represents the individual nuclei within the hypothalamus, each of which has specific regulatory functions.
    - **Attributes**:
        - `nucleus_id` (int): Unique identifier for each nucleus.
        - `hormone_release` (dict): Dictates the amount of specific hormones to release.
        - `body_temp_regulation` (bool): Indicates whether this nucleus is involved in body temperature regulation.
    - **Methods**:
        - `release_hormone(self, hormone, amount)`: Commands the release of a specific amount of a given hormone.
        - `regulate_temp(self, desired_temp)`: Attempts to regulate the body's temperature to the desired value.

2. **HypothalamicControlSystem**:
    - **Purpose**: Manages the operations of various hypothalamic nuclei, ensuring the body's homeostasis.
    - **Attributes**:
        - `nuclei` (list): Contains instances of HypothalamicNucleus.
        - `dispatcher` (EventDispatcher): Manages the event-driven interactions of the system.
    - **Methods**:
        - `initiate_sleep_cycle(self)`: Triggers the beginning of a sleep cycle.
        - `initiate_wake_cycle(self)`: Triggers the end of a sleep cycle and the start of wakefulness.

#### Database Interaction:
The `Hypothalamus` doesn't directly interact with the SQLite database in its current implementation. However, its operations can influence other systems that might have database interactions, especially with respect to hormone levels and physiological responses.

#### Main Execution:
When executed as the main script, this module simulates the regulation of body temperature, the release of specific hormones, and the initiation of sleep and wake cycles.





### PrefrontalCortex

#### File Path:
`BrainRegions/PrefrontalCortex/prefrontal_cortex.py`

#### Overview:
The `PrefrontalCortex` module emulates the functionalities of the prefrontal cortex, a crucial region of the brain responsible for executive functions like decision-making, planning, and inhibition of impulses.

#### Classes:

1. **ExecutiveFunctionModule**:
    - **Purpose**: Represents the cognitive processes involved in planning, decision-making, and error monitoring.
    - **Attributes**:
        - `current_task` (str): The task currently being processed or planned.
        - `previous_tasks` (list): A list of tasks that have been executed previously.
        - `error_count` (int): Tracks the number of errors or misjudgments made.
    - **Methods**:
        - `plan_task(self, task)`: Analyzes and plans the execution of a given task.
        - `monitor_errors(self, error)`: Logs and responds to errors or misjudgments.

2. **InhibitionControlModule**:
    - **Purpose**: Manages the control of impulses and immediate reactions, ensuring thoughtful responses.
    - **Attributes**:
        - `impulses` (list): A list of impulses or immediate reactions detected.
        - `inhibited_responses` (list): Responses that have been suppressed or delayed for better judgment.
    - **Methods**:
        - `inhibit_response(self, impulse)`: Suppresses or delays a given impulse or immediate reaction.
        - `release_inhibition(self, response)`: Allows a previously inhibited response to be executed.

#### Database Interaction:
The `PrefrontalCortex` interacts with the SQLite database to log decision-making processes, planned tasks, errors, and inhibited responses. This information can be used for future analysis and to improve the decision-making process.

#### Main Execution:
When executed as the main script, this module simulates the decision-making process, planning tasks, inhibiting impulsive responses, and monitoring errors.





### SomatosensoryCortex

#### File Path:
`BrainRegions/SomatosensoryCortex/somatosensory_cortex.py`

#### Overview:
The `SomatosensoryCortex` module is designed to emulate the functionalities of the somatosensory cortex, which is primarily responsible for processing sensory inputs from various parts of the body, such as touch, temperature, and proprioception.

#### Classes:

1. **TactileProcessingUnit**:
    - **Purpose**: Processes tactile (touch) sensory inputs from the environment.
    - **Attributes**:
        - `touch_data` (list): Captures the recent tactile sensory data.
        - `processed_data` (list): Stores the processed touch sensations.
    - **Methods**:
        - `receive_touch_data(self, data)`: Accepts raw tactile data for processing.
        - `process_touch(self)`: Processes the raw touch data and classifies the sensation.

2. **TemperatureProcessingUnit**:
    - **Purpose**: Handles and processes temperature sensations from the environment.
    - **Attributes**:
        - `temp_data` (float): Captures the current temperature data.
        - `processed_temperature` (str): Stores the classified temperature sensation (e.g., "warm", "cold").
    - **Methods**:
        - `receive_temperature_data(self, data)`: Accepts raw temperature data for processing.
        - `classify_temperature(self)`: Classifies the temperature sensation based on the received data.

3. **ProprioceptionUnit**:
    - **Purpose**: Manages the sense of position and movement of different body parts relative to each other.
    - **Attributes**:
        - `position_data` (dict): Captures the positions of various body parts.
        - `movement_data` (dict): Logs movements of body parts.
    - **Methods**:
        - `receive_position_data(self, data)`: Accepts position data of body parts.
        - `log_movement(self, movement)`: Records and analyzes movements of body parts.

#### Database Interaction:
The `SomatosensoryCortex` interacts with the SQLite database to store processed sensory data, including touch sensations, temperature classifications, and proprioception data. This ensures a record of sensory experiences and can be utilized for future analysis or decision-making processes.

#### Main Execution:
When run as the primary script, this module simulates the sensory processing experience, classifying tactile, temperature, and positional sensations, and logging them appropriately.





### Thalamus

#### File Path:
`BrainRegions/Thalamus/thalamus.py`

#### Overview:
The `Thalamus` module is designed to emulate the functionalities of the thalamus, a crucial structure in the brain that acts as a relay station, transmitting sensory and motor signals to the cerebral cortex. It is also involved in the regulation of consciousness, sleep, and alertness.

#### Classes:

1. **ThalamicRelayUnit**:
    - **Purpose**: Serves as a relay unit for transmitting sensory and motor signals.
    - **Attributes**:
        - `incoming_data` (list): Captures incoming sensory and motor signals.
        - `relay_data` (list): Holds the signals to be relayed to the cerebral cortex.
    - **Methods**:
        - `receive_data(self, data)`: Accepts incoming sensory or motor data.
        - `relay_signal(self)`: Transmits the received signals to the appropriate cortical regions.

2. **SleepRegulationUnit**:
    - **Purpose**: Manages sleep-wake cycles and alertness levels.
    - **Attributes**:
        - `alertness_level` (int): Indicates the current level of alertness on a scale from 1 to 10.
        - `sleep_signals` (list): Stores signals related to sleep regulation.
    - **Methods**:
        - `adjust_alertness(self, adjustment)`: Modifies the alertness level based on the provided adjustment value.
        - `process_sleep_signal(self, signal)`: Handles signals related to sleep and wakefulness, adjusting alertness levels accordingly.

#### Database Interaction:
The `Thalamus` module communicates with the SQLite database to store and retrieve relayed sensory and motor signals. Additionally, it logs sleep-wake cycles and alertness levels, which can be instrumental in understanding the overall state of the emulated brain system.

#### Main Execution:
When the module is the primary script, it simulates the relay of sensory and motor signals, manages alertness levels, and logs sleep-wake cycle information.





very excellent, yes and I rated you good on this one also.
please proceed with the next folder with this amount of detail, we will do ALL portions like this moving forward indefinitely, remain in raw github format





### VisualCortex

#### File Path:
`BrainRegions/VisualCortex/visual_cortex.py`

#### Overview:
The `VisualCortex` module is designed to emulate the functionalities of the visual cortex, a region in the brain responsible for processing visual information from the eyes. It handles the interpretation of visual data, including color, shape, movement, and depth.

#### Classes:

1. **VisualCortex**:
    - **Purpose**: Central class that manages the processing of visual information.
    - **Attributes**:
        - `visual_data` (list): Holds incoming visual data for processing.
        - `processed_data` (list): Stores the processed visual information.
    - **Methods**:
        - `capture_image(self)`: Simulates the capture of visual data.
        - `process_image_input(self, image_data)`: Processes the visual data, breaking it down into identifiable attributes like color, shape, and motion.
        - `identify_objects(self)`: Further processes the visual data to recognize and categorize objects in the visual field.

2. **VisualNeuron**:
    - **Purpose**: Represents individual neurons within the visual cortex.
    - **Attributes**:
        - `activation_threshold` (float): The threshold value for neuron activation based on the intensity of the visual stimulus.
        - `current_signal` (float): The current signal strength received by the neuron.
    - **Methods**:
        - `receive_signal(self, signal_strength)`: Accepts incoming visual signals.
        - `fire_neuron(self)`: Determines if the neuron should activate based on the received signal strength.

#### Database Interaction:
The `VisualCortex` module interacts with the SQLite database to store processed visual information. It saves data like recognized objects, their attributes, and associated neural activations. This stored data assists in future visual recognition tasks and helps build a visual memory for the system.

#### Main Execution:
When the module is the primary script, it simulates the processing of visual data from the eyes, identifies objects, and interacts with visual neurons to determine neural responses to visual stimuli.






### Brain Message

#### File Path:
`BrainRoot/brain_message.py`

#### Overview:
The `brain_message` module is pivotal in managing messages or signals within the JarvisoBrain system. It ensures structured communication between various components, maintaining a clear and organized flow of information.

#### Classes:

1. **BrainMessage**:
    - **Purpose**: Represents a message or piece of data transmitted within the system.
    - **Attributes**:
        - `content` (dict): Holds the actual content or data of the message.
        - `message_type` (MessageType): Enumerates the type of the message (e.g., Sensory Input, Motor Command).
        - `timestamp` (datetime): Records the time the message was created.
    - **Methods**:
        - `save_to_db(self)`: Saves the message to the SQLite database.

2. **MessageType** (Enum):
    - **Purpose**: Enumerates the different types of messages that can be passed within the system.
    - **Values**:
        - `SENSORY_INPUT`: Denotes messages carrying sensory data (e.g., visual, auditory).
        - `MOTOR_COMMAND`: Denotes messages instructing motor actions or outputs.
        - `INTERNAL_PROCESSING`: Messages related to internal brain processing and computations.

3. **ProcessingDirective**:
    - **Purpose**: Offers directives or commands related to how a message or piece of data should be processed.
    - **Attributes**:
        - `directive_type` (str): Specifies the type of directive (e.g., "Process Immediately", "Store for Later").
        - `priority_level` (int): Assigns a priority to the directive, dictating its urgency or importance.
    - **Methods**:
        - `execute_directive(self)`: Executes the directive based on its type and priority.

#### Database Interaction:
This module plays a crucial role in recording messages within the SQLite database. Each `BrainMessage` can be stored for later retrieval, aiding in tasks like historical data analysis, decision-making processes, and system debugging.

#### Main Execution:
When run as the main script, the module can simulate the creation of various message types, process them based on directives, and store them in the database.






### Controller

#### File Path:
`BrainRoot/controller.py`

#### Overview:
The `controller` module serves as a central hub for orchestrating the operations of the JarvisoBrain. It manages the flow of information, processes messages, and coordinates with different brain regions and modules.

#### Classes:

1. **Controller**:
    - **Purpose**: Acts as the main orchestrator for managing and processing messages in the system.
    - **Attributes**:
        - `current_message` (BrainMessage): The current message being processed.
        - `message_queue` (list): Holds a queue of pending messages to be processed.
        - `brain_regions` (list): References to different brain regions, facilitating communication and control.
    - **Methods**:
        - `receive_message(self, message: BrainMessage)`: Accepts a new message into the system, adding it to the queue.
        - `process_next_message(self)`: Processes the next message in the queue.
        - `dispatch_message(self, message: BrainMessage)`: Sends the message to the appropriate brain region or module for processing.
        - `initialize_brain_regions(self)`: Sets up and initializes references to various brain regions.

2. **ControllerState** (Enum):
    - **Purpose**: Enumerates the different operational states the Controller can be in.
    - **Values**:
        - `IDLE`: The Controller is not actively processing any messages.
        - `PROCESSING`: The Controller is currently processing a message.
        - `WAITING`: The Controller is waiting for an external input or event.

#### Main Execution:
When run as the main script, the module initializes the Controller, simulates receiving various messages, processes these messages, and interacts with other modules and brain regions to showcase the Controller's central orchestration role.




### Event Manager

#### File Path:
`BrainRoot/event_manager.py`

#### Overview:
The `event_manager` module manages the flow of events within the JarvisoBrain system. It establishes an event-driven architecture that allows different components of the system to communicate efficiently, ensuring that events are dispatched to the appropriate listeners.

#### Classes:

1. **EventManager**:
    - **Purpose**: Manages the registration, deregistration, and dispatch of events.
    - **Attributes**:
        - `listeners` (dict): A dictionary storing registered listeners, indexed by event type.
    - **Methods**:
        - `register_listener(self, event_type: EventType, listener: Callable)`: Registers a function as a listener for a specified event type.
        - `deregister_listener(self, event_type: EventType, listener: Callable)`: Removes a function from the list of listeners for a specified event type.
        - `dispatch(self, event: Event)`: Sends an event to all registered listeners for that event type.

2. **Event**:
    - **Purpose**: Represents a generic event in the system.
    - **Attributes**:
        - `type` (EventType): The type of the event.
        - `data` (Any): Associated data with the event.
    - **Methods**:
        - `__init__(self, event_type: EventType, data: Any = None)`: Constructor for the Event.

3. **EventType** (Enum):
    - **Purpose**: Enumerates the different types of events that can be dispatched within the system.
    - **Values**:
        - `AUDIO_INPUT`: An event related to audio input.
        - `VISUAL_INPUT`: An event related to visual input.
        ... [other event types]

#### Dependencies:
The `event_manager` module heavily interacts with the `brain_message` module, utilizing the `BrainMessage` and `MessageType` classes to facilitate communication between different parts of the system.

#### Main Execution:
When executed directly, the module demonstrates the registration of event listeners, the dispatching of events, and the subsequent calling of registered listeners, showcasing the dynamic event-driven communication within the system.




### Memory Manager

#### File Path:
`BrainRoot/memory_manager.py`

#### Overview:
The `memory_manager` module is responsible for handling the storage and retrieval of memories within the JarvisoBrain system. It interacts with the centralized SQLite database (`mainbrain.db`) to log brain activities, store processed data, and provide retrieval mechanisms for decision-making and other processes.

#### Classes:

1. **MemoryManager**:
    - **Purpose**: Offers methods to interact with the SQLite database, encompassing functions for storing, retrieving, and querying memories.
    - **Attributes**:
        - `connection` (sqlite3.Connection): The database connection object.
        - `cursor` (sqlite3.Cursor): The database cursor for executing SQL commands.
    - **Methods**:
        - `save_memory(self, memory: BrainMessage)`: Stores a memory (`BrainMessage`) into the SQLite database.
        - `retrieve_memory(self, criteria: dict)`: Retrieves memories based on specified criteria.
        - `query_database(self, query: str)`: Directly executes an SQL query on the database.
        - `close_connection(self)`: Closes the database connection.

#### Dependencies:
The `memory_manager` module is closely linked with the `brain_message` module, particularly using the `BrainMessage` class to format and structure the memories it manages. It also interacts with the SQLite3 library for database operations.

#### Main Execution:
When executed directly, the module demonstrates the process of saving a new memory to the database, retrieving specific memories based on criteria, and querying the database directly.




### Controller

#### File Path:
`BrainRoot/controller.py`

#### Overview:
The `controller` module acts as the central orchestrator for the JarvisoBrain system. It coordinates between various brain regions, manages the flow of information, and oversees the overall operation of the artificial brain.

#### Classes:

1. **Controller**:
    - **Purpose**: Provides the main interface for the JarvisoBrain's operations, managing the interactions between different modules and ensuring the system runs smoothly.
    - **Attributes**:
        - `brain_regions` (dict): A dictionary holding instances of various brain regions.
        - `event_dispatcher` (EventDispatcher): An instance of the event manager to handle events and communication.
    - **Methods**:
        - `register_brain_region(self, region_name: str, region_instance)`: Registers a new brain region to the controller.
        - `dispatch_event(self, event: Event)`: Sends an event to the appropriate brain region for processing.
        - `process_input(self, input_data: dict)`: Processes external input by routing it to the correct brain region.
        - `execute_task(self, task_data: dict)`: Executes a specific task based on the provided data.

#### Dependencies:
The `controller` module collaborates with many other modules in the system. It directly interfaces with the `event_manager` for event dispatching and manages instances of various brain regions.

#### Main Execution:
When executed directly, the module showcases the registration of different brain regions, the dispatching of events, and the processing of inputs to demonstrate the controller's role as the central coordinator.




### Neural Database

The `NeuralDatabase` directory is responsible for the management, storage, and retrieval of data within the JarvisoBrain. It serves as the primary data persistence mechanism and enables long-term storage of memories, events, and other critical brain activities.

#### File Path:
`NeuralDatabase/database.py`

#### Overview:
The `database.py` module provides the functionality to interact with an SQLite database, enabling data storage and retrieval. This centralized database acts as the long-term memory storage of the JarvisoBrain, ensuring that past data is available for decision-making and other processes.

#### Classes:

1. **DatabaseManager**:
    - **Purpose**: Manages interactions with the SQLite database.
    - **Attributes**:
        - `connection` (sqlite3.Connection): The connection to the SQLite database.
        - `cursor` (sqlite3.Cursor): Cursor object to execute SQL queries.
    - **Methods**:
        - `__init__(self, db_name: str)`: Initializes the database manager and establishes a connection.
        - `execute_query(self, query: str, parameters: Tuple)`: Executes an SQL query with provided parameters.
        - `fetch_data(self, query: str, parameters: Tuple)`: Executes an SQL query and fetches the results.
        - `close_connection(self)`: Closes the database connection.

#### Dependencies:
The `database.py` module relies on the `sqlite3` module from Python's standard library for database operations. 

#### Main Execution:
When run as a standalone module, it demonstrates the database's creation, storage of mock data, and retrieval operations to validate its core functionality.





### Neuromodulatory Systems

The `NeuromodulatorySystems` directory encompasses the various neuromodulatory systems present in the JarvisoBrain. These systems emulate the biochemical processes and effects of different neurotransmitters in the human brain, influencing neural activity, learning, memory, and behavior.

#### Overview:
Neuromodulatory systems play a crucial role in regulating neuron firing, synaptic plasticity, and overall network dynamics. By simulating these systems, JarvisoBrain can adjust its behavior and responses based on various internal and external factors, akin to real-life emotional and cognitive shifts.

#### Subdirectories and Files:

1. **Cholinergic System**:
    - **File Path**: `NeuromodulatorySystems/CholinergicSystem/cholinergic_system.py`
    - **Purpose**: Simulates the effects and functionalities of the cholinergic system, primarily associated with attention, arousal, and memory processes.
    - **Classes**:
        - **CholinergicSystem**:
            - **Attributes**: 
                - `neurons`: List of neurons associated with this system.
                - `synapses`: Synaptic connections influenced by acetylcholine.
            - **Methods**:
                - `modulate_activity`: Modulates neural activity based on acetylcholine levels.
                - `adjust_synaptic_weights`: Alters synaptic weights influenced by this system.
    
2. **Dopamine System**:
    - **File Path**: `NeuromodulatorySystems/DopamineSystem/dopamine_system.py`
    - **Purpose**: Represents the dopaminergic system, which plays a pivotal role in reward, motivation, and movement.
    - **Classes**:
        - **DopamineSystem**:
            - **Attributes**: 
                - `neurons`: Neurons linked with dopamine release and effects.
                - `synapses`: Synaptic connections influenced by dopamine.
            - **Methods**:
                - `modulate_activity`: Modifies neural activity based on dopamine concentrations.
                - `influence_learning`: Influences learning processes due to dopamine-mediated reinforcement.
                
3. **Neuromodulatory System**:
    - **File Path**: `NeuromodulatorySystems/NeuromodulatorySystem/`
    - **Purpose**: This directory contains multiple files, each representing a different neuromodulatory system.
        - **acetylcholine_system.py**: Manages acetylcholine's effects, which play a role in arousal, attention, and other cognitive functions.
        - **endocannabinoid_system.py**: Represents the endocannabinoid system, which modulates various processes like appetite, pain sensation, mood, and memory.
        - **norepinephrine_system.py**: Simulates the norepinephrine system, primarily associated with attention and responding to stimuli.

4. **Noradrenergic System**:
    - **File Path**: `NeuromodulatorySystems/NoradrenergicSystem/noradrenergic_system.py`
    - **Purpose**: Simulates the noradrenergic system, which plays a key role in alertness and arousal.
    - **Classes**:
        - **NoradrenergicSystem**:
            - **Attributes**: 
                - `neurons`: Neurons associated with this system.
                - `synapses`: Synaptic connections influenced by norepinephrine.
            - **Methods**:
                - `modulate_activity`: Modulates neural activity based on norepinephrine levels.
                - `influence_attention`: Alters attention levels based on this system's activity.

5. **Serotonin System**:
    - **File Path**: `NeuromodulatorySystems/SerotoninSystem/serotonin_system.py`
    - **Purpose**: Represents the serotonergic system, associated with mood regulation, appetite, and sleep.
    - **Classes**:
        - **SerotoninSystem**:
            - **Attributes**: 
                - `neurons`: Neurons linked with serotonin release and effects.
                - `synapses`: Synaptic connections influenced by serotonin.
            - **Methods**:
                - `modulate_activity`: Modifies neural activity based on serotonin concentrations.
                - `influence_mood`: Influences mood states due to serotonin levels.




### Neurons

#### File Path:
`Neurons/`

#### Overview:
The `Neurons` directory encapsulates the different types of neurons present in the JarvisoBrain model. Neurons are fundamental units responsible for receiving, processing, and transmitting information through electrical and chemical signals.

#### Subdirectories and Files:

1. **Interneurons**:
    - **File Path**: `Neurons/Interneurons/interneurons.py`
    - **Purpose**: Represents neurons that neither are sensory nor motor neurons but connect neurons within the brain and spinal cord.
    - **Classes**:
        - **Interneuron**: Basic implementation of an interneuron with methods to receive and process signals.

2. **MotorNeurons**:
    - **File Path**: `Neurons/MotorNeurons/motor_neurons.py`
    - **Purpose**: Represents neurons that transmit commands from the central nervous system to muscles.
    - **Classes**:
        - **MotorNeuron**: Implementation of a motor neuron with methods to activate muscle movements.

3. **SensoryNeurons**:
    - **File Path**: `Neurons/SensoryNeurons/sensory_neurons.py`
    - **Purpose**: Represents neurons responsible for converting external stimuli from the environment into internal electrical impulses.
    - **Classes**:
        - **SensoryNeuron**: Basic sensory neuron implementation with methods to capture and process sensory input.

### Synapses

#### File Path:
`Synapses/`

#### Overview:
The `Synapses` directory contains implementations representing connections between neurons. Synapses play an essential role in transmitting signals, either amplifying or inhibiting them based on their type.

#### Subdirectories and Files:

1. **ExcitatorySynapses**:
    - **File Path**: `Synapses/ExcitatorySynapses/`
    - **Purpose**: Houses synapses that amplify the signals.
    - **Files**:
        - **dopaminergic_synapse.py**: Implementation for synapses using dopamine as a neurotransmitter.
        - **excitatory_synapses.py**: General management for various excitatory synapses.
        - **glutamatergic_synapse.py**: Implementation for synapses using glutamate as a neurotransmitter.

2. **InhibitorySynapses**:
    - **File Path**: `Synapses/InhibitorySynapses/`
    - **Purpose**: Contains synapses that inhibit the signals.
    - **Files**:
        - **cholinergic_synapse.py**: Synapses using acetylcholine as a neurotransmitter.
        - **gabaergic_synapse.py**: Synapses utilizing GABA (gamma-aminobutyric acid).
        - **glycinergic_synapse.py**: Synapses employing glycine as a neurotransmitter.
        - **inhibitory_synapses.py**: General management of various inhibitory synapses.

3. **NeuromodulatorySynapses**:
    - **File Path**: `Synapses/NeuromodulatorySynapses/`
    - **Purpose**: Represents synapses that modulate other synapses or neurons' activity.
    - **Files**:
        - **endocannabinoid_synapse.py**: Synapses influenced by the endocannabinoid system.
        - **neuromodulatory_synapses.py**: General management for various neuromodulatory synapses.
        - **noradrenergic_synapse.py**: Synapses using norepinephrine.
        - **serotonergic_synapse.py**: Synapses employing serotonin.




