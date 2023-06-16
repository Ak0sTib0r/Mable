import webbrowser
import pyautogui
from datetime import date, datetime
import subprocess as program
import os
import TimeModule
import json

today = date.today()
Time = datetime.now()
current_time = Time.strftime("%H:%M")

browser = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')

programFile = open("Programs.json")
programs = json.load(programFile)

responseFile = open("Settings.json")
responses = json.load(responseFile)

def SetATimer(duration):
    timer = TimeModule.Timer(duration)
    timer.SetTimer()

def OpenProgram(exe):
    program.Popen(programs[exe])

def PlayVideosBy(text: str):
    text = text.replace(" ", "")
    channelPage = f"https://www.youtube.com/@{text}"
    browser.open(channelPage)

def GetNews():
    browser.open("https://www.bbc.co.uk/news")

def GetWeather():
    browser.open("https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j35i39j46i199i465i512j0i512j46i199i465i512j69i61l3.1452j0j7&sourceid=chrome&ie=UTF-8")

def GetDate():
    print(f"The date is {str(today)}")

def GetTime():
    print(f"The time is {current_time}") 

def OpenMail():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def ShowCalendar():
    pyautogui.keyDown("Win")
    pyautogui.keyDown("alt")
    pyautogui.press("d")
    pyautogui.keyUp("Win")
    pyautogui.keyUp("alt")

def VisitSite(domainName):
    browser.open(f"https://www.{domainName.lower()}.com/")
