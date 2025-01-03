# basal_ganglia.py

class BasalGanglia:
    def __init__(self):
        """
        The Basal Ganglia influences movement decisions, action selection, and reinforcement learning.
        """
        self.rewards = {}

    def process_decision(self, action, reward):
        """Process action decision based on reward feedback."""
        self.rewards[action] = self.rewards.get(action, 0) + reward
        return f"Decision for action '{action}' with current reward: {self.rewards[action]}"
