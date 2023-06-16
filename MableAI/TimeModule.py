import time
import pyttsx3
import settingsReader

engine = pyttsx3.init()

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

class Timer:
    def __init__(self, waitTime):
        self.waitTime = waitTime

    def SetTimer(self):
        engine.say(f"Okay. Timer set for {self.waitTime} minutes.")
        engine.runAndWait()

        time.sleep(60 * self.waitTime)
        
        engine.say("Time! Your timer has finished.")
        engine.runAndWait()