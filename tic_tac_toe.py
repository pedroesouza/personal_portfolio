import random

#Initial board rows
r1 = [" ", "|", " ", "|", " "]
r2 = [" ", "|", " ", "|", " "]
r3 = [" ", "|", " ", "|", " "]

#Possible bot moves
pBM = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    global r1, r2, r3, pBM

    #Ask user for X or O
    def ask(ans):
        if ans not in ["X", "O"]:
            return ask(input("Invalid input. Choose X or O:\n").upper())
        return ans

    #Ask user for move (row and column)
    def ask2(ans1, ans2):
        if ans1 not in ["1", "2", "3"]:
            ans1 = input("Invalid row. Choose 1, 2, or 3:\n")
            return ask2(ans1, ans2)
        if ans2 not in ["1", "2", "3"]:
            ans2 = input("Invalid column. Choose 1, 2, or 3:\n")
            return ask2(ans1, ans2)
        return ans1, ans2

    #Print board
    def print_board():
        print("_________________________")
        print("".join(r1))
        print("_________________________")
        print("".join(r2))
        print("_________________________")
        print("".join(r3))

    #Check for a winner
    def check_winner():
        wins = [
            [r1[0], r1[2], r1[4]],
            [r2[0], r2[2], r2[4]],
            [r3[0], r3[2], r3[4]],
            [r1[0], r2[0], r3[0]],
            [r1[2], r2[2], r3[2]],
            [r1[4], r2[4], r3[4]],
            [r1[0], r2[2], r3[4]],
            [r1[4], r2[2], r3[0]]
        ]
        for line in wins:
            if line == ["X", "X", "X"]:
                print_board()
                print("X wins!")
                exit()
            elif line == ["O", "O", "O"]:
                print_board()
                print("O wins!")
                exit()

    #Make a move for the bot
    def bot_move():
        while True:
            r = random.choice(pBM)
            if r == 1 and r1[0] == " ":
                r1[0] = bChoice
                break
            elif r == 2 and r1[2] == " ":
                r1[2] = bChoice
                break
            elif r == 3 and r1[4] == " ":
                r1[4] = bChoice
                break
            elif r == 4 and r2[0] == " ":
                r2[0] = bChoice
                break
            elif r == 5 and r2[2] == " ":
                r2[2] = bChoice
                break
            elif r == 6 and r2[4] == " ":
                r2[4] = bChoice
                break
            elif r == 7 and r3[0] == " ":
                r3[0] = bChoice
                break
            elif r == 8 and r3[2] == " ":
                r3[2] = bChoice
                break
            elif r == 9 and r3[4] == " ":
                r3[4] = bChoice
                break
            else:
                continue

            #prevent bot from choosing same move again
            pBM.remove(r)

    choice = ask(input("Would you like to be O or X?:\n").upper())
    bChoice = "O" if choice == "X" else "X"

    #If user is O, bot goes first
    if choice == "O":
        bot_move()

    #Main game loop
    for _ in range(5):  #Max 5 rounds
        print_board()

        row, col = ask2(
            input(f"Which row would you like to put your {choice} in? (1-3):\n"),
            input("Which column in that row? (1-3):\n")
        )

        row = int(row)
        col = int(col)

        #Convert input to board indices
        board_map = {1: 0, 2: 2, 3: 4}
        success = False

        if row == 1:
            if r1[board_map[col]] == " ":
                r1[board_map[col]] = choice
                success = True
        elif row == 2:
            if r2[board_map[col]] == " ":
                r2[board_map[col]] = choice
                success = True
        elif row == 3:
            if r3[board_map[col]] == " ":
                r3[board_map[col]] = choice
                success = True

        if not success:
            print("Invalid move! Try again.")
            continue

        check_winner()

        if _ < 4:  #Only let bot move if game not over
            bot_move()
            check_winner()

    print_board()
    print("It's a tie!")
