import speech_recognition as sr
from gtts import gTTS
import os

# Language and speech speed
language = 'en'
slow = False

# Initialize recognizer
recognizer = sr.Recognizer()

# Text to be converted to speech
intro_text = "Hello, please say your name."
name_prompt_text = "Please say your name: "

# Speak the introduction
tts_intro = gTTS(text=intro_text, lang=language, slow=slow)
tts_intro.save("intro.mp3")
os.system("mpg123 intro.mp3")
os.remove("intro.mp3")

# Prompt the user for their name
print(name_prompt_text)

with sr.Microphone() as source:
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    name = recognizer.recognize_google(audio)
    print("You said:", name)
    
    # Speak the user's name
    say_name_text = f"Your name is {name}"
    tts_name = gTTS(text=say_name_text, lang=language, slow=slow)
    tts_name.save("name.mp3")
    os.system("mpg123 name.mp3")
    os.remove("name.mp3")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
