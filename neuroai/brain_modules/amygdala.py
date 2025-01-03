import numpy as np

class Amygdala:
    def __init__(self, emotion_sensitivity=0.5):
        """
        Initialize Amygdala with emotion sensitivity. 
        - Sensitivity can range from 0 (no emotional influence) to 1 (strong emotional influence)
        :param emotion_sensitivity: The sensitivity factor to influence decisions
        """
        self.emotion_sensitivity = emotion_sensitivity
        self.emotion_map = {
            "fear": -1,
            "anger": -0.5,
            "joy": 1,
            "sadness": 0.5
        }

    def process_emotion(self, emotion):
        """
        Process the current emotion and influence decision scores.
        :param emotion: The current emotional state (e.g., "joy", "fear")
        :return: Emotional impact score to adjust decision-making
        """
        return self.emotion_map.get(emotion, 0) * self.emotion_sensitivity

    def update_sensitivity(self, new_sensitivity):
        """
        Update the emotional sensitivity factor of the Amygdala.
        :param new_sensitivity: New value for emotion sensitivity
        """
        self.emotion_sensitivity = new_sensitivity
        print(f"Amygdala emotional sensitivity updated to: {self.emotion_sensitivity}")
