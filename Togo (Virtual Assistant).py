import pyttsx3 # text to speech converter, offline module
import datetime # to get the time
import wikipedia # to get something from wikipedia
import webbrowser # to work with browsers
import os # to deal with files and directories
import random # to generate random numbers
import speech_recognition as sr # it will understand and interpret the commands given by the user
import smtplib #used to send emails using gmail account

engine = pyttsx3.init('sapi5') # initialize puttsx3 with sapi(windows in biult speech recognition API)
voices = engine.getProperty('voices') # used to get the in built windows voices
engine.setProperty('voice',voices[1].id) # set the desired voice

def speak(audio):
    """
    This function converts the text into audio
    """
    engine.say(audio)
    engine.runAndWait()

def greetings():
    """
    This function greets the user according to time
    """
    hours = int(datetime.datetime.now().hour) # take the current time in hours
    if hours>0 and hours<12:
        speak("Good Morning Masab")
    elif hours>=12 and hours<18:
        speak("Good Afternoon Masab")
    else:
        speak("Good Evening Masab")
    speak("My name is TOGO and i am your virtual assistant. How may i help you sir?")

def takeCommand():
    """
    This function takes microphone input form the user and returns a string output
    """
    r = sr.Recognizer() # Recognizer() will recognize the input
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # ctrl+click
        audio = r.listen(source)
        try:
            #Recognizing the audio that is said by the user
            print("Recognizing.....")
            query = r.recognize_google(audio,language="en-us")
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            speak("Please say that again.....")
            return "None"
        return query
def sendEmail(to,content):
    """
    This function send mails using gmail account
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password') # enter your gmail and password here
    server.sendmail('your email id',to,content)
    server.close()

if __name__ == "__main__":
    greetings()
    while True:
        query = takeCommand().lower()
        # Logic to execute tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "E:\\SONGS"
            songs = os.listdir(music_dir)
            random_song = random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[random_song]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif 'open code' in query:
            vscodePath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        
        #You'll need to allow less secure apps in gmail to send the emails
        elif 'send email' in query:
            try:
                speak("Please say what do you want  to send")
                content = takeCommand()
                to = "email@gmail.com" # Type here the email id whom you want to send the email
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir! I am not able to send your email at the moment")
        elif 'how are you' in query:
            speak("I am doing great. it's a bit hot here. What about you?")
        elif 'fine' and 'good' in query:
            speak("Good to know that")
        elif 'thank you' in query:
            speak("Thank you Masab! Have a great day")
            break
        elif 'dick head' in query:
            speak("Ohhh! That is Sajjad Hameed")
        elif 'quit' in query:
            exit()
        