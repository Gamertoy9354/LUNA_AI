import os

def speak(text):
    voice = "ar-DZ-AminaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "intro.mp3"'
    os.system(command)
    os.system("mpg123 intro.mp3")
    os.remove("intro.mp3")

speak("hey there")
