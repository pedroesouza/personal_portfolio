#Pedro Souza, Shift cypher

#list of all characters and corresponding
alphabet = "  abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA0123456789012"

#gives user options of what to do
def main():
    choice = input("Would you like to encode or incode or leave: ")
    if choice == "encode":
        encode(input("What is your word to encode: "))
    elif choice == "incode":
        incode(input("What is your word to incode: "))
    elif choice == "leave":
        return

#Function that shifts a normal word
def encode(word):
    wordLen = len(word)
    newWord = []
    repeats = 0
    for x in word:
        letter = x
        whereLetter = alphabet.index(letter)
        newWord.insert(repeats, alphabet[whereLetter + 1])
        word = "".join(newWord)
        repeats += 1
    print("encoded:",word)

#Function to decypher
def incode(word):
    wordLen = len(word)
    newWord = []
    repeats = 0
    for x in word:
        letter = x
        whereLetter = alphabet.index(letter)
        newWord.insert(repeats, alphabet[whereLetter - 1])
        word = "".join(newWord)
        repeats += 1
    print("decoded:", word)
