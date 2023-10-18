# Jarviso Brain Wiring Logic & Details - Full Scope

## Application Entry Point

### main_brain.py
- **Connects To**: 
    - BrainRoot (Initializes the overall brain architecture)
    - NeuralDatabase (Initializes database operations)
    - BrainRegions (Initiates sensory data processing)
    - NeuromodulatorySystems (Initiates emotional and reward systems)

## BrainRegions

### AuditoryCortex
- **Connects To**: 
    - SensoryNeurons (Input for raw auditory data)
    - SerotoninSystem (Input for emotional state)
    - Thalamus (Output for processed auditory signals)
    - MemoryManager (`mainbrain.db`) (Retrieval of past auditory data)

### BasalGanglia
- **Connects To**: 
    - Prefrontal Cortex (Input for decision parameters)
    - Auditory Cortex (Input for auditory signals)
    - Visual Cortex (Input for visual data)
    - DopamineSystem (Input for reward expectations)
    - Motor Neurons (Output for decisions)
    - MemoryManager (`mainbrain.db`) (Storage of decision and outcomes)
    - EventManager (Triggering decision-making events)

### Brainstem
- **Connects To**: 
    - Sensory Neurons (Input for all sensory data)
    - All NeuromodulatorySystems (Input for emotional states)
    - Thalamus (Output for refined sensory data)

### Cerebellum
- **Connects To**: 
    - Motor Neurons (Input for motor commands)
    - Sensory Neurons (Input for sensory feedback)
    - Brainstem (Output for refined motor commands)

### Hippocampus
- **Connects To**: 
    - Thalamus (Input for consolidated sensory data)
    - MemoryManager (`mainbrain.db`) (Output for long-term memory storage)
    - NoradrenergicSystem (Input for emotional context)

### Hypothalamus
- **Connects To**: 
    - All NeuromodulatorySystems (Input for emotional and homeostatic states)
    - Thalamus (Output for emotional and homeostatic state modulation)
    - Brainstem (Input for sensory data related to homeostasis)

### PrefrontalCortex
- **Connects To**: 
    - Auditory Cortex (Input for processed auditory signals)
    - Visual Cortex (Input for processed visual signals)
    - MemoryManager (`mainbrain.db`) (Output for long-term plans and decisions)
    - BasalGanglia (Output for decision-making parameters)

### SomatosensoryCortex
- **Connects To**: 
    - Sensory Neurons (Input for tactile data)
    - Thalamus (Output for processed tactile data)
    - MemoryManager (`mainbrain.db`) (Retrieval of past tactile experiences)

### Thalamus
- **Connects To**: 
    - All BrainRegions (Input for processed sensory data)
    - Hippocampus (Output for memory consolidation)
    - Prefrontal Cortex (Output for decision-making)

### VisualCortex
- **Connects To**: 
    - Sensory Neurons (Input for raw visual data)
    - Thalamus (Output for processed visual data)
    - MemoryManager (`mainbrain.db`) (Retrieval of past visual data)

## BrainRoot

### brain_message.py
- **Connects To**: 
    - All BrainRegions (Standardizes messages)
    - All NeuromodulatorySystems (Standardizes messages)

### controller.py
- **Connects To**: 
    - MemoryManager (`mainbrain.db`) (Database operations)
    - All Neurons and Synapses (Management and triggering)

### event_manager.py
- **Connects To**: 
    - All BrainRegions (Event triggering)
    - All NeuromodulatorySystems (Event triggering)

### memory_manager.py
- **Connects To**: 
    - NeuralDatabase (`mainbrain.db`) (All database operations)
    - All BrainRegions (For data storage and retrieval)
    - All NeuromodulatorySystems (For emotional and reward-based data storage)

### __init__.py (BrainRoot)
- **Connects To**: 
    - All BrainRoot modules (For initialization)

## NeuralDatabase

### database.py
- **Connects To**: 
    - MemoryManager (For all database operations)

### mainbrain.db
- **Connects To**: 
    - All modules (For data storage and retrieval)

## NeuromodulatorySystems

### CholinergicSystem
- **Connects To**: 
    - Brainstem (Input for emotional state)
    - Auditory Cortex (Output for context-aware auditory processing)
    - DopamineSystem (Interacts for reward-based learning)

