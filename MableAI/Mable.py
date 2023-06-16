import os
import time
import pyautogui
import webbrowser
import speech_recognition as sr
import pyttsx3
from datetime import date, datetime 
import settingsReader
import pyodbc
import pandas
from nltk import LancasterStemmer
import NLPS
import queryCat

#================================ Creating NLP System's Class (NLPSC) ================================
class NLPSystem:
	def __init__(self, speech):
		self.speech = speech

	#Tokenisation
	def Tokenise(self):
		self.tokenisedText = self.speech.split()
		print(self.tokenisedText)

	#Stemming
	def Stem(self):
		stemmer = LancasterStemmer()
		for self.word in self.tokenisedText:
			self.stemmedWord = stemmer.stem(self.word)
			print(self.stemmedWord)

	#SWR and Tagging
	def SWRaTag(self):
		self.swrText = []
		self.labels = []
		self.conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\akosh\\OneDrive\\Asztali gép\\USB copy\\Python Folder\\MableAI\\MableDatabase.accdb;')
		self.cursor = self.conn.cursor()

		for i in range(len(self.tokenisedText)):
			self.data = pandas.read_sql(sql = f"select Label from Words where Word = '{self.tokenisedText[i]}'", con = self.conn)
			if (self.data['Label'] == 'stop_word').all():
				continue
			else:
				self.swrText.append(self.tokenisedText[i])
				self.labels.append(self.data['Label'])

		print(self.swrText)
		print(self.labels)
		
engine = pyttsx3.init()

today = date.today()
Time = datetime.now()
current_time = Time.strftime("%H:%M")

functionIndex = "S"

#================================ Load Settings ================================

#speedSlide
rate = engine.getProperty("rate")
engine.setProperty("rate", settingsReader.speed * 20)

#voiceOptions
voices = engine.getProperty("voices")

if settingsReader.voice_profile == "Voice_1: British":
	engine.setProperty("voice", voices[1].id)

if settingsReader.voice_profile == "Voice_2: Australian":
	engine.setProperty("voice", voices[0].id)

#volumeSlide
volume = engine.getProperty("volume")
engine.setProperty("volume", settingsReader.volume/10)

#engine.say("I'm listening.")
#engine.runAndWait()

recogniser = sr.Recognizer()

def listen():
	functionIndex = 'L'
	
	while(functionIndex == "L"):   
		try:
			with sr.Microphone() as source:
				recogniser.adjust_for_ambient_noise(source, duration = 0.2)
				audio = recogniser.listen(source)
				Text = recogniser.recognize_google(audio)
				Text = Text.lower()

				abstractedInput = NLPS.LanguageAbstractor(Text)
				abstractedInput = abstractedInput.split()

				#cat = queryCat.Categorise(Text)
				#cat.FindCategory()

				print(abstractedInput)

				for i in range(0, len(abstractedInput)):

					if abstractedInput[i] == "news":
						webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://www.bbc.co.uk/news")
						break

					if abstractedInput[i] == "weather":
						webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j35i39j46i199i465i512j0i512j46i199i465i512j69i61l3.1452j0j7&sourceid=chrome&ie=UTF-8")

					if abstractedInput[i] == "my" and abstractedInput[i+1] == "name" and abstractedInput[i+2] == "is":
						engine.say("Nice to meet you," + abstractedInput[i+3])
						engine.runAndWait()
						break

					if abstractedInput[i] == "your" and abstractedInput[i+1] == "name":
						engine.say("My name is Mable")
						engine.say("What's yours?")
						engine.runAndWait()
						functionIndex = "S"
						break

					if abstractedInput[i] == "date":
						engine.say("The date is")
						engine.say(str(today))
						engine.runAndWait()
						functionIndex = "S"
						break

					if abstractedInput[i] == "time":
						engine.say("The time is")
						engine.say(current_time)
						engine.runAndWait()
						functionIndex = "S"
						break

					if abstractedInput[i] == "my" and abstractedInput[i+1] == "email":
						engine.say("Ok, opening your email.")
						engine.runAndWait()
						webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
						functionIndex = "S"
						break

					if abstractedInput[i] == "calendar":
						pyautogui.keyDown("Win")
						pyautogui.keyDown("alt")
						pyautogui.press("d")
						pyautogui.keyUp("Win")
						pyautogui.keyUp("alt")
						functionIndex = "S"
						break

					if abstractedInput[i] == "mable":
						engine.say("Yes?")
						engine.runAndWait()
						functionIndex = "S"
						break

				#Shut down
				if Text == "shut down":
					engine.say("Ok, shutting down.")
					engine.runAndWait()
					functionIndex = "O"
					break

				#Search
				if abstractedInput[0] == "search":
					Text = Text.replace("search", "")
					engine.say("Ok, here's what I found.")
					engine.runAndWait()
					webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://www.google.com/search?q="+Text+"&oq="+Text+"&aqs=chrome..69i57j35i39j46i199i465i512j0i512j46i199i465i512j69i61l3.1452j0j7&sourceid=chrome&ie=UTF-8")
					functionIndex = "S"
					break

				if abstractedInput[0] == "tell" and abstractedInput[1] == "me" and abstractedInput[2] == "about":
					Text = Text.replace("tell", "")
					Text = Text.replace("me", "")
					Text = Text.replace("about", "")
					engine.say("Okay, here's what I found on " + Text)
					engine.runAndWait()
					webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://en.wikipedia.org/wiki/"+Text)
					break

		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
			#engine.say("Request Error.")
			#engine.runAndWait()
			#import WakeMable
			functionIndex = 'O'
			break
			
		except sr.UnknownValueError:
			print("unknown error occured")
			#engine.say("Unknown Error.")
			#engine.runAndWait()
			#import WakeMable
			functionIndex = 'O'
			break

	if functionIndex != "L":
		pass