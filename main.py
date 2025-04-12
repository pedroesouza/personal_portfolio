#Pedro Souza, Personal Portfolio

#import needed library
import fontstyle

#import the functions from other files
from introduction import main as introduction
from morse_code_translator import main as morse_code_translator
from pig_latin_converter import translate as pig_latin_converter
from random_password_generator import main as random_password_generator
from high_score_tracker import main as high_score_tracker
from tic_tac_toe import main as tic_tac_toe
from shift_cypher import main as shift_cypher

#main function for the user's choice
def main():
    choice = input(fontstyle.apply("""\nChose the project by writing the number, and going to the next line by pressing enter:
          1: Morse code translator
          2. Pig latin converter
          3. Random password generator
          4. High score tracker
          5. Tic-tac-toe
          6. Shift cypher
          7. Leave
        
          Your answer here: """, "Italic")) #Asks the user for what program they should run
    

    if choice == "1":
        print(fontstyle.apply("Welcome to the morse code translator! As it can be assumed by the name, this project takes in any input and converts it into morse code (and vice versa). This project was a solo project done for my programming class in 2025. I learned much about how to manipulate lits, functional decomposit and use loops better in this project.\n", "Italic"))
        morse_code_translator()
    elif choice == "2":
        print(fontstyle.apply("Welcome to the pig latin converter! As it can be assumed by the name, this project takes in any input and converts it into pig latin. This project was a solo project done for my programming class in 2024. I learned much about how to edit strings and lists, and additionally how to think like a programmer in this project. I am particularlly proud of the logic in this project.\n", "Italic"))
        pig_latin_converter()
    elif choice == "3":
        print(fontstyle.apply("Welcome to the random password generation! This project creates random passwords for you based off YOUR choices! This project was a solo project done for my programming class in 2025. I had the experience of learning logic, how to use ascii and functions well.\n", "Italic"))
        random_password_generator()
    elif choice == "4":
        print(fontstyle.apply("Welcome to the high score tracker! This project can run a game, and store them in a csv, displaying the high scores with usernames. This project was a group project done for my programming class in 2025, my role was extra credit stuff/UI designer. I learned much about CSVs, txt files, and how to use multiple files in this project.\n", "Italic"))
        high_score_tracker()
    elif choice == "5":
        print(fontstyle.apply("Welcome to the tic tac toe! This project runs a simple tic tac toe game with enemy bots. This project was a solo project done for my programming class in 2024. I learned much about if statements and how to properly format print and stings in this project.\n", "Italic"))
        tic_tac_toe()
    elif choice == "6":
        print(fontstyle.apply("Welcome to the shift cypher! This project will get an input and either encode it with a shift cypher algorythim, or incode (translate them) back to normal. This project was a solo project done for my programming class in 2024. I learned much about the editing on stings, and how to make code consise in this project. I am particularlly proud of the logic in this project.\n", "Italic"))
        shift_cypher()
    elif choice == "7":
        exit()
    else: #Error handling
        print("INVALID INPUT")

#Just runs the intro once
introduction()

#Loops main until it is exited
while True:
    main()