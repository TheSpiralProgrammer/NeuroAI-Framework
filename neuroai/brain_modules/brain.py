from neuroai.brain_modules.cortex import PrefrontalCortex
from neuroai.brain_modules.hippocampus import Hippocampus
from neuroai.brain_modules.amygdala import Amygdala
from neuroai.brain_modules.cerebellum import Cerebellum
from neuroai.brain_modules.visual_cortex import VisualCortex
from neuroai.brain_modules.basal_ganglia import BasalGanglia
import random
import numpy as np

class FullBrainWithLearning:
    def __init__(self, input_size, output_size, memory_capacity=5, emotion_sensitivity=0.5, learning_rate=0.1, discount_factor=0.9):
        self.prefrontal_cortex = PrefrontalCortex(input_size, output_size, memory_capacity)
        self.amygdala = Amygdala(emotion_sensitivity)
        self.hippocampus = Hippocampus(memory_capacity)
        
        # Q-learning variables
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {}  # Will store Q-values
        self.state = None  # Current state

    def create_state(self, input_data, emotion, action):
        """
        Create a unique state representation based on the input_data, emotion, and action.
        """
        return f"state_{str(input_data)}_{emotion}_{action}"

    def choose_action(self, state, options, epsilon=0.1):
        """
        Choose an action based on the current state and epsilon-greedy strategy.
        """
        if np.random.rand() < epsilon:  # Exploration: choose a random action
            return np.random.choice(options)
        else:  # Exploitation: choose the best-known action
            if state not in self.q_table:
                self.q_table[state] = [0] * len(options)  # Initialize Q-values if not present
            return options[np.argmax(self.q_table[state])]  # Best action based on Q-table

    def update_q_table(self, previous_state, action, reward, new_state):
        """
        Update the Q-table using the Q-learning algorithm.
        """
        if previous_state not in self.q_table:
            self.q_table[previous_state] = [0] * len(new_state)  # Initialize if not present

        best_future_q = np.max(self.q_table[new_state]) if new_state in self.q_table else 0
        current_q = self.q_table[previous_state][action]
        
        # Q-learning update rule
        self.q_table[previous_state][action] = current_q + self.learning_rate * (reward + self.discount_factor * best_future_q - current_q)

    def think(self, input_data, emotion, options, scores):
        """
        Make a decision based on input data, emotional state, and long-term memory, with reinforcement learning.
        :param input_data: The sensory input
        :param emotion: Current emotional state ("joy", "fear", etc.)
        :param options: List of options to decide between
        :param scores: Corresponding scores for each option
        :return: The chosen option
        """
        # Recall past action from hippocampus to build the state
        if self.state is None:
            previous_action = None
        else:
            previous_action = self.state.split('_')[-1]

        # Create a state based on input data, emotion, and action
        state = self.create_state(input_data, emotion, previous_action)

        # Choose an action using Q-learning strategy
        action = self.choose_action(state, options)

        # Simulate environmental feedback/reward for the selected action
        reward = 1 if action == 'move_forward' else -1  # Example reward structure

        # Update Q-table based on current decision
        self.update_q_table(state, options.index(action), reward, state)  # Use state for simplicity

        # Store the new memory with the input_data, action, and reward
        self.hippocampus.store_memory((input_data, action))

        # Return the action
        return action