### DopamineSystem
- **Connects To**: 
    - Basal Ganglia (Input for decision confirmation)
    - Brainstem (Input for emotional state)
    - Auditory Cortex (Output for context-aware auditory processing)

### NeuromodulatorySystem (Parent class)
- **Connects To**: 
    - All specialized Neuromodulatory Systems (For general behaviors)

### NoradrenergicSystem
- **Connects To**: 
    - Brainstem (Input for emotional state)
    - Hippocampus (Output for memory consolidation)

### SerotoninSystem
- **Connects To**: 
    - Brainstem (Input for emotional state)
    - All BrainRegions (Output for context-aware processing)

## Neurons

### Interneurons
- **Connects To**: 
    - All BrainRegions (For localized signal processing)
    - Synapses (For connections)

### MotorNeurons
- **Connects To**: 
    - BasalGanglia (Input for decisions)
    - Brainstem (Output for action execution)

### SensoryNeurons
- **Connects To**: 
    - All BrainRegions (For processing sensory data)
    - Excitatory and Inhibitory Synapses (For transmitting signals)

## Synapses

### ExcitatorySynapses
- **Connects To**: 
    - Sensory Neurons (For receiving signals)
    - Interneurons (For transmitting signals)

### InhibitorySynapses
- **Connects To**: 
    - Interneurons (For receiving signals)
    - Motor Neurons (For transmitting signals)

### NeuromodulatorySynapses
- **Connects To**: 
    - All NeuromodulatorySystems (For receiving neuromodulatory signals)
    - Interneurons and Motor Neurons (For transmitting signals)

## Utils

### data_loader.py
- **Connects To**: 
    - SensoryNeurons (For loading sensory data)
    - NeuralDatabase (For storing and retrieving data)

### feedback_processor.py
- **Connects To**: 
    - All BrainRegions (For processing feedback)
    - All NeuromodulatorySystems (For emotional and reward-based feedback)
    - NeuralDatabase (`mainbrain.db`) (For storing feedback)

### signal_processing.py
- **Connects To**: 
    - SensoryNeurons (For initial signal processing)
    - BrainRegions (For additional signal refinement)

### visualization.py
- **Connects To**: 
    - All BrainRegions (For data visualization)
    - All NeuromodulatorySystems (For emotional and reward-based visualization)

### __init__.py (Utils)
- **Connects To**: 
    - All Utils modules (For initialization)



============================================================================================


## Summary of To-Dos
1. Implement methods in each BrainRegion for complete data flow.
### Brainstem
- `receive_sensory_data()`: To receive all types of sensory data from Sensory Neurons.
- `receive_emotional_state()`: To get the emotional state from NeuromodulatorySystems.
- `send_to_thalamus()`: To send refined sensory data to the Thalamus.

### Cerebellum
- `receive_motor_command()`: To receive motor commands from Motor Neurons.
- `receive_sensory_feedback()`: To receive sensory feedback from Sensory Neurons.
- `send_refined_motor_command()`: To send refined motor commands to Brainstem.

### Hippocampus
- `receive_from_thalamus()`: To receive consolidated sensory data from the Thalamus.
- `store_long_term_memory()`: To write long-term memory data to `mainbrain.db` via MemoryManager.
- `receive_emotional_context()`: To get emotional context from the NoradrenergicSystem.

### Hypothalamus
- `receive_emotional_state()`: To receive emotional and homeostatic states from NeuromodulatorySystems.
- `send_to_thalamus()`: To send emotional and homeostatic state data to the Thalamus.
- `receive_homeostatic_data()`: To receive sensory data related to homeostasis from the Brainstem.

### PrefrontalCortex
- `receive_auditory_data()`: To receive processed auditory signals from the Auditory Cortex.
- `receive_visual_data()`: To receive processed visual signals from the Visual Cortex.
- `store_long_term_plans()`: To store long-term plans in `mainbrain.db` via MemoryManager.
- `send_decision_params()`: To send decision-making parameters to BasalGanglia.

