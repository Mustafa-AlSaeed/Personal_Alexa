import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import random
import requests
import pyjokes

# from this line till

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to this line is the text to speech part

#from this line till


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alex: Listening...")
        audio=r.listen(source)
        try:    
            query = r.recognize_google(audio)
            print(f"master:{query}")
            return query
        except:
            print("Try Again")
# till this line is the speech to text

while True:
    query = command().lower() #this takes the users command

    if 'name' in query:
        speak("Hello Oday! I am Jake. Your personal assistant")

    #time
    elif "time" in query:
         time = datetime.datetime.now().strftime('%I:%M %p')
         speak("current time is " + time)

    #day
    elif "day" in query:
        day = datetime.datetime.today().weekday()+1

        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            speak("today is "+ day_of_the_week)

    #date
    elif "date" in query:
        current_date = datetime.datetime.now()
        speak("current date is"+str(current_date.month)+str(current_date.day)+str(current_date.year))
            


    elif "bye" in query:
        speak("Have a good day")
        break
