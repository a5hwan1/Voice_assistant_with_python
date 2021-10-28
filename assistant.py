import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir")
    elif hour>=12 and hour<5:
        speak("Good afternoon sir")
    else:
        speak("good evening sir")

    speak("Hello,I am your Jarvis.What can i do for you Sir")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    volume = engine.getProperty('volume')
    print(volume)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',175)
    print(rate)
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "thanks" in query:
            speak("Never mind sir")
        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is")
            speak(strtime)
        elif ("open youtube" in query) or ("youtube" in query):
            webbrowser.open("www.youtube.com")
        elif ("open facebook" in query) or ("facebook" in query):
            webbrowser.open("www.facebook.com")
        elif ("open instagram" in query) or ("instagram" in query):
            webbrowser.open("www.instagram.com")
        elif "open hackerrank" in query:
            webbrowser.open("www.hackerrank.com")
        elif "open hackerone" in query:
            webbrowser.open("www.hackerone.com")
        elif "open flipcart" in query:
            webbrowser.open("www.flipcart.com")
        elif ("open google" in query) or ("google" in query):
            webbrowser.open("www.google.com")

        elif "open pycharm " in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe"
            os.startfile(path)
        elif "open burp suite" in query:
            path = "C:\\Users\\Batukeshwar\\Downloads\\burpsuite_pro_windows-x64_v2020_7.exe"
            os.startfile(path)
