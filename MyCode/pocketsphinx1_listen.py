from pocketsphinx import LiveSpeech

# Initialize live speech recognition with PocketSphinx
speech = LiveSpeech()

print("Listening...")

# Loop to continuously listen and print recognized text
for phrase in speech:
    print(f"Recognized text: {phrase}")
