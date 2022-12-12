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
import sys
import pyjokes
import smtplib



chrome_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 130)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takeCommand():
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
        speak("speak again")
        return exit()
    return query

def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" +  hour  + "Hours and" +  min  + "Minutes")



def wish():
    time.sleep(0.65)
    hour = int(datetime.datetime.now().hour)
    if (hour >= 5 and hour <= 12):
        speak("Good morning" + name)
    elif (hour > 12 and hour < 16):
        speak("Good afternoon" + name)
    elif (hour < 19 and hour > 16):
        speak("Good evening " + name)
    else:
        speak("Have great evening " + name)

    speak("I am Alexis, your personal voice assistant. Please tell me how may I help you")


if __name__ == "__main__":
    speak("What's your name,dear user ?")
    name = takeCommand().lower()

    wish()
    while True:

        query = takeCommand().lower()

        if "open notepad" in query:
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Wordpad.lnk"
            os.startfile(path)
            break

        elif "wikipedia" in query or "search wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", takeCommand())
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open whatsapp" in query:
            path = "https://web.whatsapp.com/"
            os.startfile(path)
            break

        elif "open cmd" in query:
            os.system("start cmd")
            break

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            # while True:
            ret, img = cap.read()
            cv2.imshow("webcam", img)
            cv2.waitKey(5)
            speak("Press any key to close camera")
            #     if k == 10:
            #         break
            # cap.release()
            # cv2.destroyAllWindows()

        elif ("search music" or "search song") in query:
            # music_dir="C:\Users\krish\Music"
            # songs=os.listdir(music_dir)
            # n=random.randint(0, 3)
            # random = os.startfile(os.path.join(music_dir , songs[1]))
            # rd=random.choice(songs)
            # for song in rd:
            #     if song.endswith(".mp3"):
            #         os.startfile(os.path.join(music_dir,song))
            # os.startfile(os.path.join(music_dir,songs[0]))
            speak("Opening Spotify")
            speak("Sir,which song should I search on Spotify")
            cm = takeCommand().lower()
            webbrowser.open("https://open.spotify.com/search/" + cm)
            break

        elif "open youtube" in query:
            speak("sir,what should i search on youtube")
            cm = takeCommand().lower()
            webbrowser.open("https://www.youtube.com/results?search_query=" + cm)
            break

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open("https://www.google.com/search?q=" + cm)
            break

        elif "smart box" in query:
            webbrowser.open("https://chat.openai.com")
            speak(
                "Here sir you can get any kind of code or models of Machine Learning and AI ."
                " To get the code write the chat at bottom of page . There are the instructions and Limitation of this model.")
            break

        elif "open music player" in query:
            path = "C:\Program Files\Windows Media Player"
            os.startfile(path)
            break

        elif "today" in query:
            tellDay()

        elif "what time" in query:
            tellTime()


        elif "who made you" in query or "created you" in query:

            cr = "I have been created by Samarth and Chetan"
            speak(cr)

        elif ("define yourself" or "who are you") in query:
           about= "Hello, I am Person. Your personal Assistant.I am here to make your life easier. " \
                  "You can command me to perform various " \
                  "tasks such as i will tell you the exact date or time or opening applications etcetra"
           speak(about)

        elif "exit"in query or "close" in query:
            speak("have a good day dear")
            sys.exit()

        elif "jokes" in query or "tell me jokes" in query:
            myjokes=pyjokes.get_jokes(language='en',category='neutral')
            speak(myjokes)

        elif "joke" in query or "tell me a joke" in query :
            myjoke=pyjokes.get_joke(language='en',category='neutral')
            speak(myjoke)
            break

        elif "powerpoint" in query or "open powerpoint" in query :
            speak("Opening powerpoint")
            path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(path)
            break

        elif "Word" in query or "open Micrsoft Word" in query :
            speak("Opening Word")
            path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(path)
            break

        elif "google drive" in query or "open google drive" in query :
            speak("Opening Google Drive")
            path="https://drive.google.com/"
            os.startfile(path)
            break

        elif "excel" in query or " open Microsoft excel" in query :
            speak("Opening Microsoft Excel")
            path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(path)
            break

        elif 'news' in query :
            speak("Which newspaper do you want to read. Please say the name")
            print("The Times OF India \nThe Indian Express \nIndia Today \nNDTV \nThe Hindu \nHindustan Times")
            cm=takeCommand().lower()
            if "The Times of India" in cm:
                speak("Here is the latest news from Times of India")
                webbrowser.open("https://timesofindia.indiatimes.com/")

            elif "The Indian Express" in cm:
                speak("Here is the latest news from The Indian Express")
                webbrowser.open("https://indianexpress.com/")
                break
            elif "India today" in cm:
                speak("Here is the latest news from India Today")
                webbrowser.open("https://www.indiatoday.in/")
                break
            elif "NDTV" in cm:
                speak("Here is the latest news from NDTV")
                webbrowser.open("https://www.ndtv.com/")
                break
            elif ("The Hindu" or "Hindu") in cm:
                    speak("Here is the latest news from The Hindu")
                    webbrowser.open("https://www.thehindu.com/")
                    break
            elif "Hindustan times" in cm:
                speak("Here is the latest news from Hindustan Times")
                webbrowser.open("https://www.hindustantimes.com/")
                break

        elif "Gmail" in query or "open mail" in query:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com/mail/")
            break


        else:
            speak("I am sorry user but this word is not a command. Do you want me to search this on Google. Say Yes or No")
            cm = takeCommand().lower()
            if "yes" in cm:
                webbrowser.open("https://www.google.com/search?q=" + query)
                break
            else:
                speak("Try saying something else")
                continue



        

        


