#File initialization, character cleaning, and word list population
fileName = "MarcusAureliusMeditations_Book1.txt"
file = open(fileName, "r")
wordList = []
badChars = [';', '+', '=', ',', '.']

for line in file:
    for word in line.split():
        if word not in wordList:
            cleanWord = ""
            for letter in word:
                if letter not in badChars:
                    cleanWord += letter
            wordList.append(cleanWord.lower())

#Word Uniqueness
commonWords = {}

for item in wordList:
    if commonWords.get(item) is not None:
        commonWords[item] += 1
    else:
        commonWords[item] = 1
wordCount = len(wordList)
uniqueWordCount = len(commonWords)

print("The total number of words: " + str(wordCount))
print("The total number of unique words: " + str(uniqueWordCount))
print("The percent of unique words is: %5.2f%%" % (uniqueWordCount/wordCount*100))
