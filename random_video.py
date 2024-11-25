from TTS.api import TTS

# Load pre-trained model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True)

# Generate speech
tts.tts_to_file(text="Hello, this is a test", file_path="output.wav")
