def handleFile():
    while True:
        try:
            filename = input("Insert filename or filepath: ")
            file = open(filename, "r")
            break
        except FileNotFoundError:
            print("File not found. Insert valid filename.")
    fileAsString = file.read()
    file.close()
    return fileAsString.split()


def countWords(wordsInFile):
    counter = len(wordsInFile)
    for i in range(counter):
        if wordsInFile[i][-1] == '-':
            counter -= 1
    return counter


disclaimer = open("Disclaimer.txt", "r")
info = disclaimer.read()
disclaimer.close()
print(info)
fileAsList = handleFile()
wordsNumber = countWords(fileAsList)
print("Number of words in given file equals", wordsNumber)
