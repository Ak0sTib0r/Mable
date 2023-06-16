import json

def SaveAll():
    table = open("table.txt")
    settings = table.readlines()

    with open('Settings.json', 'r+') as source: 
        data = json.load(source)
        
        #============================================Save Voice Options
        data["voice_options"]["voice_ID"] = settings[0].rstrip("\n")                                    
        source.seek(0)                                                                     
        json.dump(data, source, indent = 4)
        source.truncate()

        data["voice_options"]["volume"] = settings[1].rstrip("\n")  
        source.seek(0)        
        json.dump(data, source, indent = 4)
        source.truncate()

        data["voice_options"]["speed"] = settings[2].rstrip("\n") 
        source.seek(0)       
        json.dump(data, source, indent = 4)
        source.truncate()

        #============================================Save Active Times
        data["active_times"]["start_time"] = settings[3].rstrip("\n")  
        source.seek(0)        
        json.dump(data, source, indent = 4)
        source.truncate()

        data["active_times"]["start_part"] = settings[4].rstrip("\n")  
        source.seek(0)       
        json.dump(data, source, indent = 4)
        source.truncate()

        data["active_times"]["end_time"] = settings[5].rstrip("\n")  
        source.seek(0)        
        json.dump(data, source, indent = 4)
        source.truncate()

        data["active_times"]["end_part"] = settings[6].rstrip("\n")  
        source.seek(0)      
        json.dump(data, source, indent = 4)
        source.truncate()

        #============================================Save Style
        if settings[7].rstrip("\n")  == "Dark Theme":
            data["style"]["theme"] = "dark"
            source.seek(0)        
            json.dump(data, source, indent = 4)
            source.truncate()

        if settings[7].rstrip("\n")  == "Light Theme":
            data["style"]["theme"] = "light"
            source.seek(0)        
            json.dump(data, source, indent = 4)
            source.truncate()