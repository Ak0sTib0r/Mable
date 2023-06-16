import webbrowser
from datetime import date, datetime
import InstructionLibrary as IL

today = date.today()
Time = datetime.now()
current_time = Time.strftime("%H:%M")

#==================================== Instruction (Command) ====================================
def instruct(Text: str):
    inputText = Text.split()

    for i in range(0, len(inputText)):

        if inputText[i] == "tell" and inputText[i+1] == "me" and inputText[i+2] == "about":
            Text = Text.replace("tell", "")
            Text = Text.replace("me", "")
            Text = Text.replace("about", "")
            print("Okay, here's what I found on " + Text)
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://en.wikipedia.org/wiki/"+Text)
        
        if inputText[i] == "videos" and inputText[i+1] == "by":
            IL.PlayVideosBy(Text.replace("play videos by", ""))
            
        if inputText[i] == "open":
            for k in range(0, len(inputText)):
                if inputText[k] == 'email' or inputText[k] == 'gmail':
                    IL.OpenMail()
                    break
                else:
                    if k == len(inputText) - 1:
                        IL.OpenProgram(inputText[i+1])

        if inputText[i] == "news":
            IL.GetNews()

        if inputText[i] == "weather":
            IL.GetWeather()

        if inputText[i] == "my" and inputText[i+1] == "name" and inputText[i+2] == "is":
            print("Nice to meet you, " + inputText[i+3])

        if inputText[i] == "your" and inputText[i+1] == "name":
            IL.SayName()

        if inputText[i] == "date":
            IL.GetDate()

        if inputText[i] == "time":
            IL.GetTime() 

        if inputText[i] == "my" and inputText[i+1] == "email":
            IL.OpenMail()

        if inputText[i] == "calendar":
            IL.ShowCalendar()

        if inputText[i] == "visit":
            IL.VisitSite(inputText[i+1])

        if inputText[i] == "timer":
            for k in range(0, len(inputText)):
                if inputText[k] == 'minute' or inputText[k] == 'minutes':
                    IL.SetATimer(int(inputText[k - 1]))
                elif inputText[k] == 'hour' or inputText[k] == 'hours':
                    IL.SetATimer(int(inputText[k - 1]) * 60)

def search(query):
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("https://www.google.com/search?q="+query+"&oq="+query+"&aqs=chrome..69i57j35i39j46i199i465i512j0i512j46i199i465i512j69i61l3.1452j0j7&sourceid=chrome&ie=UTF-8")

        