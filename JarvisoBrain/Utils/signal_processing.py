# This utility will focus on general signal processing functions that might be useful for neural computations or data preprocessing.
# For the sake of the example, I'll create basic functions for normalizing data and applying a simple filter.
# You can expand on this utility with more advanced processing functions in the future as needed.

import numpy as np

class SignalProcessor:
    def __init__(self):
        pass

    @staticmethod
    def normalize_data(data):
        """
        Normalize the data to have a mean of 0 and standard deviation of 1.

        Args:
        - data (list or np.array): Input data to be normalized.

        Returns:
        - np.array: Normalized data.
        """
        data = np.array(data)
        mean = data.mean()
        std = data.std()
        return (data - mean) / std

    @staticmethod
    def apply_filter(data, filter_type="lowpass", cutoff_frequency=1.0):
        """
        Apply a simple filter to the data.

        Args:
        - data (list or np.array): Input data to be filtered.
        - filter_type (str): Type of the filter to be applied ["lowpass", "highpass"].
        - cutoff_frequency (float): Cutoff frequency for the filter.

        Returns:
        - np.array: Filtered data.
        """
        # This is a placeholder. In practice, you'd implement a proper filtering technique using libraries like scipy.
        data = np.array(data)
        if filter_type == "lowpass":
            # Placeholder for a lowpass filter
            return np.clip(data, a_min=None, a_max=cutoff_frequency)
        elif filter_type == "highpass":
            # Placeholder for a highpass filter
            return np.clip(data, a_min=cutoff_frequency, a_max=None)
        else:
            raise ValueError(f"Unknown filter type: {filter_type}")

if __name__ == "__main__":
    # Example usage:
    processor = SignalProcessor()

    example_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    normalized_data = processor.normalize_data(example_data)
    print("Normalized Data:", normalized_data)

    filtered_data = processor.apply_filter(example_data, filter_type="lowpass", cutoff_frequency=5.5)
    print("Filtered Data (Lowpass):", filtered_data)

    filtered_data_highpass = processor.apply_filter(example_data, filter_type="highpass", cutoff_frequency=5.5)
    print("Filtered Data (Highpass):", filtered_data_highpass)
