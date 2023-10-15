import sqlite3
import numpy as np
from typing import List, Tuple

from JarvisoBrain.BrainRoot.event_manager import Event, EventType, EventDispatcher
from JarvisoBrain.BrainRoot.brain_message import BrainMessage, MessageType, ProcessingDirective

DATABASE_NAME = "JarvisoBrain/NeuralDatabase/mainbrain.db"
dispatcher = EventDispatcher()

class FeedbackProcessor:

    def process_sentence(self, sentence: str) -> np.array:
        related_memories = self.retrieve_related_memories(sentence)
        processed_data = self.average_related_memories(related_memories)
        return processed_data


    def retrieve_related_memories(self, sentence: str) -> List[str]:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT user_input FROM feedback_data WHERE user_input LIKE ?', ('%' + sentence + '%',))
        memories = cursor.fetchall()
        conn.close()
        return [memory[0] for memory in memories]


    def average_related_memories(self, memories: List[str]) -> np.array:
        memory_lengths = [len(memory) for memory in memories]
        return np.array([np.mean(memory_lengths)])


    def save_feedback_data_to_db(self, feedback_data: List[Tuple[str, str, str, str]]):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        for data in feedback_data:
            cursor.execute('''
            INSERT INTO feedback_data (user_input, jarviso_response, feedback, feedback_type)
            VALUES (?, ?, ?, ?)
            ''', (data[0], data[1], data[2], data[3]))
        conn.commit()
        conn.close()

        # Dispatching an event after saving feedback
        message = BrainMessage(
            db_path=DATABASE_NAME,
            message_type=MessageType.FEEDBACK,
            data_payload=feedback_data,
            processing_directive=ProcessingDirective.IMMEDIATE,
            source="FeedbackProcessor",
            destination="MemoryManager"
        )
        event = Event(EventType.FEEDBACK_STORED, message)
        dispatcher.dispatch(event)


    def get_feedback_data_from_db(self, feedback_type=None) -> List[Tuple[str, str, str]]:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        if feedback_type:
            cursor.execute('SELECT user_input, jarviso_response, feedback FROM feedback_data WHERE feedback_type = ?',
                           (feedback_type,))
        else:
            cursor.execute('SELECT user_input, jarviso_response, feedback, feedback_type FROM feedback_data')
        feedback_data = cursor.fetchall()
        conn.close()
        return feedback_data


    def save_training_data_to_db(self, training_data: List[Tuple[str, str]]):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        for data in training_data:
            cursor.execute('''
            INSERT INTO training_data (user_input, gpt_response)
            VALUES (?, ?)
            ''', (data[0], data[1]))
        conn.commit()
        conn.close()

        # Dispatching an event after saving training data
        message = BrainMessage(
            db_path=DATABASE_NAME,
            message_type=MessageType.LEARNING_SIGNAL,
            data_payload=training_data,
            processing_directive=ProcessingDirective.IMMEDIATE,
            source="FeedbackProcessor",
            destination="TrainingManager"
        )
        event = Event(EventType.TRAINING_DATA_STORED, message)
        dispatcher.dispatch(event)


    def get_training_data_from_db(self) -> List[Tuple[str, str]]:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT user_input, gpt_response FROM training_data')
        training_data = cursor.fetchall()
        conn.close()
        return training_data
