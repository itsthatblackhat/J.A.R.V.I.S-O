import re


class PostProcessor:

    def __init__(self):
        self.repetitive_phrases = ["I think", "In my opinion", "As I said", "Like I said"]

    def correct_grammar(self, text):
        # Here are some basic grammar corrections. This list can be expanded.
        corrections = {
            ' i ': ' I ',
            ' dont ': " don't ",
            ' isnt ': " isn't ",
            ' i\'m ': " I'm ",
            ' im ': " I'm ",
            ' youre ': " you're ",
            ' theyre ': " they're ",
            ' we\'re ': " we're ",
        }

        for incorrect, correct in corrections.items():
            text = text.replace(incorrect, correct)

        return text

    def remove_repetitive_phrases(self, text):
        for phrase in self.repetitive_phrases:
            text = text.replace(phrase, '')

        return text

    def process(self, text):
        text = self.correct_grammar(text)
        text = self.remove_repetitive_phrases(text)
        return text

# Usage:
# processor = PostProcessor()
# cleaned_text = processor.process(original_text)
