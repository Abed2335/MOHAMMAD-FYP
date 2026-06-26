from pocketsphinx import LiveSpeech
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
    elif " up" in command:
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


# Start live speech recognition
print("Listening for commands... Say 'exit program' to stop.")

speech = LiveSpeech()

for phrase in speech:
    command = str(phrase)

    if "exit program" in command.lower():
        print("Exiting...")
        break

    process_command(command)