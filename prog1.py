
def fileN():
        fileName = input("Enter the file name ")
        word = 0
        file=open(fileName , 'r')
        for i in file:
            words = i.split()
            word = word + len(words)
        print(word)
fileN()
