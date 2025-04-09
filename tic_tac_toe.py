import random




r1 = [" ", "|", " ", "|", " "]
r2 = [" ", "|", " ", "|", " "]
r3 = [" ", "|", " ", "|", " "]
p = ["_________________________", str(r1), "_________________________", str(r2), "_________________________", str(r3)]




pBM = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def main():

    def ask(ans):
        if ans not in ["X", "O"]:
            ans = ask(input("\nInvalid, please only answer with (O) or (X):\n").upper())
        return ans




    def ask2(ans1, ans2):
        if ans1 not in ["1", "2", "3"]:
            if ans2 not in ["1", "2", "3"]:
                ans1, ans2 = ask2(input("\nInvalid row selection, please only answer with 1, 2 or, 3:\n"), input("\nInvalid placement on chosen row, please only answer with 1, 2 or 3:\n"))
            else:
                ans1, ans2 = ask2(input("\nInvalid row selection, please only answer with 1, 2 or, 3:\n"), ans2)
        elif ans2 not in ["1", "2", "3"]:
            ans1, ans2 = ask2(ans1, input("\nInvalid placement on chosen row, please only answer with 1, 2 or 3:\n"))
        return ans1, ans2




    choice = ask(input("\nWould you like to be O or X?:\n").upper())


    def check_w():
        if ((r1[0] == "X") and (r1[2] == "X") and (r1[4] == "X")) or ((r2[0] == "X") and (r2[2] == "X") and (r2[4] == "X")) or ((r3[0] == "X") and (r3[2] == "X") and (r3[4] == "X")) or ((r1[0] == "X") and (r2[0] == "X") and (r3[0] == "X")) or ((r1[2] == "X") and (r2[2] == "X") and (r3[2] == "X")) or ((r1[4] == "X") and (r2[4] == "X") and (r3[4] == "X")) or ((r1[0] == "X") and (r2[2] == "X") and (r3[4] == "X")) or ((r1[4] == "X") and (r2[2] == "X") and (r3[0] == "X")) or ((r1[0] == "O") and (r1[2] == "O") and (r1[4] == "O")) or ((r2[0] == "O") and (r2[2] == "O") and (r2[4] == "O")) or ((r3[0] == "O") and (r3[2] == "O") and (r3[4] == "O")) or ((r1[0] == "O") and (r2[0] == "O") and (r3[0] == "O")) or ((r1[2] == "O") and (r2[2] == "O") and (r3[2] == "O")) or ((r1[4] == "O") and (r2[4] == "O") and (r3[4] == "O")) or ((r1[0] == "O") and (r2[2] == "O") and (r3[4] == "O")) or ((r1[4] == "O") and (r2[2] == "O") and (r3[0] == "O")):
            print("You win!")
            exit()


    def ask3():
        r = random.choice(pBM)


        if r == 1:
            if r1[0] not in ["X", "O"]:
                r1[0] = bChoice
            else:
                ask3()
        if r == 2:
            if r1[2] not in ["X", "O"]:
                r1[2] = bChoice
            else:
                ask3()
        if r == 3:
            if r1[4] not in ["X", "O"]:
                r1[4] = bChoice
            else:
                ask3()
        if r == 4:
            if r2[0] not in ["X", "O"]:
                r2[0] = bChoice
            else:
                ask3()
        if r == 5:
            if r2[2] not in ["X", "O"]:
                r2[2] = bChoice
            else:
                ask3()
        if r == 6:
            if r2[4] not in ["X", "O"]:
                r2[4] = bChoice
            else:
                ask3()
        if r == 7:
            if r3[0] not in ["X", "O"]:
                r3[0] = bChoice
            else:
                ask3()
        if r == 8:
            if r3[2] not in ["X", "O"]:
                r3[2] = bChoice
            else:
                ask3()
        if r == 9:
            if r3[4] not in ["X", "O"]:
                r3[4] = bChoice
            else:
                ask3()


    if choice == "X":
        bChoice = "O"
    elif choice == "O":
        bChoice = "X"
        ask3()
        p = ["_________________________", str(r1), "_________________________", str(r2), "_________________________", str(r3)]






    for i in range(1, 9):


        for i in p:
            print(f"{i}")


        row, placement = ask2(input(f"\nWhich row would you like to put your {choice} to be? (1, 2, or 3):\n"), input(f"\nWould you like it to be in the 1st, 2nd or 3rd spot in that row?: (1, 2, 3)\n"))


        if choice == "X":
            if row == "1":
                if placement == "1":
                    if r1[0] not in ["X", "O"]:
                        r1[0] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r1[2] not in ["X", "O"]:
                        r1[2] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r1[4] not in ["X", "O"]:
                        r1[4] = "X"
                    else:
                        print("Invalid, try again")
                        continue




            if row == "2":
                if placement == "1":
                    if r2[0] not in ["X", "O"]:
                        r2[0] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r2[2] not in ["X", "O"]:
                        r2[2] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r2[4] not in ["X", "O"]:
                        r2[4] = "X"
                    else:
                        print("Invalid, try again")
                        continue




            if row == "3":
                if placement == "1":
                    if r3[0] not in ["X", "O"]:
                        r3[0] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r3[2] not in ["X", "O"]:
                        r3[2] = "X"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r3[4] not in ["X", "O"]:
                        r3[4] = "X"
                    else:
                        print("Invalid, try again")
                        continue




        check_w()


        ask3()




        if choice == "O":
            if row == "1":
                if placement == "1":
                    if r1[0] not in ["X", "O"]:
                        r1[0] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r1[2] not in ["X", "O"]:
                        r1[2] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r1[4] not in ["X", "O"]:
                        r1[4] = "O"
                    else:
                        print("Invalid, try again")
                        continue




            if row == "2":
                if placement == "1":
                    if r2[0] not in ["X", "O"]:
                        r2[0] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r2[2] not in ["X", "O"]:
                        r2[2] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r2[4] not in ["X", "O"]:
                        r2[4] = "O"
                    else:
                        print("Invalid, try again")
                        continue




            if row == "3":
                if placement == "1":
                    if r3[0] not in ["X", "O"]:
                        r3[0] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "2":
                    if r3[2] not in ["X", "O"]:
                        r3[2] = "O"
                    else:
                        print("Invalid, try again")
                        continue
                if placement == "3":
                    if r3[4] not in ["X", "O"]:
                        r3[4] = "O"
                    else:
                        print("Invalid, try again")
                        continue
        check_w()


        p = ["_________________________", str(r1), "_________________________", str(r2), "_________________________", str(r3)]
