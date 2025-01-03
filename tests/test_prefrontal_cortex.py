import numpy as np
from neuroai.brain_modules.cortex import PrefrontalCortex

def test_prefrontal_cortex():
    cortex = PrefrontalCortex(input_size=5, output_size=3, memory_capacity=5)
    test_input = [0.8, 0.4, 0.7, 0.3, 0.2]
    output = cortex.neuron_activation(test_input)
    
    assert len(output) == 3, f"Expected output size 3, but got {len(output)}"
    print("Prefrontal Cortex test passed successfully!")
    
test_prefrontal_cortex()
