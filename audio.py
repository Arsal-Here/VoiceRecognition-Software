import speech_recognition as sr
import pyttsx3
import os 
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing")
        command = recognizer.recognize_google(audio)
        print(f"User said {command}")
    except sr.UnknownValueError:
        print("I did not understand that")
        return None
    except sr.RequestError:
        print("Server error")
        return None
    
    return command.lower()

def recognize(command):
    if 'hi' in command:
        speak('Hello')
    elif 'bye' in command:
        speak('Goodbye')
        exit()
    elif 'open' in command: 
        if 'chrome' in command:
            speak('Opening Chrome')
            os.system('start chrome')  

    elif 'search' in command:
        speak("What do you want to search?")
        search = take_command()
        webbrowser.open(f"https://www.google.com/search?q={search}")
    else:
        speak('I did not understand that')


def run_program():
    speak("Hello how may i help you?")
    while True:
        command = take_command()
        if command:
            recognize(command)

run_program()

    

