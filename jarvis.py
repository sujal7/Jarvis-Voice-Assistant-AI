import datetime
import os
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)         # prints the voices available in pc by default there are 2 (male & female)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis, your Virtual Assistant, created by Mr. Sujal Duwa. Please tell me how may I help you.")


def take_command():
    """
    Write doc string here
    It takes microphone input from user and returns string output
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "None"
    return query


def send_email(to, content):  # need to enable less secure apps in gmail to enable this feature
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sujalduwa@gmail.com", "your-password")
    server.sendmail("sujalduwa@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    greeting()
    while True:
        query = take_command().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("google.com")

        elif 'open github' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("github.com")

        elif 'open facebook' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("facebook.com")

        elif 'open instagram' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("instagram.com")

        elif 'open stackoverflow' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\Music"
            files = os.listdir(music_dir)
            music = []

            # Filters out mp3 files from other files
            for file in files:
                if file.endswith(".mp3"):
                    music.append(file)
            print(music)
            index = random.randint(0, len(music))   # Plays a random music from given folder
            os.startfile(os.path.join(music_dir, music[index]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to sujal' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "sujalduwa@gmail.com"
                send_email(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("I am not able to send this email at the moment.")

        elif 'quit' in query:
            speak("Thank you for using Jarvis. See you again soon sir.")
            exit(1)
