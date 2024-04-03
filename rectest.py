import speech_recognition as sr

r = sr.Recognizer()

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
        print("You said: " + data) #shows what user said and what was recognised
        if "luna" in data:
            print("Yes")
        if "info" in data:
            print("This is an AI that has access to Internet and can give result based on the information available online, Please keep this in mind that this AI takes information from directly wikipedia and shows it to you, Please keep this in mind that this AI is currently in it's BETA Stage so there might be some bugs")
        if "start" in data:
            print("There are currently four services that Luna offer you can select any one of them, Today's Article!,Today's Fact!,Today's News!,What happend today in history!")
            print(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e: #whenever you have a try statement you have an exception rule
        print("Luna did not understand your request")

while 1: #This starts a loop so the speech recognition is always listening to you
    recognize_main()