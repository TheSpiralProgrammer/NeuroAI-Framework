from neuroai.brain_modules.amygdala import Amygdala

def test_amygdala():
    amygdala = Amygdala(threshold=0.5)
    
    # Test for emotion based on input data
    input_data_fear = [0.8, 0.4, 0.7, 0.3, 0.2]
    emotion_fear = amygdala.process_emotion(input_data_fear)
    assert emotion_fear == "Fear", f"Expected 'Fear', but got {emotion_fear}"
    
    input_data_neutral = [0.2, 0.1, 0.3, 0.4]
    emotion_neutral = amygdala.process_emotion(input_data_neutral)
    assert emotion_neutral == "Neutral", f"Expected 'Neutral', but got {emotion_neutral}"
    
    print("Amygdala test passed successfully!")

test_amygdala()
