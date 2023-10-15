import sqlite3
from datetime import datetime
from enum import Enum


class MessageType(Enum):
    SENSORY_DATA = "SensoryData"
    PROCESSED_DATA = "ProcessedData"
    MEMORY_REQUEST = "MemoryRequest"
    MEMORY_RESPONSE = "MemoryResponse"
    EMOTION_SIGNAL = "EmotionSignal"
    ACTION_SIGNAL = "ActionSignal"
    FEEDBACK = "Feedback"
    LEARNING_SIGNAL = "LearningSignal"
    MOTOR_SIGNAL = "MotorSignal"
    FEEDBACK_STORED = "FeedbackStored"
    TRAINING_DATA_STORED = "TrainingDataStored"
    NEURAL_UPDATE = "NeuralUpdate"
    ALERT = "Alert"
    QUERY = "Query"
    MEMORY_STORE_REQUEST = "MemoryStoreRequest"
    MEMORY_RECALL_REQUEST = "MemoryRecallRequest"
    INTERACTION = "Interaction"  # Added based on previous discussions


class ProcessingDirective(Enum):
    IMMEDIATE = "Immediate"
    DEFERRED = "Deferred"
    STORE = "Store"
    RECALL = "Recall"
    LEARN = "Learn"
    ACTIVATE = "Activate"
    DEACTIVATE = "Deactivate"
    UPDATE = "Update"
    INVESTIGATE = "Investigate"


class BrainMessage:
    def __init__(self, db_path, message_type, data_payload, processing_directive, source, destination, context=None,
                 priority=1):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        self.message_type = MessageType(message_type)
        self.data_payload = data_payload
        self.processing_directive = ProcessingDirective(processing_directive)
        self.metadata = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "source": source,
            "destination": destination,
            "priority": priority,
            "context": context if context else {}
        }

    def get_message(self):
        return {
            "message_type": self.message_type.value,
            "data_payload": self.data_payload,
            "processing_directive": self.processing_directive.value,
            "metadata": self.metadata
        }

    def save_to_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                               (timestamp text, source text, destination text, message_type text, 
                               data_payload text, processing_directive text, priority integer, context text)''')
        self.cursor.execute("INSERT INTO messages VALUES (?,?,?,?,?,?,?,?)",
                            (self.metadata["timestamp"], self.metadata["source"], self.metadata["destination"],
                             self.message_type.value, str(self.data_payload), self.processing_directive.value,
                             self.metadata["priority"], str(self.metadata["context"])))
        self.connection.commit()

    def update_context(self, key, value):
        self.metadata["context"][key] = value

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    # Example of how BrainMessage can be used:
    visual_data = {
        "data_type": "Visual",
        "data_values": [1, 2, 3, 4, 5]
    }

    msg = BrainMessage(
        db_path='JarvisoBrain/NeuralDatabase/mainbrain.db',
        message_type=MessageType.SENSORY_DATA,
        data_payload=visual_data,
        processing_directive=ProcessingDirective.IMMEDIATE,
        source="VisualCortex",
        destination="PrefrontalCortex"
    )
    print(msg.get_message())
    msg.save_to_db()
    msg.close()
