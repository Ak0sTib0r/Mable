import json

#================================ Load Settings ================================
sourceFile = open("Settings.json")
settings = json.load(sourceFile)

voice = settings["voice_options"]
activity = settings["active_times"]
style = settings["style"]

#Voice
voice_profile = voice["voice_ID"]
volume = float(voice["volume"])
speed = float(voice["speed"])

#Activity
start = activity["start_time"]
spart = activity["start_part"]
end = activity["end_time"]
epart = activity["end_part"]

#Style
theme = style["theme"]
