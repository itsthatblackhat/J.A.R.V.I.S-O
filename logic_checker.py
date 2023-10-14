class LogicAndConsistencyChecker:
    def __init__(self):
        # This is a simple list for demonstration purposes.
        # You can expand this list based on the common undesirable phrases you encounter.
        self.invalid_phrases = [
            "Error calling OpenAI API",
            "Database insertion error",
            "Database retrieval error",
            "Database deletion error",
            # Add more phrases as needed
        ]

    def check(self, response_text):
        """
        Check if the response contains any of the undesirable phrases.

        Args:
            response_text (str): The generated response text.

        Returns:
            bool: True if the response is valid (doesn't contain undesirable phrases), otherwise False.
        """
        for phrase in self.invalid_phrases:
            if phrase in response_text:
                return False
        return True

