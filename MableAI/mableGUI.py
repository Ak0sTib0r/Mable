import customtkinter
import settingsReader
import settingsWriter
import os

customtkinter.set_appearance_mode(settingsReader.theme)
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x600")
root.title("Mable AI - Personal Assistant")
root.wm_resizable(width = False, height = False)

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 30, padx = 0, fill = "both", expand = True)

logoLabel = customtkinter.CTkLabel(master = frame, text = "MABLE", font = ("Roboto", 25), text_color = "gray")
logoLabel.pack(padx = 50, pady = 200)

#================================ Save Settings ================================
def writeSettings(self):
    settingsWriter.SaveAll()

def saveSettings(self):
    table = open("table.txt", "a")
    table.truncate(0)
    table.write(voiceOptions.get() + "\n")
    table.write(str(volumeSlide.get()) + "\n")
    table.write(str(speedSlide.get()) + "\n")
    table.write(setStartTime.get() + "\n")
    table.write(setStartPart.get() + "\n")
    table.write(setEndTime.get() + "\n")
    table.write(setEndPart.get() + "\n")
    table.write(styleSelect.get() + "\n")
    table.close()
    writeSettings(self)

#================================ Input Text Area ================================
userInput = customtkinter.CTkEntry(master = root, placeholder_text = "Type Here...")
userInput.place(x = 0, y = root._current_height - 30)
userInput._set_dimensions(width = 310, height = 30)

#================================== Stack Management Function =================================
messageStack = []

import MessageModule

def StackManagement():
    newMessage = MessageModule.Message(userInput.get().lower(), 0)
    MessageModule.UpdateMessagePos(messageStack, newMessage)

#================================== Displaying Mable's Responses =================================
def DisplayAIResponse(response):
    messageLabel = customtkinter.CTkLabel(master = frame, text = "Mable: " + response, font = ("Helvetica", 15))
    messLabelStack.append(messageLabel)

    MessageModule.StackManagement(response.lower())

    for messageIndex in range(0, len(messLabelStack)):
        messLabelStack[messageIndex].place(x = 10, y = frame._current_height - int(MessageModule.messageStack[messageIndex][1]) - 20)

#================================== Ask Function =================================
import mableWText
import queryCat
import NLPS
import ConversationCheck as cc

messLabelStack = []

def ask():

    messageLabel = customtkinter.CTkLabel(master = frame, text = "You: " + userInput.get(), font = ("Helvetica", 15))
    messLabelStack.append(messageLabel)

    MessageModule.StackManagement(userInput.get().lower())

    for messageIndex in range(0, len(messLabelStack)):
        messLabelStack[messageIndex].place(x = 10, y = frame._current_height - int(MessageModule.messageStack[messageIndex][1]) - 20)

    if userInput.get() == "cls":
        os._exit(0)

    abstractedInput = NLPS.LanguageAbstractor(userInput.get().lower())
    
    #Categorisation
    cat = queryCat.Categorise(abstractedInput.split())
    category = cat.FindCategory()

    if category[0] == "command":
        mableWText.instruct(abstractedInput)

    elif category[0] == "question":
        if category[1] == "what" or category[1] == "how":
            response = cc.CheckQuestion(abstractedInput)
            if response == None:
                mableWText.search(abstractedInput)
            else:
                DisplayAIResponse(response.capitalize())
        else:
            mableWText.search(abstractedInput)

    elif category[0] == "conversation":
        response = cc.CheckGreeting(abstractedInput)
        if response == None:
            response = cc.CheckMeet(abstractedInput)
            DisplayAIResponse(response.capitalize())
        else:
            DisplayAIResponse(response.capitalize())
             
    userInput.delete(0, len(userInput.get()))

askButton = customtkinter.CTkButton(master = root, text = "--->", command = ask)
askButton.place(x = 310, y = root._current_height - 30)
askButton._set_dimensions(width = 90, height = 30)

#====================================== Listen Button =====================================
import Mable

def listen():
    Mable.listen()

listenButton = customtkinter.CTkButton(master = root, text = "Listen", command = listen)
listenButton.place(x = root._current_width - 90, y = 0)
listenButton._set_dimensions(width = 90, height = 30)

#================================ Settings Window Def ================================
def settingsGUI():
    settingsFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    frame.pack_forget()

#================================= Voice Options Def ================================
def voiceOptionsGUI():
    voiceFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    settingsFrame.pack_forget()

#================================= Active Times Def ================================
def activeTimesGUI():
    activeTimesFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    settingsFrame.pack_forget()

#================================= Style Def ================================
def styleGUI():
    styleFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    settingsFrame.pack_forget()

settingsButton = customtkinter.CTkButton(master = root, text = "Settings", command = settingsGUI, fg_color = "gray")
settingsButton.place(x = 0, y = 0)
settingsButton._set_dimensions(width = 45, height = 30)

#================================ Settings Frame ================================
def backToFrame():
    frame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    settingsFrame.pack_forget()

settingsFrame = customtkinter.CTkFrame(master = root)

settingsLabel = customtkinter.CTkLabel(master = settingsFrame, text = "Settings", font = ("Roboto", 25))
settingsLabel.pack(padx = 12, pady = 10)

voiceOptions = customtkinter.CTkButton(master = settingsFrame, text = "Voice Options", command = voiceOptionsGUI)
voiceOptions.pack(padx = 12, pady = 10)

operationTimes = customtkinter.CTkButton(master = settingsFrame, text = "Active Times", command = activeTimesGUI)
operationTimes.pack(padx = 12, pady = 10)

