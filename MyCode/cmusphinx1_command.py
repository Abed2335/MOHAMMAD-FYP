import speech_recognition as sr
import pyautogui
import webbrowser
import subprocess


# Function to process commands
def process_command(command):
    command = command.lower()
    print(f"Recognized command: {command}")

    # Mouse clicks
    if "left click" in command:
        pyautogui.click()

    elif "right click" in command:
        pyautogui.click(button='right')

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
    elif "open browser" in command or "browser" in command:
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command or "youtube" in command:
        webbrowser.open("https://www.youtube.com")

    # Open calculator
    elif "open calculator" in command or "calculator" in command:
        subprocess.Popen("calc.exe")

    # Open camera
    elif "open camera" in command or "camera" in command:
        subprocess.Popen("start microsoft.windows.camera:", shell=True)

    else:
        print(f"Unknown command: {command}")


# Speech recognition setup
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Listening for commands... Say 'exit program' to stop.")

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Using CMU Sphinx offline recognition
        command = recognizer.recognize_sphinx(audio)
        print("You said:", command)

        if "exit program" in command.lower():
            print("Exiting...")
            break

        process_command(command)

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Sphinx error:", e)