import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os


friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

def speak(audio):
    print('Me: ' + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Meo!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Meo!")
        elif hour>=18 and hour<24:
            speak("Good Evening Meo")
        speak("How can I help you,Meo") 


def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=1
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("Ice: "+query)
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query

if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        #All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')

        elif "youtube" in query:
            speak("What should I search,boss")
            search=command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif "good bye" in query:
            speak("Ice is off. Goodbye Meo")
            quit()
        elif "open code" in query:
            code =r"C:\Users\MUN\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code)
        elif 'time' in query:
            time()