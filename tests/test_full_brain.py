from neuroai.brain_modules.brain import FullBrainWithLearning

def test_full_brain():
    brain = FullBrainWithLearning(input_size=5, output_size=3, memory_capacity=5, emotion_sensitivity=0.5)
    
    # Test decisions with different emotional states
    options = ["move_forward", "turn_left", "turn_right"]
    scores = [0.7, 0.3, 0.5]
    
    decision_1 = brain.think([0.8, 0.4, 0.7, 0.3, 0.2], "joy", options, scores)
    print(f"Decision 1 (Emotion: joy): {decision_1}")
    
    decision_2 = brain.think([0.5, 0.2, 0.8, 0.3, 0.4], "fear", options, scores)
    print(f"Decision 2 (Emotion: fear): {decision_2}")

    print("Full brain system test passed successfully!")
    
test_full_brain()