### SomatosensoryCortex
- `receive_tactile_data()`: To receive tactile data from Sensory Neurons.
- `send_to_thalamus()`: To send processed tactile data to the Thalamus.
- `retrieve_past_tactile_data()`: To retrieve past tactile experiences from `mainbrain.db` via MemoryManager.

### Thalamus
- `receive_from_brainregions()`: To receive processed sensory data from all BrainRegions.
- `send_to_hippocampus()`: To send data for memory consolidation to the Hippocampus.
- `send_to_prefrontal_cortex()`: To send data for decision-making to the Prefrontal Cortex.

### VisualCortex
- `receive_raw_visual_data()`: To receive raw visual data from Sensory Neurons.
- `send_to_thalamus()`: To send processed visual data to the Thalamus.
- `retrieve_past_visual_data()`: To retrieve past visual data from `mainbrain.db` via MemoryManager.




2. Establish the connection between different types of Neurons and Synapses.
### Sensory Neurons
- **Connected via Excitatory Synapses to**:
  - Auditory Cortex: For auditory data.
  - Visual Cortex: For visual data.
  - Somatosensory Cortex: For tactile data.
  
- **Connected via Inhibitory Synapses to**:
  - None: Generally, sensory neurons don't inhibit any other neurons directly.
  
### Motor Neurons
- **Connected via Excitatory Synapses to**:
  - Cerebellum: For refined motor commands.
  
- **Connected via Inhibitory Synapses to**:
  - Interneurons: To regulate muscle contraction and relaxation.
  
### Interneurons
- **Connected via Excitatory Synapses to**:
  - Motor Neurons: To facilitate muscle contraction.
  - Other Interneurons: For complex reflex loops and local circuits.
  
- **Connected via Inhibitory Synapses to**:
  - Motor Neurons: To inhibit unwanted muscle contractions.
  - Other Interneurons: To form inhibitory circuits and balance excitability.

### Neuromodulatory Synapses
- **Connected to**:
  - All types of Neurons: To modulate the overall neural activity based on emotional states or other higher-level functions.
  
### Excitatory Synapses
- **Found in**:
  - Dopaminergic Synapse: Connects neurons in the DopamineSystem.
  - Glutamatergic Synapse: Common in sensory pathways.

### Inhibitory Synapses
- **Found in**:
  - GABAergic Synapse: Common in motor pathways to balance excitability.
  - Glycinergic Synapse: Typically in the spinal cord and brainstem.
  
### Neuromodulatory Synapses
- **Found in**:
  - Noradrenergic Synapse: Connects neurons in the NoradrenergicSystem.
  - Serotonergic Synapse: Connects neurons in the SerotoninSystem.




3. Implement the NeuromodulatorySystems for emotional and reward-based feedback.
### Comprehensive NeuromodulatorySystems Implementation Plan

---

#### Cholinergic System (Acetylcholine)
- **Purpose**: To modulate attention, learning, and memory.
  
- **Methods Needed**:
  1. `receive_attentional_focus()`: To get data from the Prefrontal Cortex.
  2. `receive_learning_data()`: To get data from the Hippocampus.
  3. `modulate_neurons()`: To send acetylcholine to target neurons.

- **Data Structures**:
  - Attentional Queue: To keep track of current attentional focus.
  - Learning Matrix: To store learning variables and states.
  
- **Database Interactions**:
  - Will read/write to `mainbrain.db` to store learning and memory variables.
  
- **Dependencies**:
  - Prefrontal Cortex, Hippocampus, Main Database (`mainbrain.db`).

---

#### Dopamine System
- **Purpose**: To manage reward-based learning, motivation, and pleasure.
  
- **Methods Needed**:
  1. `receive_decision_outcome()`: To get outcomes from the Basal Ganglia.
  2. `receive_expectations()`: To get planning data from the Prefrontal Cortex.
  3. `modulate_reward_neurons()`: To send dopamine to neurons.

- **Data Structures**:
  - Reward Queue: To keep track of rewards and penalties.
  - Expectation Matrix: To store expected outcomes.

- **Database Interactions**:
  - Will read/write to `mainbrain.db` to store rewards and expectations.
  
- **Dependencies**:
  - Basal Ganglia, Prefrontal Cortex, Main Database (`mainbrain.db`).

---

#### Serotonin System
- **Purpose**: To manage mood, emotion, and various physiological processes.
  
