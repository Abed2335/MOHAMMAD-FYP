import sounddevice as sd
import queue
import json
import vosk

# Set path to the VOSK model
VOSK_MODEL_PATH = r"C:\Users\moham\PycharmProjects\PythonProject4"
# Load VOSK model
model = vosk.Model(VOSK_MODEL_PATH)
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize a queue to collect audio data
audio_queue = queue.Queue()

# Audio callback function to put data into the queue
def callback(indata, frames, time, status):
    audio_queue.put(bytes(indata))

# Start the microphone input stream
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")

    while True:
        data = audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            if text:
                print(f"Recognized text: {text}")
