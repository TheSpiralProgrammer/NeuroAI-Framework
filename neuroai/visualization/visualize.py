import numpy as np
import matplotlib.pyplot as plt

def plot_neuron_activity(activity_matrix, title="Neuron Activity Over Time"):
    """
    Plots neuron activations over time.
    :param activity_matrix: A matrix where each row is the time steps and columns represent individual neurons.
    :param title: Title of the plot
    """
    plt.figure(figsize=(10, 6))
    plt.imshow(activity_matrix, aspect='auto', cmap='viridis', interpolation='none')
    plt.colorbar(label="Activation")
    plt.xlabel("Neurons")
    plt.ylabel("Time Steps")
    plt.title(title)
    plt.show()

def plot_weight_matrix(weights, title="Synaptic Weight Matrix"):
    """
    Plots the synaptic weights.
    :param weights: The current synaptic weight matrix.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(weights, cmap='viridis', interpolation='none')
    plt.colorbar(label="Weight Strength")
    plt.title(title)
    plt.show()
