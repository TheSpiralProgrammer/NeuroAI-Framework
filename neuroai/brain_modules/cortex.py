import numpy as np
import math

class PrefrontalCortex:
    """
    Simulates a model of the Prefrontal Cortex with capabilities for:
    - Decision-making
    - Working memory
    - Hebbian learning
    - Neuron activation using a customizable activation function
    """

    def __init__(self, input_size, output_size, memory_capacity=5, learning_rate=0.01):
        self.input_size = input_size
        self.output_size = output_size
        self.memory_capacity = memory_capacity
        self.working_memory = []
        self.learning_rate = learning_rate

        # Initialize synaptic weights for the neuron
        # Randomize the weights to simulate neural connections
        self.weights = np.random.randn(input_size, output_size)  # Shape (input_size, output_size)

    def add_to_memory(self, item):
        """
        Add an item to working memory. Evicts the oldest item if capacity is exceeded.
        :param item: The item to add
        """
        if len(self.working_memory) >= self.memory_capacity:
            self.working_memory.pop(0)  # Evict oldest item
        self.working_memory.append(item)

    def decide(self, options, scores):
        """
        Make a decision based on options and their scores using a simple decision rule.
        :param options: List of options to choose from
        :param scores: Corresponding scores for each option
        :return: The selected option
        """
        index = np.argmax(scores)
        return options[index]

    def get_memory(self):
        """Return the current state of working memory."""
        return self.working_memory

    def neuron_activation(self, input_data, activation_function="sigmoid"):
        """
        Simulates neuron activation using a specified activation function.
        :param input_data: List of input data values
        :param activation_function: The activation function to use ('sigmoid', 'tanh', etc.)
        :return: A list of activated values after applying the activation function
        """
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        def tanh(x):
            return np.tanh(x)

        # Choose activation function
        if activation_function == "sigmoid":
            activation_func = sigmoid
        elif activation_function == "tanh":
            activation_func = tanh
        else:
            raise ValueError(f"Unsupported activation function: {activation_function}")

        # Calculate output for each neuron by applying weights and activation
        weighted_sum = np.dot(input_data, self.weights)  # Linear combination of inputs and weights
        activated_output = activation_func(weighted_sum)  # Apply the activation function

        # Return output matching 'output_size' (size truncation or expansion)
        return activated_output[:self.output_size]

    def hebbian_learning(self, input_data, output_data):
        """
        Apply Hebbian learning: updates synaptic weights based on input and output activities.
        :param input_data: The input data to the neurons
        :param output_data: The output data from the neurons
        """
        input_array = np.array(input_data).reshape(-1, 1)
        output_array = np.array(output_data).reshape(1, -1)

        # Hebbian learning rule: Δw = η * input * output (outer product of input and output)
        delta_weights = self.learning_rate * np.dot(input_array, output_array)

        # Update the synaptic weights
        self.weights += delta_weights

        print("Hebbian learning applied! Updated weights:")
        print(self.weights)

    def reset_weights(self):
        """Reset weights to random values."""
        self.weights = np.random.randn(self.input_size, self.output_size)
        print("Weights have been reset to random values.")
