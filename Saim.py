import pywhatkit
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser





listener=sr.Recognizer()
def returncom():

    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=0)
            print("Hy My Name Is Saim")
            print("How Can I Help You")
            print("Hy,I Am Listening.....")
            voice= listener.listen(source)
            command =listener.recognize_google(voice)
            command=command.lower()

            print(command)


    except:
        pass
    return command

def playsaim():
    command =returncom()
    if "play" in command:
        print("Playing ")
        pywhatkit.playonyt(command)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M:%S:%P")
        print("The Time Is"+ time)
    elif "wikipedia" in command:
        info=wikipedia.summary(command)
        print(info)

    elif "Joke" in command:
        print(pyjokes.get_jokes())
    elif f"open youtube" in command:
        webbrowser.open(f"https://www.youtube.com/")




playsaim()

