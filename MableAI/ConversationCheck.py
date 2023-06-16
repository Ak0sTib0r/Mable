import json
import random

conversationFile = open("ResponseLibrary.json")
phrases = json.load(conversationFile)

def CheckGreeting(userInput):
    for i in range(1, len(phrases["greetings"])):
        if userInput == phrases["greetings"][f"g{i}"] + " ":
            index = random.randint(1, len(phrases["greetings"]))
            response = phrases["greetings"][f"g{index}"]
            return response
        else:
            if i == len(phrases["greetings"]):
                return None

def CheckQuestion(userInput):
    if userInput == "what your name ":
        index = random.randint(1, len(phrases["name"]))
        response = phrases["name"][f"n{index}"]
        return response

    elif userInput == "how you ":
        index = random.randint(1, len(phrases["how_are_you"]))
        response = phrases["how_are_you"][f"h{index}"]
        return response

    else: 
        return None

def CheckMeet(userInput):
    if userInput == "nice meet you " or userInput == "pleasure meet you ":
        index = random.randint(1, len(phrases["my_name"]))
        response = phrases["my_name"][f"mn{index}"]
        return response