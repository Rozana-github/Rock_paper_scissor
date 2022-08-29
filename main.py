"""
# This is a simple Rock Paper scissor game
- Rock vs paper  then paper win because paper can cover the rock
- Rock vs scissor then Rock wins
- paper vs scissor then scissor wins
"""

import random

l = ["rock", "scissor", "paper"]

while True:
    ucount = 0
    ccount = 0
    uc = int(input('''
    Game start....
    1. Yes
    2. NO / Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
1. rock
2. scissor 
3. paper 
        
       '''))

            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"
            cchoice = random.choice(l)
            if uchoice == cchoice:
                print("user given value", uchoice)
                print("computer given value", cchoice)
                print("Game draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == " paper " and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "paper"):
                print("You Win ! Congratulations !")
                ucount = ucount + 1
            else:
                print("user given value", uchoice)
                print("computer given value", cchoice)
                print("Computer win")
                ccount = ccount + 1

            if ucount == ccount:
                print("Final game is Draw")
                print("User score", ucount)
                print("Computer score", ccount)

            elif ucount > ccount:
                print("Finally you win !")
                print("User score", ucount)
                print("Computer score", ccount)
            else:
                print("Computer  win !")
                print("User score", ucount)
                print("Computer score", ccount)
    else:
        break
