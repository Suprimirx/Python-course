import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    playerchoise = input("\nEnter...\n1 for Rock\n2 for Paper, or\n3 for Scissors\n\n" )

    player = int(playerchoise)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3")

    # sys.exit("You must enter 1, 2, or 3") if player < 1 or player > 3 else None

    computerchoise = random.choice("123")

    computer = int(computerchoise)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("🎉You win!")
    elif player == 2 and computer == 1:
        print("🎉You win!")
    elif player == 3 and computer == 2:
        print("🎉You win!")
    elif player == computer:
        print("🥵It's a tie!")
    else:
        print("🐍Python wins!")

    playagain = input("\nPlay again? \nY for Yes or \nq to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n👌👌")
        print("Thank you for playing!\n")
        playagain = False
    
sys.exit("Bye! 👋")