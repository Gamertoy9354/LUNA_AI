import requests
import time
from googlesearch import search
from bs4 import BeautifulSoup
import os
import speech_recognition as sr
from gtts import gTTS

language = 'en'
slow = False

def speak (text):
    tts_intro = gTTS(text=text, lang=language, slow=slow)
    tts_intro.save("intro.mp3")
    os.system("mpg123 intro.mp3")
    os.remove("intro.mp3")



def listen (recognizer, audio):
    with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            mp3 = recognizer.listen(source)
    noise = mp3

    try:
         name = recognizer.recognize_google(mp3)
         print("you said", mp3)
    except sr.UnknownValueError:
         print("SRY didn't hear that")

    print(mp3)

listen()