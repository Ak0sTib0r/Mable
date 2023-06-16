library = open("stop_words.txt")
content = library.readlines()

index = 0

def encrypt(content, index):
    for k in range(len(content)):
        content[k] = content[k].lower().rstrip("\n")
        for i in range(len(content[k])):
            charCode = ord(content[k][i]) - 97
            charInWord = len(content[k]) - i
            finalIndex = (26**(charInWord - 1)) * charCode
            index += finalIndex

        index += 1
        index += (26**(len(content[k]) - 1))

        #print(f"{content[k]}: Word index is {index + 1} with {len(content[k])} letters")
        print(index)
        index = 0
    
encrypt(content, index)

library.close()