- **Methods Needed**:
  1. `receive_emotional_state()`: To get emotional data from various brain regions.
  2. `receive_basic_drives()`: To get basic physiological states from the Hypothalamus.
  3. `modulate_emotional_neurons()`: To send serotonin to target neurons.

- **Data Structures**:
  - Emotional State Matrix: To store current emotional variables.
  - Physiological State Queue: To keep track of basic drives like hunger and sleep.

- **Database Interactions**:
  - Will read/write to `mainbrain.db` to store emotional and physiological states.
  
- **Dependencies**:
  - Hypothalamus, Auditory and Visual Cortices, Main Database (`mainbrain.db`).




4. Complete the Utils for data loading, feedback processing, signal processing, and visualization.



5. Ensure that all modules are connected to MemoryManager and EventManager appropriately for data storage and event triggering.
### MemoryManager and EventManager: Detailed Connection and Implementation Plan

---

#### MemoryManager Connections

1. **BrainRegions**
    - **Required Tables in `mainbrain.db`:**
        - AuditoryCortexData
        - VisualCortexData
        - BasalGangliaData
        - ... (Each BrainRegion should have its own table)
    - **Methods Required**: 
        - `store_processed_data()`: Saves processed sensory data to the respective table.
        - `retrieve_past_data()`: Fetches previous experiences from the respective table for contextual decisions.
    - **Event Triggering**: 
        - On data storage: Trigger `MEMORY_STORED` event.
        - On data retrieval: Trigger `MEMORY_RETRIEVED` event.

2. **NeuromodulatorySystems**
    - **Required Tables in `mainbrain.db`:**
        - DopamineSystemData
        - SerotoninSystemData
        - ... (Each NeuromodulatorySystem should have its own table)
    - **Methods Required**: 
        - `store_emotional_state()`: Saves current emotional state to the respective table.
        - `retrieve_past_emotional_state()`: Fetches previous emotional states from the respective table.
    - **Event Triggering**: 
        - On emotional state change: Trigger `EMOTIONAL_STATE_CHANGED` event.
        - On reward state change: Trigger `REWARD_STATE_CHANGED` event.

3. **Neurons**
    - **Required Tables in `mainbrain.db`:**
        - InterneuronActivity
        - MotorNeuronActivity
        - SensoryNeuronActivity
    - **Methods Required**: 
        - `store_neuron_activity()`: Saves the current neuron firing patterns to the respective table.
    - **Event Triggering**: 
        - On neuron firing: Trigger `NEURON_FIRED` event.

#### EventManager Connections

1. **BrainRegions**
    - **Events Listened For**: 
        - `NEW_SENSORY_DATA`
        - `EMOTIONAL_STATE_CHANGED`
        - `MEMORY_RETRIEVED`
    - **Events Triggered**: 
        - `MEMORY_STORED`
        - `MEMORY_RETRIEVED`
  
2. **NeuromodulatorySystems**
    - **Events Listened For**: 
        - `REWARD_RECEIVED`
        - `PUNISHMENT_RECEIVED`
    - **Events Triggered**: 
        - `EMOTIONAL_STATE_CHANGED`
        - `REWARD_STATE_CHANGED`

3. **Neurons**
    - **Events Listened For**: 
        - `NEW_SENSORY_DATA`
    - **Events Triggered**: 
        - `NEURON_FIRED`

4. **Synapses**
    - **Events Listened For**: 
        - `NEURON_FIRED`
    - **Events Triggered**: 
        - `SYNAPTIC_SIGNAL_SENT`



6. Implement the `main_brain.py` to initialize and control all other modules.

============================================================================================

## Summary of Interactions
1. BrainRoot acts as the central control, initializing all other modules.
2. BrainRegions process and send sensory data to Thalamus and other specialized brain regions.
3. NeuromodulatorySystems provide emotional and reward-based context to BrainRegions and Neurons.
4. Neurons act as the functional units, transmitting signals across BrainRegions and to Synapses.
5. Synapses serve as the points of contact between Neurons, modulating the signals.
6. Utils provide auxiliary functionalities like data loading, signal processing, and feedback.
7. `main_brain.py` is the entry point that ties all these components together.
