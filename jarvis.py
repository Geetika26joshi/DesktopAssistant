import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('dummy')
engine=pyttsx3.init('sapi5')#for voice
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am selena . how may i help you?")   
def takeCommand():#it takes microphone input from user and outputs string
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening......")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognising...")   
        query=r.recognize_google(audio,language='en-in') 
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        speak("pardon me ma'am please repeat")
        print("pardon me please repeat")
        return"none"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp,gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('my gmail','my password')
    server.sendmail('geetika26joshi@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
   speak("hello ma'am")
   wishMe()
while True:
    query=takeCommand().lower()
    #logic on executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wiki')
        query = query.replace("wikipedia","")
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("Google.com")
    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play friends' in query:

        vdo_dir = 'C:\\Users\\nehajoshi\\Desktop\\FRIENDS\\S3'
        vdo=os.listdir(vdo_dir)
        os.startfile(os.path.join(vdo_dir,vdo[5]))
    elif 'geeks for geeks' in query:
        webbrowser.open("www.geeksforgeeks.org")
    elif 'amazon' in query:
        webbrowser.open("www.amazon.in")
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"ma'am the time is {strTime}")
    elif'open code' in query:
        code_path="C:\\Users\\nehajoshi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif'email to geetika' in query:
        try:
            speak("please tell the emai contain")
            content=takeCommand()
            to="reciever gmail"
            sendEmail(to,content)
            speak("email sent")
        except Exception as e:
            print(e)
            speak("sorry ma'am email not sent")

    elif 'bye' in query:
       speak("thank you ma'am have a good day")
       break