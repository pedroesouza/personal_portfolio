#This is Nicole's simple game functions
import random

def save_user(userName): #Functun saves username so it can be returned and put on file
    if len(userName) == 3: #Only saves when the username is 3 characters long
        return userName
    else:
        userName = save_user(input("Invalid username, what is your username? (Please make it 3 characters) ").upper())
        return userName

def one_ten(): #The user guesses from 1-10
    score = 0
    current = 0
    streak = 0
    username = save_user(input("What is your username? (Please make it 3 characters) ").upper())
    while True:
            comp_num = random.randint(1,10)
            while True:
                #Error handling for making sure the user chooses a number
                try:
                    user_num = int(input("\nGuess a number from 1-10!\n      "))
                    if user_num >= 1 and user_num <= 10:
                        pass
                    else:
                        print("-------\nCHOOSE FROM 1-10\n-------")
                        continue
                except ValueError:
                    print("Please choose a valid NUMBER.")
                    continue
                if user_num == comp_num: #Checks to see if the user picked the right number
                    print("\n--------------CONGRATTS!!!! YOU DID IT----------------\n")
                    streak+=1
                    #Depending on how many times it takes for the user to get the right answer, they can get a score increase or boost
                    if current <= 3 and current > 0:
                        score = score+streak*2
                        current = 0
                    elif current > 3:
                        score+=1
                        current = 0
                    elif current == 0:
                        score = score+streak*4
                    while True:
                        play = input(f"SCORE: {score}\nSTREAK: {streak}\nWould you like to keep playing?(yes or no)\n ").title()
                        if play == 'No':
                            return score, 'end', username 
                        elif play == 'Yes':
                            break
                        elif play != 'Yes' and play != 'No':
                            print("Choose yes or no. ")
                            continue
                    break
                elif user_num != comp_num:
                    #Checks to see if the user needs to guess higher or lower
                    if user_num > comp_num:
                        print("Go a bit lower!")
                    elif user_num < comp_num:
                        print("Go higher!")
                    print("\n")
                    streak = 0
                    current+=1
                    continue


def one_hundred(): #The user guesses 1-100
    score = 0
    current = 0
    streak = 0
    username = save_user(input("What is your username? (Please make it 3 characters) ").upper()) #Gets username from user
    while True:
            comp_num = random.randint(1,100)
            while True:
                #Error handling for making sure the user chooses a number
                try:
                    user_num = int(input("\nGuess a number from 1-100!\n      "))
                    if user_num >= 1 and user_num <= 100:
                        pass
                    else:
                        print("-------\nCHOOSE FROM 1-100\n-------")
                        continue
                except ValueError:
                    print("Please choose a valid NUMBER.")
                    continue
                if user_num == comp_num:
                    print("\n--------------CONGRATTS!!!! YOU DID IT----------------\n")
                    streak+=1
                    #Depending on how many times it takes for the user to get the right answer, they can get a score increase or boost
                    if current <= 3 and current > 0:
                        score = score+streak*2
                        current = 0
                    elif current > 3:
                        score+=1
                        current = 0
                    elif current == 0:
                        score = score+streak*4
                    while True:
                        play = input(f"SCORE: {score}\nSTREAK: {streak}\nWould you like to keep playing?(yes or no)\n ").title()
                        if play == 'No':
                            return score, 'end', username
                        elif play == 'Yes':
                            break
                        elif play != 'Yes' and play != 'No':
                            print("Choose yes or no. ")
                            continue
                    break
                elif user_num != comp_num:
                    #Checks to see if the user needs to guess higher or lower
                    if user_num > comp_num:
                        print("Go a bit lower!")
                    elif user_num < comp_num:
                        print("Go higher!")
                    print("\n")
                    streak = 0
                    current+=1
                    continue