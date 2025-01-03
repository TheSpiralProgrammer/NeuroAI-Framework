import numpy as np

class HebbianLearning:
    """
    Implements Hebbian learning for synaptic weight updates.
    """

    def __init__(self, learning_rate=0.01):
        """
        Initialize the Hebbian learning rule.
        :param learning_rate: The rate at which weights are updated.
        """
        self.learning_rate = learning_rate

    def update_weights(self, weights, pre_activations, post_activations):
        """
        Update weights based on pre- and post-synaptic neuron activations.
        :param weights: Current weight matrix (2D numpy array).
        :param pre_activations: Pre-synaptic activations (1D numpy array).
        :param post_activations: Post-synaptic activations (1D numpy array).
        :return: Updated weight matrix.
        """
        delta_w = self.learning_rate * np.outer(post_activations, pre_activations)
        return weights + delta_w
