import queue
import subprocess
import webbrowser
import sounddevice as sd
import json
import pyautogui
from vosk import Model, KaldiRecognizer

# Path to your downloaded Vosk model
MODEL_PATH = r"C:\Users\moham\PycharmProjects\PythonProject4"

# Load Vosk model
model = Model(MODEL_PATH)

# Audio settings
samplerate = 16000
q = queue.Queue()

# Initialize recognizer
recognizer = KaldiRecognizer(model, samplerate)


# Audio callback
def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))


# Function to process commands
def process_command(command):
    command = command.lower()
    print(f"Recognized command: {command}")

    # Mouse clicks
    if "left click" in command:
        pyautogui.click()

    elif "right click" in command:
        pyautogui.click(button="right")

    elif "double click" in command:
        pyautogui.doubleClick()

    # Mouse movement
    elif "move up" in command:
        pyautogui.moveRel(0, -100)

    elif "move down" in command:
        pyautogui.moveRel(0, 100)

    elif "move left" in command:
        pyautogui.moveRel(-100, 0)

    elif "move right" in command:
        pyautogui.moveRel(100, 0)

    # Scrolling
    elif "scroll up" in command:
        pyautogui.scroll(300)

    elif "scroll down" in command:
        pyautogui.scroll(-300)

    # Open browser
    elif "open browser" in command:
        subprocess.Popen("start chrome", shell=True)

    # Close browser
    elif "close browser" in command:
        subprocess.Popen("taskkill /f /im chrome.exe", shell=True)

    # Open YouTube
    elif "open" in command and (
        "youtube" in command or "you tube" in command or "you too" in command
    ):
        webbrowser.open("https://www.youtube.com")

    # Close YouTube
    elif "close" in command and (
        "youtube" in command or "you tube" in command or "you too" in command
    ):
        subprocess.Popen("taskkill /f /im chrome.exe", shell=True)

    # Open calculator
    elif "open calculator" in command:
        subprocess.Popen("calc.exe")

    # Close calculator
    elif "close calculator" in command:
        subprocess.Popen("taskkill /f /im CalculatorApp.exe", shell=True)

    # Open camera
    elif "open camera" in command:
        subprocess.Popen("start microsoft.windows.camera:", shell=True)

    # Capture photo
    elif "capture" in command:
        pyautogui.press("enter")

    # Close camera
    elif "close camera" in command:
        subprocess.Popen("taskkill /f /im WindowsCamera.exe", shell=True)

    # Volume control
    elif "volume up" in command:
        pyautogui.press("volumeup")

    elif "volume down" in command:
        pyautogui.press("volumedown")

    elif "mute" in command:
        pyautogui.press("volumemute")

    # Unknown command
    else:
        print(f"Unknown command: {command}")


# Start microphone stream
with sd.RawInputStream(
    samplerate=samplerate,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=callback,
):
    print("Listening offline with Vosk...")

    while True:
        data = q.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())

            if "text" in result:
                command = result["text"]

                if command.strip() != "":
                    process_command(command)