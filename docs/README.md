
# NeuroAI Framework

**NeuroAI Framework** is a Python library that merges neuroscience and AI principles to create innovative neural network architectures. The framework integrates key components of the brain, such as the Prefrontal Cortex, Amygdala, and Hippocampus, with reinforcement learning and decision-making algorithms.

## Features

- **Prefrontal Cortex**: Simulates decision-making and working memory.
- **Amygdala**: Simulates emotional responses based on input data.
- **Hippocampus**: Simulates memory storage and recall.
- **Q-learning**: A reinforcement learning algorithm for decision-making.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TheSpiralProgrammer/NeuroAI-Framework.git
   cd NeuroAI-Framework
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Creating the Full Brain System

```python
from neurobrain.brain_modules import FullBrain

brain = FullBrain(input_size=5, output_size=3)

# Test the decision-making process with emotions
emotion = "joy"
input_data = [0.8, 0.4, 0.7, 0.3, 0.2]
options = ['move_forward', 'turn_left', 'turn_right']
scores = [0.5, 0.2, 0.3]

decision = brain.think(input_data, emotion, options, scores)
print("Decision:", decision)
```

## License

This project is licensed under the MIT License.
