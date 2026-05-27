#!/usr/bin/python3

# Made with Love and Tailscale in 🇵🇱

import random
import sys

computer_score = 0
user_score = 0
print("The rules are simple: Rock beats Scissors, Paper beats Rock, and Scissors beats Paper. You can type 'exit' to quit the game.")
while True:
    try:
        randint = random.randint(1, 3)
        userinput = input("Rock (1), Paper (2), Scissors (3)? ")
        if userinput == "exit":
            print(f"Final score: You {user_score}, Computer {computer_score}")
            sys.exit(0)

        if randint == 1:
            computer = "Rock"
        elif randint == 2:
            computer = "Paper"
        else:
            computer = "Scissors"

        if userinput == "1":
            user = "Rock"
        elif userinput == "2":
            user = "Paper"
        elif userinput == "3":
            user = "Scissors"
        else:
            print("Invalid input. Please enter 1, 2, 3, or exit.")
            continue

        print("Computer: " + computer)
        print("You: " + user)

        if computer == user:
            print("It's a tie!")
        elif (
            (computer == "Rock" and user == "Scissors")
            or (computer == "Paper" and user == "Rock")
            or (computer == "Scissors" and user == "Paper")
        ):
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1

        if computer_score > user_score:
            print(f"You are losing {computer_score}, {user_score}")
        elif user_score > computer_score:
            print(f"You are winning {user_score}, {computer_score}")
        else:
            print("You are tied!")

    except KeyboardInterrupt:
        print(f"Bye Bye! The score was You: {user_score}, Computer: {computer_score}.")
        sys.exit(0)
