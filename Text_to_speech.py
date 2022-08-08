import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#speak("My Name is Mustafa Al-Saeed and I will be huge in the tech world")

speak("lets gooooooooooooooooo")