styleOptions = customtkinter.CTkButton(master = settingsFrame, text = "Style", command = styleGUI)
styleOptions.pack(padx = 12, pady = 10)

backToMain = customtkinter.CTkButton(master = settingsFrame, text = "Back", fg_color = "gray", command = backToFrame)
backToMain.pack(padx = 12, pady = 10)

#================================ Voice Options Frame ================================
def backToSettV():
    settingsFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    voiceFrame.pack_forget()

voiceFrame = customtkinter.CTkFrame(master = root)

settingsLabel = customtkinter.CTkLabel(master = voiceFrame, text = "Voice Options", font = ("Roboto", 25))
settingsLabel.pack(padx = 12, pady = 10)

voiceOptions = customtkinter.CTkOptionMenu(master = voiceFrame, values = ["Voice_1: British", "Voice_2: Australian"], command = saveSettings)
voiceOptions.place(x = 10, y = 80)
voiceOptions.set(settingsReader.voice_profile)

volumeLabel = customtkinter.CTkLabel(master = voiceFrame, text = "Volume", font = ("Roboto", 15))
volumeLabel.place(x = 10, y = 130)

volumeSlide = customtkinter.CTkSlider(master = voiceFrame, from_ = 0, to = 10, width = 200, height = 10, command = saveSettings)
volumeSlide.place(x = 70, y = 140)
volumeSlide.set(settingsReader.volume)

speedLabel = customtkinter.CTkLabel(master = voiceFrame, text = "Speed", font = ("Roboto", 15))
speedLabel.place(x = 10, y = 170)

speedSlide = customtkinter.CTkSlider(master = voiceFrame, from_ = 0, to = 10, width = 200, height = 10, command = saveSettings)
speedSlide.place(x = 70, y = 180)
speedSlide.set(settingsReader.speed)

backToSettings = customtkinter.CTkButton(master = voiceFrame, text = "Back", fg_color = "gray", command = backToSettV)
backToSettings.pack(padx = 12, pady = 200)

#================================ Active Times Frame ================================
def backToSettAT():
    settingsFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    activeTimesFrame.pack_forget()

timeOptions = ['01:00', '02:00', '03:00', '04:00', '05:00' ,'06:00' ,'07:00', '08:00', '09:00', '10:00', '11:00', '12:00']
dayPartOptions = ['AM', 'PM']

activeTimesFrame = customtkinter.CTkFrame(master = root)

activeTimesLabel = customtkinter.CTkLabel(master = activeTimesFrame, text = "Active Times", font = ("Roboto", 25))
activeTimesLabel.pack(padx = 12, pady = 10)

backToSettingsAT = customtkinter.CTkButton(master = activeTimesFrame, text = "Back", fg_color = "gray", command = backToSettAT)
backToSettingsAT.pack(padx = 12, pady = 200)

startTimeLabel = customtkinter.CTkLabel(master = activeTimesFrame, text = "Start", font = ("Roboto", 15))
startTimeLabel.place(x = 10, y = 80)

endTimeLabel = customtkinter.CTkLabel(master = activeTimesFrame, text = "End", font = ("Roboto", 15))
endTimeLabel.place(x = 10, y = 120)

setStartTime = customtkinter.CTkOptionMenu(master = activeTimesFrame, values = timeOptions, command = saveSettings)
setStartTime.place(x = 70, y = 80)
setStartTime.set(settingsReader.start)

setStartPart = customtkinter.CTkOptionMenu(master = activeTimesFrame, values = dayPartOptions, command = saveSettings)
setStartPart.place(x = 210, y = 80)
setStartPart.set(settingsReader.spart)

setEndTime = customtkinter.CTkOptionMenu(master = activeTimesFrame, values = timeOptions, command = saveSettings)
setEndTime.place(x = 70, y = 120)
setEndTime.set(settingsReader.end)

setEndPart = customtkinter.CTkOptionMenu(master = activeTimesFrame, values = dayPartOptions, command = saveSettings)
setEndPart.place(x = 210, y = 120)
setEndPart.set(settingsReader.epart)

#====================================== Style Frame =====================================
def backToSettS():
    settingsFrame.pack(pady = 0, padx = 0, fill = "both", expand = True)
    styleFrame.pack_forget()

def changeStyle(self):
    if styleSelect.get() == "Dark Theme":
        customtkinter.set_appearance_mode("dark")

    if styleSelect.get() == "Light Theme":
        customtkinter.set_appearance_mode("light")

    saveSettings(self)

styleFrame = customtkinter.CTkFrame(master = root)

styleLabel = customtkinter.CTkLabel(master = styleFrame, text = "Style", font = ("Roboto", 25))
styleLabel.pack(padx = 12, pady = 10)

backToSettingsS = customtkinter.CTkButton(master = styleFrame, text = "Back", fg_color = "gray", command = backToSettS)
backToSettingsS.pack(padx = 12, pady = 200)

styleSelectLabel = customtkinter.CTkLabel(master = styleFrame, text = "Style Options", font = ("Roboto", 15))
styleSelectLabel.place(x = 10, y = 80)

styleSelect = customtkinter.CTkOptionMenu(master = styleFrame, values = ["Dark Theme", "Light Theme"], command = changeStyle)
styleSelect.place(x = 110, y = 80)

if settingsReader.theme == "dark":
    styleSelect.set("Dark Theme")

if settingsReader.theme == "light":
    styleSelect.set("Light Theme")

root.mainloop()