import time
from datetime import datetime
import settingsReader
import os

checkStart = True
checkEnd = False

currentTime = f"%H:{'00'}"

if settingsReader.spart == "PM":
    startTime = str(int(settingsReader.start.replace(':00', '')) + 12) + ':00'
else:
    startTime = settingsReader.start

if settingsReader.epart == "PM":
    endTime = str(int(settingsReader.end.replace(':00', '')) + 12) + ':00'
else:
    endTime = settingsReader.end

while checkStart == True:

    Time = datetime.now()

    if Time.strftime(currentTime) == startTime:
        import Mable
        checkStart = False
        checkEnd = True

    time.sleep(60)

while checkEnd == True:

    Time = datetime.now()

    if Time.strftime(currentTime).replace(':', '') == endTime:
        Mable.functionIndex = "O"
        checkEnd = False

    time.sleep(60)