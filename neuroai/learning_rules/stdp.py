import numpy as np

class STDP:
    """
    Implements Spike-Timing-Dependent Plasticity (STDP) for synaptic weight updates.
    """

    def __init__(self, a_plus=0.01, a_minus=0.012, tau=20.0):
        """
        Initialize the STDP parameters.
        :param a_plus: Maximum weight increase (LTP).
        :param a_minus: Maximum weight decrease (LTD).
        :param tau: Time constant for weight updates.
        """
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.tau = tau

    def update_weights(self, weights, spike_timing):
        """
        Update weights based on spike timing differences.
        :param weights: Current weight matrix (2D numpy array).
        :param spike_timing: Matrix of spike time differences (t_post - t_pre).
        :return: Updated weight matrix.
        """
        delta_w = np.where(
            spike_timing > 0,
            self.a_plus * np.exp(-spike_timing / self.tau),
            -self.a_minus * np.exp(spike_timing / self.tau)
        )
        return weights + delta_w

