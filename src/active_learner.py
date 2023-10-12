import random

class ActiveLearner:
    def __init__(self):
        self.unlabeled_data = []
        self.labeled_data = []

    def add_unlabeled_data(self, interaction):
        self.unlabeled_data.append(interaction)

    def get_data_for_labeling(self):
        if not self.unlabeled_data:
            return None

        # As a simple approach, we can just pick the first interaction from the unlabeled data.
        # Later, we can refine this to select the most uncertain samples.
        uncertain_interaction = self.unlabeled_data[0]
        self.unlabeled_data.pop(0)
        return uncertain_interaction

    def receive_label(self, interaction, label):
        self.labeled_data.append((interaction, label))
