class Hippocampus:
    def __init__(self, memory_capacity=5, decay_rate=0.1):
        """
        :param memory_capacity: Number of memories it can hold
        :param decay_rate: Rate at which memories decay (emotionally weak memories decay faster)
        """
        self.memory_capacity = memory_capacity
        self.memory = []  # Store memories as tuples of (input_data, decision, emotion_impact)
        self.decay_rate = decay_rate

    def store_memory(self, memory):
        """
        Store memory in the hippocampus, applying decay if necessary.
        :param memory: Memory tuple (input_data, decision, emotion_impact)
        """
        if len(self.memory) >= self.memory_capacity:
            self.memory.pop(0)  # Remove oldest memory if capacity exceeded
        self.memory.append(memory)

    def recall_memory(self):
        """
        Recall memories with consideration to emotional intensity.
        Emotional impact influences how long memories are retained.
        """
        for index, (input_data, decision, emotion_impact) in enumerate(self.memory):
            # The lower the emotional impact, the faster the decay
            decay_factor = 1 - (self.decay_rate * emotion_impact)
            if decay_factor < 0:
                decay_factor = 0
            self.memory[index] = (input_data, decision, decay_factor)

        # Filter out any fully decayed memories
        self.memory = [(input_data, decision, emotion_impact) for input_data, decision, emotion_impact in self.memory if emotion_impact > 0]

        return self.memory
