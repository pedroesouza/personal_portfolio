#Pedro Souza, Pig latin translator

#List of letters that are vowels
vowels = ["a", "e", "i", "o", "u"]

#Only function, the one that translates
def translate():
    word = input("Your word (please all lowercase): ")
    firstLetter = word[0]
    if firstLetter in vowels: #just ads yay if first letter is a vowel
        print("Original word:", word)
        word += "yay"
        print(word)
    else:
        wordList = list(word) #do the whole process of moving consonants  + adding ay if not
        while firstLetter not in vowels:
            wordList.append(firstLetter)
            wordList.pop(0)
            firstLetter = wordList[0]

        print("Original word:", word)
        word = "".join(wordList)
        word += "ay"
        print("Pig latin translation:", word)
