#!/usr/bin/python3

# Number guessing game

# Initialization and import:
import random
import sys

print_number = "--show-number" in sys.argv[1:]
number = random.randint(1, 100)
if print_number:
    print(number)

# Game logic:

guess_number = 1
while True:
    try:
        guess = int(input(f"What is your guess (number {guess_number})? "))
    except ValueError:
        print("NOPE! That is not a number, you monkey! Try again.")
        continue

    guess_number += 1

    if guess == number:
        print(f"Congratulations! Your guess ({number}) is correct!")
        sys.exit(0)

    if guess < 1 or guess > 100:
        print("?! That is not valid, you monkey! Please very kindly enter a number from 1 to 100.")
        continue

    diff = abs(guess - number)
    if diff > 20:
        print("Sorry, that's not quite right! You're cold.")
    elif diff > 10:
        print("Sorry, that's not quite right! You're warmer.")
    elif diff > 5:
        print("Sorry, that's not quite right! You're hot.")
    else:
        print("Sorry, that's not quite right, but you're so hot it might melt your face off!")
