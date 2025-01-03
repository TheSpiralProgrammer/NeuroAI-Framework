
# Usage Guide for NeuroAI Framework

This guide provides an overview of how to use the various components of the **NeuroAI Framework**.

## Full Brain System

The **Full Brain System** combines the key modules (Prefrontal Cortex, Amygdala, and Hippocampus) into a complete brain simulation. You can make decisions based on sensory input, emotional states, and memory.

### Example: Using the Full Brain

```python
from neurobrain.brain_modules import FullBrain

# Initialize the full brain system
brain = FullBrain(input_size=5, output_size=3)

# Define the options and their scores for decision-making
emotion = "joy"
input_data = [0.8, 0.4, 0.7, 0.3, 0.2]
options = ['move_forward', 'turn_left', 'turn_right']
scores = [0.5, 0.2, 0.3]

# Make a decision based on the input and emotional state
decision = brain.think(input_data, emotion, options, scores)
print("Decision:", decision)
```

## Prefrontal Cortex

The **Prefrontal Cortex** simulates decision-making and working memory. It receives input data and makes decisions based on current scores.

### Example: Using the Prefrontal Cortex

```python
from neurobrain.brain_modules import PrefrontalCortex

cortex = PrefrontalCortex(input_size=5, output_size=3)

# Add an item to working memory
cortex.add_to_memory([0.8, 0.4, 0.7, 0.3, 0.2])

# Make a decision based on input scores
options = ['move_forward', 'turn_left', 'turn_right']
scores = [0.5, 0.2, 0.3]
decision = cortex.decide(options, scores)
print("Decision:", decision)
```

## Amygdala

The **Amygdala** processes emotional input based on a threshold. It assigns emotions like fear or joy to the decision-making process.

### Example: Using the Amygdala

```python
from neurobrain.brain_modules import Amygdala

amygdala = Amygdala(threshold=0.7)

# Process emotion based on input data
emotion = amygdala.process_emotion([0.9, 0.5, 0.7])
print("Emotion:", emotion)
```

## Hippocampus

The **Hippocampus** stores and recalls memory. It simulates the brain's long-term memory and can be used for episodic memory recall.

### Example: Using the Hippocampus

```python
from neurobrain.brain_modules import Hippocampus

hippocampus = Hippocampus(memory_capacity=5)

# Store a new memory
hippocampus.store_memory(([0.8, 0.4, 0.7, 0.3, 0.2], 'move_forward'))

# Recall a memory
memory = hippocampus.recall_memory()
print("Memory:", memory)
```
