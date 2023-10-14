import json
from src.dialogue_manager import DialogueManager


class TestManager:
    def __init__(self, test_data_path, dialogue_manager):
        self.test_data_path = test_data_path
        self.dialogue_manager = dialogue_manager
        self.load_test_data()

    def load_test_data(self):
        with open(self.test_data_path, 'r') as file:
            self.test_data = json.load(file)

    def evaluate(self):
        correct_responses = 0
        total_questions = len(self.test_data)

        for question, expected_answer in self.test_data:
            response, _, _ = self.dialogue_manager.respond(question)
            if self.compare_responses(response, expected_answer):
                correct_responses += 1

        accuracy = correct_responses / total_questions
        return accuracy

    @staticmethod
    def compare_responses(response, expected_answer):
        # This is a basic comparison. It can be enhanced to handle synonyms, semantic meaning, etc.
        return response.strip().lower() == expected_answer.strip().lower()

    def run_tests(self):
        accuracy = self.evaluate()
        print(f"Bot accuracy: {accuracy * 100:.2f}%")


if __name__ == '__main__':
    test_data_path = 'path_to_test_data.json'
    # Assuming DialogueManager takes a local model and a context manager as initialization parameters
    local_model = None  # Replace with your local model initialization
    context_manager = None  # Replace with your context manager initialization
    dialogue_manager = DialogueManager(local_model, context_manager)

    manager = TestManager(test_data_path, dialogue_manager)
    manager.run_tests()
