# Import Packages
import pyttsx3
import speech_recognition as sr
import subprocess
# from Features import YoutubeSearch
import Features
# =============================================

# Changing Assistant Sound to Female
Engine = pyttsx3.init()
Voices = Engine.getProperty("voices")
Engine.setProperty("voice", Voices[1].id)
Engine.setProperty('rate',170)


# Speak Function For Command


def Speak(Command):
    Engine.say(Command)
    Engine.runAndWait()


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        Query = r.recognize_google(audio)
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return Query.lower()
    except:
        return ""
# Speak("Hello World");
# Listen();


def Tasks():
    Results = Listen()

    if "youtube search" in Results:
        Tokenize = Results.replace("youtube search", "")
        Features.YoutubeSearch(Tokenize)
    elif "google search" in Results:
        Tokenize = Results.replace("google search", "")
        Features.GoogleSearch(Tokenize)
    elif "download this video" in Results:
        Features.DownloadVideo();
    elif "test internet speed" in Results:
        Features.SpeedTest();
    elif "calculate" in Results:
        Tokenize = Results.replace("calculate", "")
        Tokenize=Tokenize.replace("divided by","/")
        Tokenize=Tokenize.replace("x","*")
        Features.Calculator(Tokenize)
    elif "whatsapp message" in Results:
        Speak("Tell The Recipient Name");
        Name=Listen();
        print(f"User Name Is : {Name}")
        Speak("Record Your Message")
        Message=Listen();
        print(f"Message Is : {Message}")
        Features.WhatsappMessage(Name,Message)
    elif "open" in Results:
        Tokenize=Results.replace("open","");
        Features.RunProgramme(Tokenize)
    elif "" in Results:
        return ""
    else:
        Speak("Google Speech Recognition Could Not Understand Audio or May Be Network Issue")

while 1:
        Tasks()