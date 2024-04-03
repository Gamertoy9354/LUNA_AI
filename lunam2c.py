import requests
import speech_recognition as sr
from gtts import gTTS
import os
import time
from googlesearch import search
from bs4 import BeautifulSoup
import sys
import threading
from playsound import playsound

language = 'en'
slow = False

r = sr.Recognizer()

def Speak(text):
    voice = "en-US-EmmaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "intro.mp3"'
    os.system(command)
    os.system("mpg123 intro.mp3")
    os.remove("intro.mp3")

Speak("Please enjoy the music while i prepare all the functions to use!")

def play_music(file_path):
    playsound(file_path)

def p1():
    time.sleep(1)
    Speak("conneting to the server")
    time.sleep(2)
    Speak("initialising the connection")
    time.sleep(1)
    Speak("sending report packets to the server")
    time.sleep(1)
    Speak("packets recieved")

if __name__ == "__main__":
    file_path = "/home/shis/Desktop/LunaAI/test/music.mp3"
  

    # Start playing the music in a separate thread
    music_thread = threading.Thread(target=play_music, args=(file_path,))
    music_thread.start()

    # Print messages while the music is playing
    p1()

    # Wait for the music thread to finish before exiting
    music_thread.join()

    Speak("initialisation completed")

def recognize_main(): #Main reply call function
    main_page = "https://en.wikipedia.org/wiki/Main_Page"
    r = sr.Recognizer() # sets r variable
    with sr.Microphone() as source: #sets microphone
        print("Say something!") #prints to screen
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #sets variable 'audio'
    data = "" #assigns user voice entry to variable 'data'
    try:
        data = r.recognize_google(audio) #now uses Google speech recognition
        data = data.lower() # makes all voice entries show as lower case
        if __name__ == "__main__":
            print("You said: " + data) #shows what user said and what was recognised
            if "luna" in data:
                Speak("Yes")
            if "exit" in data:
                exit
            if "info" in data:
                Speak("This is an AI that has access to Internet and can give result based on the information available online, Please keep this in mind that this AI takes information from directly wikipedia and shows it to you, Please keep this in mind that this AI is currently in it's BETA Stage so there might be some bugs")
            if "start" in data:
                Speak("There are currently four services that Luna offer you can select any one of them, Today's Article!,Today's Fact!,Today's News!,What happend today in history!")
            if "today's article" in data:
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    h21_element = soup.find("h2", id="mp-tfa-h2")
                    if h21_element:
                        Speak(h21_element.text.strip())  
                    else:
                        print("No <h2> element with id 'mp-tfa-h2' found.")

                print("")

                div1_element = soup.find("div", id="mp-tfa")
                if div1_element:
                    p1_tag = div1_element.find("p")
                if p1_tag:
                        Speak(p1_tag.text.strip())
        
            if "today's fact" in data:
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divf_element = soup.find("div", id="mp-dyk")
                    if divf_element:
                        ulf_element = divf_element.find("ul")
                    if ulf_element:
                        lif_tags = ulf_element.find_all("li")
                        print("Text content of the first three <li> tags within <ul>:")
                        for lif_tag in lif_tags[:7]:
                            Speak(lif_tag.text.strip())
                else:
                    print("Failed to retrieve webpage.")
            if "today's news" in data:
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divn_element = soup.find("div", id="mp-itn")
                    if divn_element:
                        uln_element = divn_element.find("ul")
                    if uln_element:
                        lin_tags = uln_element.find_all("li")
                        for lin_tag in lin_tags[:3]:
                            Speak(lin_tag.text.strip())
            if "what happened today in history" in data:
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    divd_element = soup.find("div", id="mp-otd")
                    if divd_element:
                        uld_element = divd_element.find("ul")
                    if uld_element:
                        lid_tags = uld_element.find_all("li")
                        for lid_tag in lid_tags[:5]:
                            Speak(lid_tag.text.strip())
        

            else:
                print("Please chose a correct option")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e: #whenever you have a try statement you have an exception rule
        Speak("Luna did not understand your request")



while 1: #This starts a loop so the speech recognition is always listening to you
    recognize_main() #calls first function 'start_recogniser