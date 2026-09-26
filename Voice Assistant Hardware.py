# Voice Assistant Hardware using Python

# Install required libraries:

# pip install SpeechRecognition PyAudio pyttsx3

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize voice engine

engine = pyttsx3.init()

engine.setProperty("rate", 150)

def speak(text):
print("Assistant:", text)
engine.say(text)
engine.runAndWait()

def listen():
recognizer = sr.Recognizer()

```
with sr.Microphone() as source:
    print("\nListening...")
    recognizer.adjust_for_ambient_noise(
        source,
        duration=1
    )

    try:
        audio = recognizer.listen(
            source,
            timeout=5
        )

        command = recognizer.recognize_google(
            audio
        )

        print("You:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No voice detected.")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
```
