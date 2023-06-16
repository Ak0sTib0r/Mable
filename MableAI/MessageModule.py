unitSize = 20

class Message:
    def __init__(self, text, pos):
        self.pos = pos
        self.text = text

def UpdateMessagePos(Stack, newMess):
    Stack.append([str(newMess.text), newMess.pos])

    for messageIndex in range(len(Stack)):
        Stack[messageIndex][1] = str((len(Stack) - messageIndex) * unitSize)

messageStack = []

def StackManagement(text):
    newMessage = Message(text, 0)
    UpdateMessagePos(messageStack, newMessage)