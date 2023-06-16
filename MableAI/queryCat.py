class Categorise:
    def __init__(self, nlpCompleteInput):
        self.nlpCompleteInput = nlpCompleteInput
        self.queryCategory = ["conversation", ""]
        self.askWords = ["what", "where", "how", "who", "why", "when", "is", "are", "was", "were"]
        self.commandWords = ["open", "search", "show", "tell", "play", "find", "start", "visit"]
    
    def FindCategory(self):
        for self.word in self.askWords:
            if self.nlpCompleteInput[0] == self.word:
                self.queryCategory = ["question", self.word]
                
        for self.word in self.commandWords:
            if self.nlpCompleteInput[0] == self.word:
                self.queryCategory = ["command", self.word]

        return self.queryCategory
                