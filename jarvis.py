import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import random
from requests import get
import time
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
engine.setProperty("rate",130)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



def wish():
    time.sleep(0.65)
    hour=int(datetime.datetime.now().hour)
    if(hour>=5 and hour<=12):
        speak("Good morning sir!")
    elif(hour>12 and hour<16):
        speak("Good afternoon sir!")
    elif(hour<19 and hour>16):
        speak("Good evening sir!")
    else:
        speak("Have great evening sir!")

    speak("I am Rubal. Please tell me how may I help you") 

if __name__=="__main__":
   wish()
   while True:
        
        query=takeCommand().lower()
        
        if"open notepad" in query:
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(path)
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", takeCommand())
            results = wikipedia.summary(query) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif"open whatsapp" in query:
            path="C:\\Users\\Siddheshsingh Tanwar\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(path)
        elif"open command prompt" in query:
            os.system("start cmd")

        elif"open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(58)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif("play music" or "play song") in query:
            # music_dir="C:\\Users\\Siddheshsingh Tanwar\\Music"
            # songs=os.listdir(music_dir)
            # # n=random.randint(0, 3)
            # # random = os.startfile(os.path.join(music_dir , songs[1]))
            # # rd=random.choice(songs)
            # # for song in rd:
            # #     if song.endswith(".mp3"):
            # #         os.startfile(os.path.join(music_dir,song))
            # os.startfile(os.path.join(music_dir,songs[0]))
            speak("sir,which song should i search on spotify")
            cm=takeCommand().lower()
            webbrowser.open("https://open.spotify.com/search/"+cm)
        elif"open youtube" in query :
            speak("sir,what should i search on youtube")
            cm=takeCommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query="+cm)
        elif"open google" in query :
            speak("sir,what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open("https://www.google.com/search?q="+cm)
        elif"smart box" in query:
            webbrowser.open("https://chat.openai.com")
            speak("Here sir you can get any kind of code or models of Machine Learning and AI . To get the code write the chat at bottom of page . There are the instructions and Limitation of this model.")



        

        


