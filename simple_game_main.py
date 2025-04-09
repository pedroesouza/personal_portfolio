#This is Nicole's simple game user interface
#Whre most of the username info is (pedro)
from simple_games import one_ten as ten, one_hundred as hundred

#Controls the running of games and saving of scores and users
def simple_game_main():
    while True:
        choice = input("\nWelcome to the SIMPLE GUESSING GAME!\n What would you like to do? \n 1) Guess 1-10\n 2) Guess 1-100\n 3) EXIT to the main menu\n")
        if choice == '1':
            while True:
                score, oneTen, username = ten() #Runs game and stores score, whether the player is done playing, and name
                if 'end' in oneTen:
                    with open('High Score Tracker/simple_game1-10.csv','a') as file:
                        file.write(f"\n{username},{score}") #Saves username and score to a row in the correct csv file
                    break       
        elif choice == '2':
            while True:
                score, oneHundred, username = hundred() #runs game and stores score, whether the player is done playing, and name
                if 'end' in oneHundred:
                    with open('High Score Tracker/simple_game1-100.csv','a') as file:
                        file.write(f"\n{username},{score}") #Saves username and score to a row in the correct csv file
                    break
        elif choice == '3':
            break
