from neuroai.brain_modules.hippocampus import Hippocampus

def test_hippocampus():
    hippocampus = Hippocampus(memory_capacity=5)
    
    # Test storing and recalling memory
    input_data = [0.8, 0.4, 0.7, 0.3, 0.2]
    hippocampus.store_memory((input_data, "move_forward"))
    
    recalled_memory = hippocampus.recall_memory()
    assert recalled_memory == [(input_data, "move_forward")], f"Expected memory: {[(input_data, 'move_forward')]}, but got {recalled_memory}"
    
    print("Hippocampus test passed successfully!")
    
test_hippocampus()
