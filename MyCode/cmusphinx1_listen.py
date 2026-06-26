import speech_recognition as sr

# create recognizer
r = sr.Recognizer()

# use microphone
with sr.Microphone() as source:
    print("Speak something...")

    # record audio
    audio = r.listen(source)

    print("Processing...")

    try:
        # offline recognition using sphinx
        text = r.recognize_sphinx(audio)

        print("You said:")
        print(text)

    except Exception as e:
        print("Error:", e)