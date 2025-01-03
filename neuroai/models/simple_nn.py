import numpy as np
from neuroai.learning_rules.hebbian import HebbianLearning
from neuroai.learning_rules.stdp import STDP

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rule='hebbian'):
        """
        Initialize the simple feedforward neural network with learning rules.
        :param input_size: Number of input neurons.
        :param hidden_size: Number of hidden neurons.
        :param output_size: Number of output neurons.
        :param learning_rule: The type of learning rule ('hebbian' or 'stdp').
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rule = learning_rule

        # Randomly initialize weights (input-to-hidden and hidden-to-output)
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)

        # Instantiate the chosen learning rule
        if self.learning_rule == 'hebbian':
            self.learning_rule = HebbianLearning(learning_rate=0.01)
        elif self.learning_rule == 'stdp':
            self.learning_rule = STDP(a_plus=0.01, a_minus=0.012, tau=20.0)

    def feedforward(self, inputs):
        """
        Perform a feedforward pass through the network.
        :param inputs: Input vector for the network.
        :return: Output from the network.
        """
        hidden_layer_input = np.dot(inputs, self.weights_input_hidden)
        hidden_layer_output = np.tanh(hidden_layer_input)  # Tanh as activation
        final_output = np.dot(hidden_layer_output, self.weights_hidden_output)
        return final_output

    def train(self, inputs, target, num_epochs=100):
        """
        Train the neural network using a simple feedforward and learning rule-based approach.
        :param inputs: Training input data.
        :param target: Expected output for the input data.
        :param num_epochs: Number of training epochs.
        """
        for epoch in range(num_epochs):
            # Feedforward step
            output = self.feedforward(inputs)

            # Compute error (basic squared error)
            error = target - output

            # Update weights based on the chosen learning rule (Hebbian or STDP)
            self.weights_input_hidden = self.learning_rule.update_weights(self.weights_input_hidden,
                                                                          inputs, output)
            self.weights_hidden_output = self.learning_rule.update_weights(self.weights_hidden_output,
                                                                          inputs, output)

            if epoch % 10 == 0:
                print(f"Epoch {epoch+1}/{num_epochs}, Error: {np.mean(error)}")

