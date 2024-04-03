import threading
from playsound import playsound
import time

def play_music(file_path):
    playsound(file_path)

    

def p1():
    print("conneting to the server")
    time.sleep(4)
    print("initialising the connection")
    time.sleep(3)
    print("connection established")
    time.sleep(4)
    print("sending report packets to the server")
    time.sleep(6)
    print("packets recieved")

if __name__ == "__main__":
    file_path = "/home/shis/Desktop/LunaAI/test/music.mp3"

    # Start playing the music in a separate thread
    music_thread = threading.Thread(target=play_music, args=(file_path,))
    music_thread.start()

    # Print messages while the music is playing
    p1()

    # Wait for the music thread to finish before exiting
    music_thread.join()
