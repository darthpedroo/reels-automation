from pydub import AudioSegment

# Load the audio file
sound = AudioSegment.from_file("Por qué las variables son como cajas de donas.mp3")  # Replace with your file path

# Shift the pitch down by half an octave
octaves = -0.5  # Negative value to lower the pitch
new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# Change the frame rate to the new lower sample rate
lower_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# Set the frame rate to 44.1kHz to ensure compatibility with standard players
lower_pitch_ready_to_export = lower_pitch_sound.set_frame_rate(44100)

# Export the modified audio
lower_pitch_ready_to_export.export('output_lower_pitch.mp3', format='mp3')

print("Pitch-lowered audio exported as 'output_lower_pitch.mp3'")
