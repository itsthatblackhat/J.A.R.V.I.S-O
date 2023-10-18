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

## Summary of To-Dos
1. Implement methods in each BrainRegion for complete data flow.
2. Establish the connection between different types of Neurons and Synapses.
3. Implement the NeuromodulatorySystems for emotional and reward-based feedback.
4. Complete the Utils for data loading, feedback processing, signal processing, and visualization.
5. Ensure that all modules are connected to MemoryManager and EventManager appropriately for data storage and event triggering.
6. Implement the `main_brain.py` to initialize and control all other modules.

## Summary of Interactions
1. BrainRoot acts as the central control, initializing all other modules.
2. BrainRegions process and send sensory data to Thalamus and other specialized brain regions.
3. NeuromodulatorySystems provide emotional and reward-based context to BrainRegions and Neurons.
4. Neurons act as the functional units, transmitting signals across BrainRegions and to Synapses.
5. Synapses serve as the points of contact between Neurons, modulating the signals.
6. Utils provide auxiliary functionalities like data loading, signal processing, and feedback.
7. `main_brain.py` is the entry point that ties all these components together.
