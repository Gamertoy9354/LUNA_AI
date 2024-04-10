import requests
import speech_recognition as sr
import os
import time
from googlesearch import search
from bs4 import BeautifulSoup
import sys
import threading
from playsound import playsound
from cryptography.fernet import Fernet
from gtts import gTTS
from googleapiclient.discovery import build
import subprocess
import spacy
from spacy.matcher import Matcher

API_KEY = 'AIzaSyBXjm4RzjzplYTL2sNPVvqyrZ1cMjt8_QE'
PLAYLIST_ID = 'PLaQPXATbDPkKU8bnOQdvCx9OjesE0ZZ5w'

language = 'en'
slow = False

def Speak(text):
    voice = "en-US-EmmaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "intro.mp3"'
    os.system(command)
    os.system("mpg123 intro.mp3")
    os.remove("intro.mp3")

# Generate a key
key = b'2AbgwdSql-1lzi0u6RN56G8PH7ALq4db84SnfpnGMeA='
cipher_suite = Fernet(key)

with open('/home/shis/Desktop/LunaAI/test/password_file.txt', 'r') as file:
    # Read the password from the file
    password = file.readline().strip()

password_bytes = password.encode()

decrypted_text = cipher_suite.decrypt(password_bytes)

decpass = decrypted_text.decode()

print("Please enter the password to continue: ")
Speak("Please enter the password to continue: ")
upass = str(input())
def internet_test():
    try:
        response = requests.get("https://google.com", timeout=5)
        response.raise_for_status() 
        print("You have network connection!")
    except requests.exceptions.RequestException as e:
        print("YOU DON'T HAVE NETWORK CONNECTION! or you think this is wrong please request an issue on our github!")
        sys.exit()
