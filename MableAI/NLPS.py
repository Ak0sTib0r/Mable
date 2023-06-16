#==================================== NLP System ====================================

#Remove Special Characters
def CutSymbols(speech: str) -> str:
    symbols = [',','.','!','?',':',';']

    for i in range(0, len(symbols)):
        speech = speech.replace(symbols[i], "")

    return speech

#Tokenisation
def Tokenise(speech: str) -> list[str]:
    tokenisedText = speech.split()

    return tokenisedText

#Simplify Ask Words
askWords = ["what", "where", "how", "who", "why", "when", "is", "are", "was", "were"]

def AskWordSimplifier(array) -> str:
    for i in range(0, len(array)):
        for j in range(0, len(askWords)):
            if array[i] == askWords[j] + "'s" or array[i] == askWords[j] + "'re" or array[i] == askWords[j] + "'d":
                array[i] = askWords[j]
    
    awsText = ""

    for word in array:
        awsText += word + " "

    return awsText

#Stop Word Removal
stopWords = ["and", "to", "is", "am", "are", "at", "a", "the", "with", "an", "be", "do", "please"]

def RemoveStopWords(tokenisedText: list[str]) -> list[str]:
    tokString = ""

    for i in range(0, len(stopWords)):
        for j in range(0 , len(tokenisedText)):
            if stopWords[i] == tokenisedText[j]:
                tokenisedText[j] = ""

    for word in tokenisedText:
        if word != "":
            tokString += word + " "

    tokenisedText = tokString.split()

    return tokenisedText

#Main Abstractor
def LanguageAbstractor(InputFromUser: str) -> list[str]:
    abstractedOutput = AskWordSimplifier(RemoveStopWords(Tokenise(CutSymbols(InputFromUser))))

    return abstractedOutput
