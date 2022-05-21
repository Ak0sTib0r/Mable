AIname = "Mable"

import tkinter as tk
import time
import pyautogui
import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import date, datetime 
engine = pyttsx3.init()

window = tk.Tk()

today = date.today()
Time = datetime.now()
current_time = Time.strftime("%H:%M")

functionIndex = "S"

rate = engine.getProperty("rate")
engine.setProperty("rate", 140)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("I'm listening.")
engine.runAndWait()

functionIndex = "L"

r = sr.Recognizer()

while(functionIndex == "L"):   
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration = 0.2)
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            inputText = MyText.split()

            #Date/Time
            for i in range(0, len(inputText)):
            	if inputText[i] == "insult":
            		engine.say(inputText[i+1])
            		engine.say("You are an absolute dumbass.")
            		engine.say("And you suck")
            		engine.runAndWait()
            		functiunIndex = "S"

            	if inputText[i] == "date":
            		engine.say("The date is")
            		engine.say(str(today))
            		engine.runAndWait()
            		functionIndex = "S"

            	if inputText[i] == "time":
            		engine.say("The time is")
            		engine.say(current_time)
            		engine.runAndWait()
            		functionIndex = "S"

            	if inputText[i] == "my" and inputText[i+1] == "email":
            		engine.say("Ok, opening your email.")
            		engine.runAndWait()
            		webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            		functionIndex = "S"

            	if inputText[i] == "calendar":
            		pyautogui.keyDown("Win")
            		pyautogui.keyDown("alt")
            		pyautogui.press("d")
            		pyautogui.keyUp("Win")
            		pyautogui.keyUp("alt")
            		functionIndex = "S"

            	if inputText[i] == "mable":
            		engine.say("Yes?")
            		engine.runAndWait()
            		functionIndex = "S"

            #Shut down
            if MyText == "shut down":
            	engine.say("Ok, shutting down.")
            	engine.runAndWait()
            	break

            #Search
            if inputText[0] == "search":
            	MyText = MyText.replace("search", "")
            	engine.say("Ok, here's what I found.")
            	engine.runAndWait()
            	webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://www.google.com/search?q="+MyText+"&oq="+MyText+"&aqs=chrome..69i57j35i39j46i199i465i512j0i512j46i199i465i512j69i61l3.1452j0j7&sourceid=chrome&ie=UTF-8")
            	functionIndex = "S"

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        import WakeMable
         
    except sr.UnknownValueError:
        print("unknown error occured")
        import WakeMable

if functionIndex == "S":
	import WakeMable