internet_test()
if upass == decpass:
    Speak("Welcome Back Sir! it's Luna,")
    Speak("Please enjoy the music while i prepare all the functions to use!")

    def play_music(file_path):
        playsound(file_path)

    def p1():
        time.sleep(1)
        Speak("connecting to the server")
        time.sleep(2)
        Speak("initializing the connection")
        time.sleep(1)
        Speak("sending report packets to the server")
        time.sleep(1)
        Speak("packets received")

    if __name__ == "__main__":
        file_path = "/home/shis/Desktop/LunaAI/test/music.mp3"
        # Start playing the music in a separate thread
        music_thread = threading.Thread(target=play_music, args=(file_path,))
        music_thread.start()

        # Print messages while the music is playing
        p1()

        # Wait for the music thread to finish before exiting
        music_thread.join()

        Speak("initialization completed")
        def get_weather(city):
            api_key = '5e2d19aa35f844b2a3c105236240504'  # Replace 'YOUR_API_KEY' with your actual API key
            url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
            response = requests.get(url)
            data = response.json()
            if 'error' not in data:
                weather_description = data['current']['condition']['text']
                temperature = data['current']['temp_c']
                return f'Today\'s weather is: {weather_description}, and Temperature is: {temperature}°C'
            else:
                print('Failed to fetch weather data with error code: 678EC please use this code in your github issue request!')
                Speak('Failed to fetch weather data with error code: 678EC please use this code in your github issue request!')


        if __name__ == "__main__":
            city = "Ahmedabad"
            print(get_weather(city))

        Speak("I am now listning!")

    def NaturalLanguageProccessor(data):
            nlp = spacy.load('en_core_web_sm')
            matcher = Matcher(nlp.vocab)

            article_pattern = [{'LOWER': 'today'}, {'LOWER': "'s"}, {'LOWER': 'article'}]
            weather_pattern = [{'LOWER': 'today'}, {'LOWER': "'s"}, {'LOWER': 'weather'}]
            fact_pattern = [{'LOWER': 'today'}, {'LOWER': "'s"}, {'LOWER': 'fact'}]
            News_pattern = [{'LOWER': 'today'}, {'LOWER': "'s"}, {'LOWER': 'news'}]
            history_pattern = [{'LOWER': 'today'}, {'LOWER': "in"}, {'LOWER': 'history'}]
            Study_pattern = [{'LOWER': 'enable'}, {'LOWER': "study"}, {'LOWER': 'mode'}]
            sleep_pattern = [{'LOWER': 'sleep'}]
            mute_pattern= [{'LOWER': 'mute'}]
            exit_pattern = [{'LOWER': 'exit'}]

            matcher.add('TodayArticle', [article_pattern])
            matcher.add('TodayWeather', [weather_pattern])
            matcher.add('TodayFact', [fact_pattern])
            matcher.add('TodayNews', [News_pattern])
            matcher.add('TodayInHistory', [history_pattern])
            matcher.add('Study', [Study_pattern])
            matcher.add('Sleep', [sleep_pattern])
            matcher.add('Mute', [mute_pattern])
            matcher.add('Exit', [exit_pattern])
            doc = nlp(data)
            matches = matcher(doc)
            for match_id, start, end in matches:
                if nlp.vocab.strings[match_id] == 'TodayArticle':
                    return "today's article"
                elif nlp.vocab.strings[match_id] == 'Exit':
                    return "exit"
                elif nlp.vocab.strings[match_id] == 'Study':
                    return "enable study mode"
                elif nlp.vocab.strings[match_id] == 'Sleep':
                    return "sleep"
                elif nlp.vocab.strings[match_id] == 'Mute':
                    return "mute"
                elif nlp.vocab.strings[match_id] == 'TodayWeather':
                    return "today's weather"
                elif nlp.vocab.strings[match_id] == 'TodayFact':
                    return "today's fact"
                elif nlp.vocab.strings[match_id] == "TodayNews":
                    return "today's news"
                elif nlp.vocab.strings[match_id] == "TodayInHistory":
                    return "today in history"
                else:
                    return "error"
            return None
    def recognize_main(): #Main reply call function
        main_page = "https://en.wikipedia.org/wiki/Main_Page"
        r = sr.Recognizer() # sets r variable
        with sr.Microphone() as source: #sets microphone
            print("recognizer initialzied")
            print("Say something!") #prints to screen
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) #sets variable 'audio'
        data = "" #assigns user voice entry to variable 'data'
        try:
            data = r.recognize_google(audio) #now uses Google speech recognition
            data = data.lower() # makes all voice entries show as lower case
            Aanalp = NaturalLanguageProccessor(data)
            print("You said: " + data) #shows what user said and what was recognised
            if "today's article" in Aanalp:
                response = requests.get(main_page)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    h21_element = soup.find("h2", id="mp-tfa-h2")
                    if h21_element:
                        Speak(h21_element.text.strip())  
                    else:
                        print("No <h2> element with id 'mp-tfa-h2' found. with error code: 356EC please use this code in your github issue request!")
                        Speak("No <h2> element with id 'mp-tfa-h2' found. with error code: 356EC please use this code in your github issue request!")

                    div1_element = soup.find("div", id="mp-tfa")
                    if div1_element:
                        p1_tag = div1_element.find("p")
                    if p1_tag:
                        Speak(p1_tag.text.strip())
                else:
                    print("The program has faced an error with error code: 356EC please use this code in your github issue request!")
                    Speak("The program has faced an error with error code: 356EC please use this code in your github issue request!")
            if "today's weather" in Aanalp:
                def get_weather(city):
                    api_key = '5e2d19aa35f844b2a3c105236240504'  
                    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
                    response = requests.get(url)
                    datawq = response.json()
                    if 'error' not in datawq:
                        weather_description = datawq['current']['condition']['text']
                        temperature = datawq['current']['temp_c']
                        return f'Today\'s weather is: {weather_description}, and Temperature is: {temperature}°C'
                    else:
                        print('Failed to fetch weather data with error code: 678EC please use this code in your github issue requesst!')
                        Speak('Failed to fetch weather data with error code: 678EC please use this code in your github issue request!')
                        return 'Failed to fetch weather data'
                if __name__ == "__main__":
                    city = "Ahmedabad"
                    Speak(get_weather(city))
            if "today's fact" in Aanalp:
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
                        print("Failed to find fact list with error code: 248EC please use this code in your github issue request!")
                        Speak("Failed to find fact list with error code: 248EC please use this code in your github issue request!")
                else:
                    print("Failed to retrieve webpage. or service does not exists error code: 248EC please use this code in your github issue request!")
                    Speak("Failed to retrieve webpage. or service does not exists error code: 248EC please use this code in your github issue request!")
            if "today's news" in Aanalp:
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
                    else:
                        Speak("luna AI was unable to find the news article with error code:776EC Please use this code in your github issue request!")
                        print("luna AI was unable to find the news article with error code:776EC Please use this code in your github issue request!")
                else:
                    print("Luna Ai has failed to fetch the news with error code:776EC Please use this code in your github issue request!")
                    Speak("Luna Ai has failed to fetch the news with error code:776EC Please use this code in your github issue request!")
            if "today in history" in Aanalp:
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
                    print("Luna AI was unable to fetch data with error code:893EC PLease use this code in your github issue request!")
                    Speak("Luna AI was unable to fetch data with error code:893EC PLease use this code in your github issue request!")
            if "enable study mode" in Aanalp:
                Speak("yes sir, enabling study mode and good luck with your study!")
                def start_youtube_music_playlist():
                    youtube = build('youtube', 'v3', developerKey=API_KEY)
                    playlist_items = youtube.playlistItems().list(
                    part='snippet',
                    playlistId=PLAYLIST_ID,
                    maxResults=1
                    ).execute()
                    video_id = playlist_items['items'][0]['snippet']['resourceId']['videoId']
                    playlist_url = f'https://music.youtube.com/watch?v={video_id}&list={PLAYLIST_ID}'
                    import subprocess
                    subprocess.Popen(["xdg-open", playlist_url])
                start_youtube_music_playlist()
            if "sleep" in Aanalp:
                import os
                def put_to_sleep():
                    Speak("ok sir on it!")
                    os.system("systemctl suspend")
                put_to_sleep()
            if "mute" in Aanalp:
                Speak("ok sir on it!")
                def mute_speakers():
                    subprocess.run(["amixer", "-q", "set", "Master", "mute"])

                mute_speakers()
            elif "unmute" in data:
                
                def unmute_speakers():
                    subprocess.run(["amixer", "-q", "set", "Master", "unmute"])
                    Speak("your speaker has been unmuted!")
                unmute_speakers()
            
            if "error" in Aanalp:
                print("This error might have  acured because there are not serices like",data,"or luna might have not heard that well plese request an issue on the github repository with error code: 346EC")
                Speak("This error might have  acured because there are not serices like",data,"or luna might have not heard that well plese request an issue on the github repository with error code: 346EC")

            if "NONE" in data or not any(keyword in data for keyword in ["luna", "info", "start", "today's article", "today's fact", "today's news", "what happened today in history", "enable study mode","mute", "unmute","exit","today's weather"]):
                def search_wikipedia(data):
                    wikipedia_urls = [url for url in search(data, num=10, stop=10) if "https://en.wikipedia.org/wiki/" in url]
                    return wikipedia_urls[0] if wikipedia_urls else None
                wikipedia_result = search_wikipedia(data)
                if wikipedia_result:
                    url = wikipedia_result
                    response = requests.get(url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")
    
                        div_element = soup.find("div", id="mw-content-text")
                        if div_element:
                            div2_lement = div_element.find("div")
                            print("found DIV 2!")
                            if div2_lement:
                                p_tags = div2_lement.find_all("p")
                                print("Text content of the first three <p> tags within <div id='mp-tfa'>:")
                                for p_tag in p_tags[:3]:
                                    Speak(p_tag.text.strip())
                            else:
                                print("NO <p> tag sorry for inconvinience with error code:459EC")
                        else:
                            print("no <div> tag found sorry for the inconvinience with error code: 459EC")
                    else:
                        print("Failed to retrieve webpage with error code: 459EC Please use this code in your github issue request!")
                        Speak("Failed to retrieve webpage with error code: 459EC Please use this code in your github issue request!")
                else:
                    print("No Wikipedia page found for the given query or you think that this is wrong please use error code: 459EC in your github issue request!")
                    Speak("No Wikipedia page found for the given query or you think that this is wrong please use error code: 459EC in your github issue request!")
            if "exit" in Aanalp:
                Speak("GoodBye!")
                sys.exit()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
    while 1: 
        recognize_main() 